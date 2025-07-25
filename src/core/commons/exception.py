from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class ApplicationException(Exception):
    @property
    def message(self) -> str:
        return "Ошибка при работе с приложением!"
