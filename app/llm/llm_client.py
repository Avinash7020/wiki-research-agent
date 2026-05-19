from groq import Groq
from dotenv import load_dotenv
import os


load_dotenv()


class LLMClient:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def generate_report(self, content):

        prompt = f"""
        Create a professional markdown research report.

        Content:
        {content}

        Include:
        - Title
        - Introduction
        - Key Insights
        - Technical Overview
        - Conclusion

        Format properly in markdown.
        """

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content