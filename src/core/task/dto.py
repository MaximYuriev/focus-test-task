from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class CreateTaskDTO:
    title: str
    description: str | None
    status: str


@dataclass(frozen=True, eq=False)
class UpdateTaskDTO:
    title: str | None
    description: str | None
    status: str | None
