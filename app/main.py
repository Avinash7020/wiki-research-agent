from app.llm.llm_client import LLMClient


def main():

    llm = LLMClient()

    content = """
    Artificial Intelligence is a branch of computer science
    focused on building intelligent systems.
    """

    result = llm.generate_report(content)

    print(result)


if __name__ == "__main__":
    main()