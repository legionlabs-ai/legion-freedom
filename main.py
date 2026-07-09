from datetime import datetime
from pathlib import Path

from legion_freedom.agents.research.research_director import generate_daily_report

print("=" * 60)
print("LEGION FREEDOM")
print("Employee #001: Research Director")
print("=" * 60)

report = generate_daily_report()

today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_dir = Path("outputs/research_reports")
output_dir.mkdir(parents=True, exist_ok=True)

file_path = output_dir / f"research_briefing_{today}.md"

file_path.write_text(report)

print(report)
print("\nReport saved to:")
print(file_path)