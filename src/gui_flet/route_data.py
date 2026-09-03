from __future__ import annotations

from enum import StrEnum


class AppRoute(StrEnum):
    MAIN_WINDOW = "/"
    EMPLOYEE_VIEW = "/employee_view"
    REPORT_VIEW = "/report_view"
    PROTOCOL_VIEW = "/protocol_view"
