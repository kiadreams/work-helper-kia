import pytest

from src.core.domain.rza.enums import CurrentRelayType, TimeRelayType
from src.core.domain.rza.ralays import CurrentRelay, TimeRelay


def test_current_relay() -> None:
    relay = CurrentRelay(CurrentRelayType.RELAY_CR_ANY)
    relay.schematic_designation = "Реле перегруза"

    with pytest.raises(ValueError, match="Не указан величина срабатывания реле"):
        relay.calculate_reset_ratio()

    relay.pickup_setting = 1.5

    with pytest.raises(ValueError, match="Не указана величина возврата реле"):
        relay.calculate_reset_ratio()

    relay.reset_setting = 0.75

    relay.calculate_reset_ratio()
    assert relay.relay_type.value == "РТ", "The relay type is not correct"
    assert relay.reset_ratio == 0.5, "The reset ratio should be 0.5"

    assert relay.pickup_time_delay is None, "The property return incorrect value"
    relay.pickup_time_delays.append(5)
    relay.pickup_time_delays.append(3)
    relay.calculate_pickup_time_delay()
    assert relay.pickup_time_delay == 4.0, "The property return incorrect value"
    assert len(relay.pickup_time_delays) == 0, "The pickup_time_dalay list is not empty"

    assert relay.reset_time_delay is None, "The property return incorrect value"
    relay.reset_time_delays.append(5)
    relay.reset_time_delays.append(3)
    relay.calculate_reset_time_delay()
    assert relay.reset_time_delay == 4.0, "The property return incorrect value"
    assert len(relay.reset_time_delays) == 0, "The reset_time_dalay list is not empty"


def test_time_relay() -> None:
    relay = TimeRelay(TimeRelayType.RELAY_TR_ANY)
    assert relay.passing_contact_time_delay is None, "The property return incorrect value"
    relay.passing_contact_time_delays.append(5)
    relay.passing_contact_time_delays.append(3)
    relay.calculate_passing_contact_time_delay()
    assert relay.passing_contact_time_delay == 4.0, "The property return incorrect value"
    assert len(relay.passing_contact_time_delays) == 0, (
        "The passing_contact_time_delays list is not empty"
    )
