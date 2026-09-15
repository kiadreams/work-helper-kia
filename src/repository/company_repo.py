from __future__ import annotations

from typing import TYPE_CHECKING, Sequence

from sqlmodel import select

from src.core.domain import EmployeeDomain, CompanyDomain
from src.core.protocols import CompanyRepoProtocol

if TYPE_CHECKING:
    from src.database.db_manager import DatabaseManager


class CompanyRepository(CompanyRepoProtocol):
    def __init__(self, db_manager: DatabaseManager) -> None:
        self.db_manager = db_manager

    async def add_employee(self, employee: EmployeeDomain) -> None:
        async with self.db_manager.connection() as conn:
            conn.add(employee)
            await conn.commit()

    async def add_employees(self, employees: list[EmployeeDomain]) -> None:
        async with self.db_manager.connection() as conn:
            for employee in employees:
                conn.add(employee)
            await conn.commit()

    async def get_all_employees(self) -> Sequence[EmployeeDomain]:
        async with self.db_manager.connection() as conn:
            stm = select(EmployeeDomain)
            result = await conn.exec(stm)
            return result.all()

    async def add_company(self, company: CompanyDomain) -> None:
        async with self.db_manager.connection() as conn:
            conn.add(company)
            await conn.commit()

    async def add_companies(self, companies: list[CompanyDomain]) -> None:
        async with self.db_manager.connection() as conn:
            for company in companies:
                conn.add(company)
            await conn.commit()

    async def get_all_companies(self) -> Sequence[CompanyDomain]:
        async with self.db_manager.connection() as conn:
            stm = select(CompanyDomain)
            result = await conn.exec(stm)
            return result.all()
