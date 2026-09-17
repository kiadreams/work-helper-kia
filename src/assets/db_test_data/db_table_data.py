from src.core.domain import CompanyDomain, EmployeeDomain

test_companies = [CompanyDomain(name=f"Кубанское ПМЭС_${1}") for i in range(5)]

test_employees = [EmployeeDomain(name=f"Igor_${i}", last_name=f"First_${i}") for i in range(100)]
