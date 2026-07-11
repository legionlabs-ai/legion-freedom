from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
import json


@dataclass
class Product:
    product_id: str
    product_name: str
    category: str
    affiliate_program: str
    affiliate_link: str
    commission_rate: str
    target_audience: str
    price: str

    demand_score: int
    competition_score: int
    commission_score: int
    video_potential_score: int
    evergreen_score: int
    seasonality_score: int
    scalability_score: int

    opportunity_reason: str
    verification_needed: list[str]

    status: str = "Research"
    owner: str = "Research Director"
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

    def total_score(self) -> int:
        return (
            self.demand_score
            + self.competition_score
            + self.commission_score
            + self.video_potential_score
            + self.evergreen_score
            + self.seasonality_score
            + self.scalability_score
        )

    def average_score(self) -> float:
        return round(self.total_score() / 7, 2)

    def recommendation(self) -> str:
        score = self.average_score()

        if score >= 8.5:
            return "APPROVED"
        if score >= 7:
            return "REVIEW"
        return "REJECTED"

    def _touch(self) -> None:
        self.updated_at = datetime.now().isoformat(timespec="seconds")

    def to_dict(self) -> dict:
        data = asdict(self)
        data["total_score"] = self.total_score()
        data["average_score"] = self.average_score()
        data["recommendation"] = self.recommendation()
        return data

    def save_json(self, output_directory: str = "outputs/products") -> Path:
        output_dir = Path(output_directory)
        output_dir.mkdir(parents=True, exist_ok=True)

        output_path = output_dir / f"{self.product_id}.json"
        output_path.write_text(
            json.dumps(self.to_dict(), indent=2),
            encoding="utf-8",
        )

        return output_path