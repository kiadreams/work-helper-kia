from src.core.domain import CompanyDomain, EmployeeDomain


def test_company_dmn_model() -> None:
    company_domain = CompanyDomain(name="КПМЭС", full_name="Кубанское ПМЭС")

    assert company_domain.id is None, "The id field doesn't exist"
    assert company_domain.name == "КПМЭС", "The name field doesn't exist"
    assert company_domain.full_name == "Кубанское ПМЭС", "The full_name field doesn't exist"


def test_employee_dmn_model() -> None:
    employee_domain = EmployeeDomain(name="Igor", last_name="First")

    assert employee_domain.id is None, "The id field doesn't exist"
    assert employee_domain.name == "Igor", "The name field doesn't exist"
    assert employee_domain.last_name == "First", "The last_name field doesn't exist"
