# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from datetime import datetime
from colorama.initialise import reset_all
from itemadapter import ItemAdapter
from requests.models import codes
from sqlalchemy.orm import sessionmaker

from course_parser.items import Course, Department
from colorama import Style, Fore

from . import models


class CoursePipeline:

    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = models.db_connect()
        models.create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        if isinstance(item, Course) or isinstance(item, Department):
            session = self.Session()

            if isinstance(item, Course):
                course = models.Course()

                course.id = item.get('id', '')
                course.name = item.get('name', '')
                # course.dept_code = item.get('dept_code', '')
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

                session.add(course)

            elif isinstance(item, Department):
                dept = models.Department()

                dept.name = item.get('name', '')
                dept.code = item.get('code', '')
                dept.id = item.get('id', '')
                dept.loc = item.get('loc', '')
                dept.phone = item.get('phone', '')
                dept.home_page = item.get('home_page', '')
                dept.last_updated = datetime.now()

                session.add(dept)

            session.commit()
            session.close()

        return item
