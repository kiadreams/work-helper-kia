import pytest

from core.domain.rza.relays.auxiliary_relays import AuxiliaryRelayType
from core.domain.rza.relays.auxiliary_relays import RelayAr23, RelayAr220


class TestRelayAr23:
    @pytest.fixture
    def ar_23(self) -> RelayAr23:
        return RelayAr23()

    def test_check_creating_relay(self, ar_23: RelayAr23):
        assert isinstance(ar_23, RelayAr23), "Type of AR 23 relay should be RelayAr23"

    def test_check_default_output_field(self, ar_23: RelayAr23):
        assert not ar_23.is_output, "Default output field should be False"

    def test_check_default_relay_type_field(self, ar_23: RelayAr23):
        assert (
            ar_23.relay_type == AuxiliaryRelayType.RELAY_AR_23
        ), f"Relay type of ar_23 should be {AuxiliaryRelayType.RELAY_AR_23}"


class TestRelayAr220:
    @pytest.fixture
    def ar_220(self) -> RelayAr220:
        return RelayAr220()

    def test_check_creating_relay(self, ar_220: RelayAr220):
        assert isinstance(ar_220, RelayAr220), "Type of AR 23 relay should be RelayAr23"

    def test_check_default_output_field(self, ar_220: RelayAr220):
        assert not ar_220.is_output, "Default output field should be False"

    def test_check_default_relay_type_field(self, ar_220: RelayAr220):
        assert (
            ar_220.relay_type == AuxiliaryRelayType.RELAY_AR_220
        ), f"Relay type of ar_23 should be {AuxiliaryRelayType.RELAY_AR_220}"
