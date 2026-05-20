try:
    from .research_agent import WikiResearchAgent
except ImportError:
    from research_agent import WikiResearchAgent


def main():
    query = input("Enter topic: ")

    result = WikiResearchAgent().run(query)

    print("\n===== FINAL REPORT =====\n")
    print(result["report"])
    print("\n===== FILE SAVED =====\n")
    print(result["file"])


if __name__ == "__main__":
    main()
