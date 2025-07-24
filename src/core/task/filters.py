from dataclasses import dataclass

from src.core.commons.filter import BaseFilter


@dataclass(frozen=True, eq=False)
class GetTaskListFilter(BaseFilter):
    status: str | None
