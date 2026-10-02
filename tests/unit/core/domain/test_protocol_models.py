import pytest

from src.core.domain.rza.measure_value import MeasuredValue
from src.core.domain.rza.enums import (
    AuxiliaryRelayType,
    CurrentRelayType,
    TimeRelayType,
    VoltageRelayType, RelayType,
)
from src.core.domain.rza.relays import (
    CurrentRelay,
    TimeRelay,
    AuxiliaryRelay,
    Relay,
    VoltageRelay,
)


def test_reset_ration_of_relay() -> None:
    relay = Relay(AuxiliaryRelayType.RELAY_AR_ANY)
    relay.schematic_designation = "Реле"

    assert relay.relay_type.value == "рп", "The relay type is not correct"

    with pytest.raises(ValueError, match="Не указан величина срабатывания реле"):
        relay._calculate_reset_ratio()
    relay.pickup_setting = 1.5
    with pytest.raises(ValueError, match="Не указана величина возврата реле"):
        relay._calculate_reset_ratio()
    relay.reset_setting = 0.75
    relay._calculate_reset_ratio()
    assert relay.reset_ratio == 0.5, "The reset ratio should be 0.5"


def test_pickup_time_delay_of_relay() -> None:
    relay = Relay(AuxiliaryRelayType.RELAY_AR_23)
    relay.schematic_designation = "Реле"

    assert relay.relay_type.value == "рп-23", "The relay type is not correct"

    assert relay.pickup_time_delay is None, "The property return incorrect value"
    relay.pickup_time_delays.append(5)
    relay.pickup_time_delays.append(3)
    relay.calculate_pickup_time_delay()
    assert relay.pickup_time_delay == 4.0, "The property return incorrect value"
    assert len(relay.pickup_time_delays) == 0, "The pickup_time_dalay list is not empty"


def test_auxiliary_relay() -> None:
    relay = AuxiliaryRelay(AuxiliaryRelayType.RELAY_AR_222)
    relay.schematic_designation = "Реле РП-222"

    assert relay.relay_type.value == "рп-222", "The relay type is not correct"


def test_reset_time_delay_of_relay() -> None:
    relay = Relay(AuxiliaryRelayType.RELAY_AR_ANY)
    relay.schematic_designation = "Реле"

    assert relay.reset_time_delay is None, "The property return incorrect value"
    relay.reset_time_delays.append(5)
    relay.reset_time_delays.append(3)
    relay.calculate_reset_time_delay()
    assert relay.reset_time_delay == 4.0, "The property return incorrect value"
    assert len(relay.reset_time_delays) == 0, "The reset_time_dalay list is not empty"


def test_current_relay() -> None:
    relay = CurrentRelay(CurrentRelayType.RELAY_CR_ANY)
    relay.schematic_designation = "Реле РТ"

    assert relay.relay_type.value == "рт", "The relay type is not correct"


def test_voltage_relay() -> None:
    relay = VoltageRelay(VoltageRelayType.RELAY_VR_ANY)
    relay.schematic_designation = "Реле РН"

    assert relay.relay_type.value == "рн", "The relay type is not correct"


def test_passing_contact_of_time_relay() -> None:
    relay = TimeRelay(TimeRelayType.RELAY_TR_ANY)
    assert relay.passing_contact_time_delay is None, "The property return incorrect value"

    assert relay.relay_type.value == "рв", "The relay type is not correct"

    relay.passing_contact_time_delays.append(5)
    relay.passing_contact_time_delays.append(3)
    relay.calculate_passing_contact_time_delay()
    assert relay.passing_contact_time_delay == 4.0, "The property return incorrect value"
    assert len(relay.passing_contact_time_delays) == 0, (
        "The passing_contact_time_delays list is not empty"
    )


def test_addition_of_measure_value() -> None:
    value_1 = MeasuredValue(100)
    value_2 = MeasuredValue(200)
    assert value_1 + value_2 == 300, "The value must be equal to 300"


def test_subtraction_of_measure_value() -> None:
    value_1 = MeasuredValue(100)
    value_2 = MeasuredValue(200)
    assert value_1 - value_2 == -100, "The result must be equal -100"


def test_division_of_measure_value() -> None:
    value_1 = MeasuredValue(5)
    value_2 = MeasuredValue(3)
    assert value_1 / value_2 == 5 / 3, "The result must be equal 5 / 3"


def test_multiplication_of_measure_value() -> None:
    value_1 = MeasuredValue(5)
    value_2 = MeasuredValue(3)
    assert value_1 * value_2 == 15, "The result must be equal 15"


def test_less_than_of_measure_value() -> None:
    value_1 = MeasuredValue(1.2777)
    value_2 = MeasuredValue(1.3)
    assert value_1 < value_2, "The value_1 must be less than value_2"


def test_greater_than_of_measure_value() -> None:
    value_1 = MeasuredValue(1.2777)
    value_2 = MeasuredValue(1.3)
    assert value_2 > value_1, "The value_2 must be greater than value_1"


def test_equals_two_values() -> None:
    value_1 = MeasuredValue(20002)
    value_2 = MeasuredValue(20000)
    assert value_1 == value_2, "The value_1 and value_2 must be equal"

def test_relative_difference_two_values() -> None:
    value_1 = MeasuredValue(20003)
    value_2 = MeasuredValue(20000)
    assert not value_1 == value_2, "The value_1 and value_2 must not be equal"