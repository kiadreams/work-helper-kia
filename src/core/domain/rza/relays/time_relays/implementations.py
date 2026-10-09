from core.domain.rza.relays.time_relays.base import TimeRelay
from core.domain.rza.relays.time_relays.enums import TimeRelayType
from core.domain.rza.types import VoltageInterval


class RelayTrEv114(TimeRelay):
    _default_pickup_setting = VoltageInterval(109, 119)
    _default_reset_setting = VoltageInterval(17, 27)

    def __init__(self) -> None:
        super().__init__(relay_type=TimeRelayType.RELAY_TR_EV_14)


class RelayTrEv122(TimeRelay):
    _default_pickup_setting = VoltageInterval(114, 127)
    _default_reset_setting = VoltageInterval(17, 25)

    def __init__(self) -> None:
        super().__init__(relay_type=TimeRelayType.RELAY_TR_EV_122)


class RelayTrEv132(TimeRelay):
    _default_pickup_setting = VoltageInterval(106, 117)
    _default_reset_setting = VoltageInterval(12, 21)

    def __init__(self) -> None:
        super().__init__(relay_type=TimeRelayType.RELAY_TR_EV_132)
