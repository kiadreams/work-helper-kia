from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.database.db_manager import DatabaseManager
    from src.domain.models import Employee


class EmployeeRepository:
    def __init__(self, db_manager: DatabaseManager) -> None:
        self.db_manager = db_manager

    def add_employee(self, employee: Employee) -> None:
        with self.db_manager.get_session() as session:
            session.add(employee)
            session.commit()
