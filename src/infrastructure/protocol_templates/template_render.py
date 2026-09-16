from pathlib import Path
from docxtpl import DocxTemplate


def create_headline_template(
        template_path: Path,
        target_file_path: Path,
        template_data: dict[str, str] | None = None
) -> None:
    # data = {
    #     "accession": "ВЛ 330 кВ Ст.ГРЭС - Армавир",
    #     "substation": "ПС 330 кВ Кропоткин",
    #     "enterprise_name": "Кубанское ПМЭС",
    #     "group_of_substation": "Северо - Восточная группа ПС",
    #     "device_type_and_number": "шкаф №35",
    #     "creation_date": '"23" февраля 2026 г.',
    # }
    doc = DocxTemplate(template_path)
    if template_data:
        doc.render(template_data)
    doc.save(target_file_path)
