from dataclasses import dataclass

@dataclass(frozen=True)
class EmployeeUIEntity:
    id: int
    full_name: str
    position: str
    photo_path: str | None = None