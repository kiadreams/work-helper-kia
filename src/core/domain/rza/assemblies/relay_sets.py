from typing import TYPE_CHECKING

from src.core.domain.rza.assemblies import ProtectionAssembly

if TYPE_CHECKING:
    from src.core.domain.rza.relays import Relay
    from src.core.domain.rza.enums import RelaySetType


class RelaySet(ProtectionAssembly):
    def __init__(self, set_type: RelaySetType, set_id: int | None = None):
        super().__init__(assembly_type=set_type, assembly_id=set_id)
        self.relays: list[Relay] = []
