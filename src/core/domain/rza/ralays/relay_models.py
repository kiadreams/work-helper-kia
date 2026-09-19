from typing import TYPE_CHECKING

from src.core.domain.rza.base_rza_models import RzaDevice
from src.core.domain.rza.enums import ValueQuality
from src.core.domain.rza.measure_value import MeasuredValue

if TYPE_CHECKING:
    from src.core.domain.rza.enums import RelayType


class Relay(RzaDevice):
    def __init__(
        self,
        relay_type: RelayType,
        relay_id: int | None = None,
        schematic_designation: str | None = None,
    ) -> None:
        super().__init__(relay_id)
        self.is_tested = False
        self.schematic_designation = schematic_designation
        self.relay_type = relay_type
        self._reset_ratio: MeasuredValue | None = None
        self._pickup_setting: MeasuredValue | None = None
        self._reset_setting: MeasuredValue | None = None
        self._pickup_time_delay: MeasuredValue | None = None
        self._reset_time_delay: MeasuredValue | None = None

        self.pickup_time_delays: list[float] = list()
        self.reset_time_delays: list[float] = list()

    @property
    def pickup_setting(self) -> MeasuredValue | None:
        return self._pickup_setting

    @pickup_setting.setter
    def pickup_setting(self, value: float) -> None:
        self._pickup_setting = MeasuredValue(value=value, quality=ValueQuality.REAL)

    @property
    def reset_setting(self) -> MeasuredValue | None:
        return self._reset_setting

    @reset_setting.setter
    def reset_setting(self, value: float) -> None:
        self._reset_setting = MeasuredValue(value=value, quality=ValueQuality.REAL)

    @property
    def pickup_time_delay(self) -> MeasuredValue | None:
        return self._pickup_time_delay

    def calculate_pickup_time_delay(self) -> None:
        if self.pickup_time_delays:
            self._pickup_time_delay = self._calculate_average_value(self.pickup_time_delays)
            self.pickup_time_delays.clear()

    @property
    def reset_time_delay(self) -> MeasuredValue | None:
        return self._reset_time_delay

    def calculate_reset_time_delay(self) -> None:
        if self.reset_time_delays:
            self._reset_time_delay = self._calculate_average_value(self.reset_time_delays)
            self.reset_time_delays.clear()

    @property
    def reset_ratio(self) -> MeasuredValue | None:
        return self._reset_ratio

    def calculate_reset_ratio(self) -> None:
        if self._pickup_setting is None:
            raise ValueError("Не указан величина срабатывания реле")
        if self._reset_setting is None:
            raise ValueError("Не указана величина возврата реле")
        self._reset_ratio = self._reset_setting / self._pickup_setting

    @staticmethod
    def _calculate_average_value(list_of_value: list[float]) -> MeasuredValue:
        average_value = sum(list_of_value) / len(list_of_value)
        return MeasuredValue(value=average_value, quality=ValueQuality.REAL)
