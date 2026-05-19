from app.tools.wiki_search_tool import WikiSearchTool


def main():

    tool = WikiSearchTool()

    result = tool.search("Artificial Intelligence")

    print(result)


if __name__ == "__main__":
    main()