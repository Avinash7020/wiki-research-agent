from app.tools.wiki_search_tool import WikiSearchTool
from app.llm.llm_client import LLMClient
from app.report.report_generator import ReportGenerator


class WikiAgent:

    def __init__(self):

        self.wiki_tool = WikiSearchTool()

        self.llm = LLMClient()

        self.report_generator = ReportGenerator()

    def run(self, query):

        print("[Agent Thinking] Need external knowledge...")

        print("[Agent Action] Using Wikipedia Tool...")

        wiki_result = self.wiki_tool.search(query)

        if "error" in wiki_result:
            return {
                "report": wiki_result["error"],
                "file": None
            }

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

        saved_file = self.report_generator.save_report(
            query,
            report
        )

        return {
            "report": report,
            "file": saved_file
        }