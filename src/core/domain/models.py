from __future__ import annotations

from sqlmodel import Field, SQLModel


class CompanyDomain(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    full_name: str | None = Field(default=None)


class EmployeeDomain(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    last_name: str
