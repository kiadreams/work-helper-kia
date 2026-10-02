from typing import TYPE_CHECKING

from src.core.domain.rza.assemblies import ProtectionAssembly

if TYPE_CHECKING:
    from src.core.domain.rza.enums import RelaySetType
    from src.core.domain.rza.relays import Relay


class RelaySet(ProtectionAssembly):
    def __init__(
        self,
        set_type: RelaySetType,
        set_id: int | None = None,
        schematic_designation: str | None = None,
        serial_number: str | None = None,
    ) -> None:
        super().__init__(
            assembly_type=set_type,
            assembly_id=set_id,
            schematic_designation=schematic_designation,
            serial_number=serial_number,
        )
        self.relays: list[Relay] = []
