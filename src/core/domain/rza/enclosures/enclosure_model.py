from typing import TYPE_CHECKING

from src.core.domain.rza.base_rza_models import RzaDevice


if TYPE_CHECKING:
    from src.core.domain.rza.enums import EnclosureType
    from src.core.domain.rza.assemblies import ProtectionAssembly
    from src.core.domain.rza.relays import Relay


class Enclosure(RzaDevice):
    def __init__(
        self,
        enclosure_type: EnclosureType,
        operational_designation: str | None = None,
        serial_number: str | None = None,
        inventory_number: str | None = None,
        enclosure_id: int | None = None,
    ) -> None:
        super().__init__(enclosure_id)
        self.enclosure_type = enclosure_type
        self.operational_designation = operational_designation
        self.serial_number = serial_number
        self.inventory_number = inventory_number
        self.assemblies: list[ProtectionAssembly] = []
        self.relays: list[Relay] = []
