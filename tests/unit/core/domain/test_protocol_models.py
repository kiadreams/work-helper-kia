import pytest

from src.core.domain.protocol_domain.enums import CurrentRelayType, TimeRelayType
from src.core.domain.protocol_domain.ralays import CurrentRelay, TimeRelay


def test_current_relay() -> None:
    relay = CurrentRelay(CurrentRelayType.RELAY_CR_ANY)
    relay.schematic_designation = "Реле перегруза"

    with pytest.raises(ValueError, match="Не указан величина срабатывания реле"):
        _ = relay.current_reset_ratio

    relay.pickup_current = 1.5

    with pytest.raises(ValueError, match="Не указана величина возврата реле"):
        _ = relay.current_reset_ratio

    relay.reset_current = 0.75

    assert relay.relay_type.value == "РТ", "The relay type is not correct"
    assert relay.current_reset_ratio == 0.5

    assert relay.pickup_time_delay == -1, "The property return incorrect value"
    relay.pickup_time_delay = 5
    relay.pickup_time_delay = 3
    assert relay.pickup_time_delay == 4.0, "The property return incorrect value"
    relay.clean_pickup_time_delay()
    assert relay.pickup_time_delay == -1, "The property return incorrect value"

    assert relay.reset_time_delay == -1, "The property return incorrect value"
    relay.reset_time_delay = 5
    relay.reset_time_delay = 3
    assert relay.reset_time_delay == 4.0, "The property return incorrect value"
    relay.clean_reset_time_delay()
    assert relay.reset_time_delay == -1, "The property return incorrect value"


def test_time_relay() -> None:
    relay = TimeRelay(TimeRelayType.RELAY_TR_ANY)
    assert relay.passing_contact_time_delay == -1, "The property return incorrect value"
    relay.passing_contact_time_delay = 5
    relay.passing_contact_time_delay = 3
    assert relay.passing_contact_time_delay == 4.0, "The property return incorrect value"
    relay.clean_passing_contact_time_delay()
    assert relay.passing_contact_time_delay == -1, "The property return incorrect value"
