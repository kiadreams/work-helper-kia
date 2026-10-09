from typing import TYPE_CHECKING

from core.domain.rza.base_rza_models import RzaDevice
from core.domain.rza.enums import ValueQuality
from core.domain.rza.measure_value import MeasuredValue

if TYPE_CHECKING:
    from core.domain.rza.enums import RelayType


class Relay(RzaDevice):
    def __init__(
        self,
        relay_type: RelayType,
        relay_id: int | None = None,
        schematic_designation: str | None = None,
    ) -> None:
        super().__init__(device_id=relay_id)
        self.is_tested = False
        self.schematic_designation = schematic_designation
        self.relay_type = relay_type
        self._reset_ratio: MeasuredValue | None = None
        self._pickup_setting: MeasuredValue | None = None
        self._reset_setting: MeasuredValue | None = None

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
    def reset_ratio(self) -> MeasuredValue:
        return self._calculate_reset_ratio()

    def _calculate_reset_ratio(self) -> MeasuredValue:
        if self._pickup_setting is None:
            raise ValueError("Не указан величина срабатывания реле")
        if self._reset_setting is None:
            raise ValueError("Не указана величина возврата реле")
        return self._reset_setting / self._pickup_setting

    @staticmethod
    def _calculate_average_value(list_of_value: list[float]) -> MeasuredValue:
        average_value = sum(list_of_value) / len(list_of_value)
        return MeasuredValue(value=average_value, quality=ValueQuality.REAL)
