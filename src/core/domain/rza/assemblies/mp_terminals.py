from typing import TYPE_CHECKING
from src.core.domain.rza.assemblies import ProtectionAssembly

if TYPE_CHECKING:
    from src.core.domain.rza.enums import MpTerminalType


class MpTerminal(ProtectionAssembly):
    def __init__(
        self,
        terminal_type: MpTerminalType,
        terminal_id: int | None = None,
        schematic_designation: str | None = None,
        serial_number: str | None = None,
    ) -> None:
        super().__init__(
            assembly_type=terminal_type,
            assembly_id=terminal_id,
            schematic_designation=schematic_designation,
            serial_number=serial_number,
        )
