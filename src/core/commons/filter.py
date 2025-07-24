from abc import ABC
from dataclasses import dataclass, asdict
from typing import Any


@dataclass(frozen=True, eq=False)
class BaseFilter(ABC):
    def to_dict(self) -> dict[str, Any]:
        """
        Возвращает словарь содержащий параметры фильтрации без null значений.
        """

        filter_dict = asdict(self)
        filter_dict_without_none = {}

        for key, value in filter_dict.items():
            if value is not None:
                filter_dict_without_none[key] = value

        return filter_dict_without_none
