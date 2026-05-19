import requests


class WikiSearchTool:

    SEARCH_URL = "https://en.wikipedia.org/w/api.php"

    SUMMARY_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"

    HEADERS = {
        "User-Agent": "WikiResearchAgent/1.0 (avinash@example.com)"
    }

    def search(self, query):

        print("[Tool] Searching Wikipedia...")

        search_params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json"
        }

        search_response = requests.get(
            self.SEARCH_URL,
            params=search_params,
            headers=self.HEADERS
        )

        search_data = search_response.json()

        search_results = search_data.get("query", {}).get("search", [])

        if not search_results:
            return {
                "error": "No results found"
            }

        page_title = search_results[0]["title"]

        print(f"[Tool] Found Page: {page_title}")

        formatted_title = page_title.replace(" ", "_")

        summary_url = self.SUMMARY_URL + formatted_title

        summary_response = requests.get(
            summary_url,
            headers=self.HEADERS
        )

        print(f"[Tool] Summary Status: {summary_response.status_code}")

        if summary_response.status_code != 200:
            return {
                "error": "Could not fetch summary"
            }

        summary_data = summary_response.json()

        return {
            "title": summary_data.get("title"),
            "summary": summary_data.get("extract"),
            "source": summary_data.get("content_urls", {})
                                  .get("desktop", {})
                                  .get("page")
        }