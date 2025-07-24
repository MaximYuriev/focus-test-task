from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class CreateTaskDTO:
    title: str
    description: str | None
    status: str
