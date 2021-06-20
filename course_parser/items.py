# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CourseParserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Course(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    dept_code = scrapy.Field()
    description = scrapy.Field()
    units = scrapy.Field()
    hours = scrapy.Field()
    total_hours = scrapy.Field()
    GE = scrapy.Field()
    program_applicable = scrapy.Field()
    credit_degree_applicable = scrapy.Field()
    grading_method = scrapy.Field()
    prereqs = scrapy.Field()
    advisory = scrapy.Field()
    notes = scrapy.Field()
    coreqs = scrapy.Field()
    details_page = scrapy.Field()
    outline_page = scrapy.Field()


class Department(scrapy.Item):
    name = scrapy.Field()
    code = scrapy.Field()
    id = scrapy.Field()
    loc = scrapy.Field()
    phone = scrapy.Field()
    home_page = scrapy.Field()
