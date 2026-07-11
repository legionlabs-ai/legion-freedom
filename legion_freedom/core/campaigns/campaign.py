from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
import json


@dataclass
class Campaign:
    campaign_id: str
    product_name: str
    affiliate_program: str
    affiliate_link: str
    commission_rate: str
    target_audience: str
    platforms: list[str]

    status: str = "Research"
    owner: str = "Research Director"
    research_summary: str = ""
    content_package: str = ""
    notes: list[dict[str, str]] = field(default_factory=list)

    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )
    updated_at: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )

    def add_note(self, employee: str, note: str) -> None:
        self.notes.append(
            {
                "employee": employee,
                "note": note,
                "timestamp": datetime.now().isoformat(timespec="seconds"),
            }
        )
        self._touch()

    def assign_to(self, employee: str) -> None:
        self.owner = employee
        self._touch()

    def update_status(self, status: str) -> None:
        self.status = status
        self._touch()

    def _touch(self) -> None:
        self.updated_at = datetime.now().isoformat(timespec="seconds")

    def to_dict(self) -> dict:
        return asdict(self)

    def save_json(self, output_directory: str = "outputs/campaigns") -> Path:
        output_dir = Path(output_directory)
        output_dir.mkdir(parents=True, exist_ok=True)

        output_path = output_dir / f"{self.campaign_id}.json"
        output_path.write_text(
            json.dumps(self.to_dict(), indent=2),
            encoding="utf-8",
        )

        return output_path