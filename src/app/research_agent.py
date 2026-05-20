import json
import os

from dotenv import load_dotenv
from openai import OpenAI

try:
    from .report.report_generator import ReportGenerator
    from .tools.wiki_search_tool import WikiSearchTool
except ImportError:
    from report.report_generator import ReportGenerator
    from tools.wiki_search_tool import WikiSearchTool


load_dotenv()


class WikiResearchAgent:
    def __init__(self):
        self.client = OpenAI()
        self.model = os.getenv("OPENAI_MODEL", "gpt-5.5")
        self.wiki_tool = WikiSearchTool()
        self.report_generator = ReportGenerator()
        self.tools = [
            {
                "type": "function",
                "name": "search_wikipedia",
                "description": "Search Wikipedia for a topic and return the best matching page summary.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "The topic to search on Wikipedia.",
                        }
                    },
                    "required": ["query"],
                    "additionalProperties": False,
                },
                "strict": True,
            }
        ]

    def run(self, query):
        input_items = [
            {
                "role": "user",
                "content": (
                    f"Research {query} using Wikipedia and write a concise markdown report."
                ),
            }
        ]

        response = self._create_response(input_items)

        while True:
            function_calls = [
                item for item in response.output if item.type == "function_call"
            ]
            if not function_calls:
                break

            # Preserve the model's tool call items so the next request can match
            # each function_call_output back to its originating call_id.
            input_items.extend(response.output)

            for call in function_calls:
                result = self._run_tool(call.name, call.arguments)
                input_items.append(
                    {
                        "type": "function_call_output",
                        "call_id": call.call_id,
                        "output": json.dumps(result, ensure_ascii=False),
                    }
                )

            response = self._create_response(input_items)

        report = response.output_text.strip()
        saved_file = self.report_generator.save_report(query, report)

        return {
            "report": report,
            "file": saved_file,
        }

    def _create_response(self, input_items):
        return self.client.responses.create(
            model=self.model,
            instructions=(
                "Use the Wikipedia tool when needed. "
                "Return only the final markdown report."
            ),
            tools=self.tools,
            input=input_items,
        )

    def _run_tool(self, name, arguments):
        if name != "search_wikipedia":
            return {"error": f"Unknown tool: {name}"}

        try:
            args = json.loads(arguments) if arguments else {}
        except json.JSONDecodeError:
            return {"error": "Invalid tool arguments"}

        query = args.get("query", "").strip()
        if not query:
            return {"error": "Missing query"}

        return self.wiki_tool.search(query)
