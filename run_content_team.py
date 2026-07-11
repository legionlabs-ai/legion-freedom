from datetime import datetime
from pathlib import Path

from legion_freedom.agents.content.executive_content_director import (
    create_content_package,
)
from legion_freedom.agents.research.research_director import (
    generate_daily_report,
)


def save_output(content: str) -> Path:
    output_dir = Path("outputs/content_packages")
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_path = output_dir / f"content_package_{timestamp}.md"

    output_path.write_text(content, encoding="utf-8")
    return output_path


print("=" * 60)
print("LEGION LABS — CONTENT TEAM")
print("=" * 60)

print("\nResearch Director is working...")
research_report = generate_daily_report()

print("Executive Content Director is working...")
content_package = create_content_package(research_report)

saved_path = save_output(content_package)

print("\n" + content_package)
print("\nContent package saved to:")
print(saved_path)