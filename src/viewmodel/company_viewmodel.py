from __future__ import annotations

from dataclasses import dataclass, field
from select import select
from typing import TYPE_CHECKING

import flet as ft

if TYPE_CHECKING:
    pass


@ft.observable
@dataclass
class CompanyState:
    name: str
    full_name: str | None = field(default=None)
    id: int | None = field(default=None)

    def update(self, name: str, full_name: str) -> None:
        self.name = name
        self.full_name = full_name


@ft.observable
@dataclass
class CompanyListViewModel:
    companies: list[CompanyState] = field(default_factory=list)
    selected_company: CompanyState | None = field(default=None)

    def __post_init__(self) -> None:
        self.companies.append(CompanyState(id=1, name="Кубанское ПМЭС"))
        self.companies.append(CompanyState(id=2, name="Ростовское ПМЭС"))
        self.selected_company = self.companies[0] if self.companies else None

    def add_company(self, name: str, full_name: str | None = None) -> None:
        self.companies.append(CompanyState(name, full_name))

    def delete_company(self, company: CompanyState) -> None:
        self.companies.remove(company)
