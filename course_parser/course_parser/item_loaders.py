from itemloaders.processors import (Compose, Identity, Join, MapCompose,
                                    TakeFirst)
from scrapy.loader import ItemLoader

from .utils import text_to_int


class CourseLoader(ItemLoader):
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()

    def is_GE(ge_text: str) -> bool:
        return ge_text == 'General Education Class'

    def is_program_applicable(program_applicable: str):
        return not program_applicable.startswith('Not')

    def is_credit_degree_applicable(credit_degree_applicable: str):
        return not credit_degree_applicable.startswith('Non')

    GE_in = MapCompose(default_input_processor, is_GE)
    program_applicable_in = MapCompose(
        default_input_processor, is_program_applicable)
    credit_degree_applicable_in = MapCompose(
        default_input_processor, is_credit_degree_applicable)
    hours_in = MapCompose(default_input_processor, text_to_int)

    notes_out = Identity()


class DepartmentLoader(ItemLoader):

    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()
