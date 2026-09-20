from typing import TYPE_CHECKING

from src.core.domain.rza.base_rza_models import RzaDevice

if TYPE_CHECKING:
    from src.core.domain.rza.enums import AssemblyType
    from src.core.domain.rza.relays import Relay


class ProtectionAssembly(RzaDevice):
    def __init__(
        self,
        assembly_type: AssemblyType,
        schematic_designation: str | None = None,
        assembly_id: int | None = None,
        serial_number: str | None = None,
    ):
        super().__init__(device_id=assembly_id)
        self.assembly_type = assembly_type
        self.schematic_designation = schematic_designation
        self.serial_number = serial_number


class MpTerminal(ProtectionAssembly):
    def __init__(self, name: str, firmware: str, **kwargs):
        super().__init__(name, **kwargs)
        self.firmware = firmware
