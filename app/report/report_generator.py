from datetime import datetime


class ReportGenerator:

    def save_report(self, topic, content):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"reports/{topic}_{timestamp}.md"

        filename = filename.replace(" ", "_")

        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"[Report Generator] Report saved: {filename}")

        return filename