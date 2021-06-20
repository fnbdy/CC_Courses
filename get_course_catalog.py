from datetime import datetime

from colorama import Fore, Style
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from sqlalchemy import engine
from sqlalchemy.orm import Session, sessionmaker

from course_parser.items import Course, Department
import models
from course_parser.spiders import deanza_spider
from sqlalchemy.dialects.postgresql import insert

CONNECTION_STRING = 'postgresql://postgres:ppgres@192.168.0.202:5432/de_anza'


# list to collect all items
items = []


# pipeline to fill the items list
class ItemCollectorPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = models.db_connect()
        models.create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        if isinstance(item, Department):
            session = self.Session()
            dept = models.Department()

            dept.name = item.get('name', '')
            dept.code = item.get('code', '')
            dept.id = item.get('id', '')
            dept.loc = item.get('loc', '')
            dept.phone = item.get('phone', '')
            dept.home_page = item.get('home_page', '')
            dept.last_updated = datetime.now()

            session.merge(dept)
            session.commit()
            session.close()
        elif isinstance(item, Course):
            items.append(item)
        else:
            return item


def process_items(items):
    for item in items:
        if isinstance(item, Course):
            course = models.Course()

            course.id = item.get('id', '')
            course.name = item.get('name', '')
            course.description = item.get('description', '')
            course.units = item.get('units', '')
            course.hours = item.get('hours', '')
            course.total_hours = item.get('total_hours', '')
            course.GE = item.get('GE', '')
            course.program_applicable = item.get('program_applicable', '')
            course.credit_degree_applicable = item.get(
                'credit_degree_applicable', '')
            course.grading_method = item.get('grading_method', '')
            course.prereqs = item.get('prereqs', '')
            course.advisory = item.get('advisory', '')
            course.notes = item.get('notes', '')
            course.coreqs = item.get('coreqs', '')
            course.details_page = item.get('details_page', '')
            course.outline_page = item.get('outline_page', '')
            course.last_updated = datetime.now()

            print(course)

            dept_code = item.get('dept_code', '')

            dept = session.query(models.Department).filter(
                models.Department.code == dept_code).one()

            if not session.query(models.Course.id).filter(models.Course.id == course.id).one_or_none():
                dept.courses.append(course)

            session.commit()
    session.close()


settings = dict(get_project_settings())
settings.update({
    'ITEM_PIPELINES': {
        '__main__.ItemCollectorPipeline': 100
    },
    'LOG_LEVEL': 'INFO'
})
process = CrawlerProcess(settings=settings)

engine = models.db_connect()
session = Session(bind=engine)

process.crawl(deanza_spider.CourseCatalogSpider)
process.start()  # the script will block here until the crawling is finished
process_items(items)
