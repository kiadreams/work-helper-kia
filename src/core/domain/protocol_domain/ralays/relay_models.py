from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.domain.protocol_domain.enums import PCRelay


class Relay:
    def __init__(
        self,
        relay_type: PCRelay,
        schematic_designation: str | None = None,
    ) -> None:
        self.id: int | None = None
        self.is_tested = False
        self.schematic_designation = schematic_designation
        self.relay_type = relay_type
        self._pickup_setting: float = -1
        self._reset_setting: float = -1
        self._pickup_time_delay: list[float ] = list()
        self._reset_time_delay: list[float] = list()

    @property
    def pickup_time_delay(self) -> float:
        if self._pickup_time_delay:
            return sum(self._pickup_time_delay) / len(self._pickup_time_delay)
        return -1

    @pickup_time_delay.setter
    def pickup_time_delay(self, value: float) -> None:
        self._pickup_time_delay.append(value)

    def clean_pickup_time_delay(self) -> None:
        self._pickup_time_delay.clear()

    @property
    def reset_time_delay(self) -> float:
        if self._reset_time_delay:
            return sum(self._reset_time_delay) / len(self._reset_time_delay)
        return -1

    @reset_time_delay.setter
    def reset_time_delay(self, value: float) -> None:
        self._reset_time_delay.append(value)

    def clean_reset_time_delay(self) -> None:
        self._reset_time_delay.clear()

    @property
    def _reset_ratio(self) -> float:
        if self._pickup_setting == -1:
            raise ValueError("Не указан величина срабатывания реле")
        if self._reset_setting == -1:
            raise ValueError("Не указана величина возврата реле")
        return self._reset_setting / self._pickup_setting
