from typing import Protocol


class HeadlineDataProtocol(Protocol):
    @property
    def title(self) -> str: ...
