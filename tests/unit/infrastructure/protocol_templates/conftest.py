import pytest


@pytest.fixture
def mock_headline_data() -> dict[str, str]:
    return {
        "accession": "ВЛ 330 кВ Ст.ГРЭС - Армавир",
        "substation": "ПС 330 кВ Кропоткин",
        "enterprise_name": "Кубанское ПМЭС",
        "group_of_substation": "Северо - Восточная группа ПС",
        "device_type_and_number": "шкаф №35",
        "creation_date": '"23" февраля 2026 г.',
    }
