from typing import NamedTuple

from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, RGBColor


class TextStyle(NamedTuple):
    text_align: WD_ALIGN_PARAGRAPH = WD_ALIGN_PARAGRAPH.LEFT
    font_name: str = "Times New Roman"
    font_size: Pt = Pt(12)
    is_bold: bool = False
    is_italic: bool = False
    is_underline: bool = False
    font_color: RGBColor = RGBColor(0, 0, 0)


class ParagraphStyle(NamedTuple):
    space_before: Pt = Pt(0)
    space_after: Pt = Pt(0)


class CellStyle(NamedTuple):
    vertical_alignment: WD_CELL_VERTICAL_ALIGNMENT = WD_CELL_VERTICAL_ALIGNMENT.CENTER
