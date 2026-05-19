from app.tools.wiki_search_tool import WikiSearchTool
from app.llm.llm_client import LLMClient


class WikiAgent:

    def __init__(self):

        self.wiki_tool = WikiSearchTool()

        self.llm = LLMClient()

    def run(self, query):

        print("[Agent Thinking] Need external knowledge...")

        print("[Agent Action] Using Wikipedia Tool...")

        wiki_result = self.wiki_tool.search(query)

        if "error" in wiki_result:
            return wiki_result["error"]

        print("[Agent Observation] Knowledge retrieved")

        content = f"""
        Title:
        {wiki_result['title']}

        Summary:
        {wiki_result['summary']}

        Source:
        {wiki_result['source']}
        """

        print("[Agent Thinking] Generating AI report...")

        report = self.llm.generate_report(content)

        return report