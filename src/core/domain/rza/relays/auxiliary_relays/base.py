from typing import TYPE_CHECKING

from src.core.domain.rza.relays.relay_model import Relay
from src.core.domain.rza.enums import ValueQuality
from src.core.domain.rza.measure_value import MeasuredValue

if TYPE_CHECKING:
    from .enums import AuxiliaryRelayType


class AuxiliaryRelay(Relay):
    def __init__(
        self,
        relay_type: AuxiliaryRelayType,
        schematic_designation: str | None = None,
        relay_id: int | None = None,
        is_output: bool = False,
    ) -> None:
        super().__init__(
            relay_type=relay_type, schematic_designation=schematic_designation, relay_id=relay_id
        )
        self.is_output = is_output
        self._pickup_time: MeasuredValue | None = None
        self._dropout_time: MeasuredValue | None = None

    @property
    def pickup_time(self) -> MeasuredValue | None:
        return self._pickup_time

    @pickup_time.setter
    def pickup_time(self, value: float) -> None:
        self._pickup_time = MeasuredValue(value=value, quality=ValueQuality.REAL)

    @property
    def dropout_time(self) -> MeasuredValue | None:
        return self._dropout_time

    @dropout_time.setter
    def dropout_time(self, value: float) -> None:
        self._dropout_time = MeasuredValue(value=value, quality=ValueQuality.REAL)
