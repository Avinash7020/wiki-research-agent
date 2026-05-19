from app.agent.wiki_agent import WikiAgent


def main():

    query = input("Enter topic: ")

    agent = WikiAgent()

    result = agent.run(query)

    print("\n===== FINAL REPORT =====\n")

    print(result["report"])

    print("\n===== FILE SAVED =====\n")

    print(result["file"])


if __name__ == "__main__":
    main()