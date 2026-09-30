from dataclasses import dataclass, field
from typing import TYPE_CHECKING

import flet as ft

if TYPE_CHECKING:
    pass


@ft.observable
@dataclass
class CompanyViewModel:
    name: str
    full_name: str | None = field(default=None)
    id: int | None = field(default=None)

    def update(self, name: str, full_name: str) -> None:
        self.name = name
        self.full_name = full_name


@ft.observable
@dataclass
class MainMenuViewModel:
    companies: list[CompanyViewModel] = field(default_factory=list)
    selected_company: CompanyViewModel | None = field(default=None)

    def __post_init__(self) -> None:
        self.companies.append(CompanyViewModel(id=1, name="Кубанское ПМЭС"))
        self.companies.append(CompanyViewModel(id=2, name="Ростовское ПМЭС"))
        self.selected_company = self.companies[0] if self.companies else None

    def add_company(self, name: str, full_name: str | None = None) -> None:
        self.companies.append(CompanyViewModel(name, full_name))

    def delete_company(self, company: CompanyViewModel) -> None:
        self.companies.remove(company)
