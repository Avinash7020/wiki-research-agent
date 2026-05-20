from datetime import datetime
from pathlib import Path
import re


class ReportGenerator:
    def __init__(self, output_dir="reports"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def save_report(self, topic, content):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        slug = re.sub(r"[^A-Za-z0-9_-]+", "_", topic).strip("_") or "report"
        path = self.output_dir / f"{slug}_{timestamp}.md"

        path.write_text(content, encoding="utf-8")
        return str(path)
