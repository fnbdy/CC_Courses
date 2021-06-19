import re
from itemloaders.processors import MapCompose
from course_parser.items import Course, Department
from course_parser.item_loaders import CourseLoader, DepartmentLoader

from scrapy import Spider, item
from scrapy.http.response.html import HtmlResponse
from datetime import datetime


class AssistOrgSpider(Spider):
    name = "assist_org"
    start_urls = [
        'https://www.deanza.edu/catalog/courses/',
    ]
    query_url = 'https://www.deanza.edu/_resources/php/catalog/dept-course-list.php?dept='

    def parse(self, response: HtmlResponse, **kwargs):
        for dept_tag in response.xpath('//select[@id="ddlDepts"]/option[@value!=0]'):
            dept_ldr = DepartmentLoader(item=Department(), response=response)

            dept_ldr.add_value(
                'name', dept_tag.xpath('./text()').get(), re=r'(.*)\s\(.*\)')
            dept_ldr.add_value(
                'code', dept_tag.xpath('./text()').get(), re=r'.*\((.*)\)')
            dept_ldr.add_value(
                'id', dept_tag.xpath('./@value').get())

            dept = dept_ldr.load_item()
            dept_courses_page = f'{self.query_url}{dept["id"]}'

            yield response.follow(dept_courses_page, callback=self.get_course_catalogs, meta={'dept': dept})

    def get_course_catalogs(self, response: HtmlResponse, **kwargs):
        dept_ldr = DepartmentLoader(
            item=response.meta['dept'], response=response)
        dept_ldr.add_xpath(
            'loc', '//*[@class="callout-content"]//div[@class="row"]//p/text()[1]')
        dept_ldr.add_xpath(
            'phone', '//*[@class="callout-content"]//div[@class="row"]//p/text()[3]')
        dept_ldr.add_xpath(
            'home_page', '//a[text()="Visit Department Website"]/@href',
            MapCompose(CourseLoader.default_input_processor, response.urljoin))

        dept = dept_ldr.load_item()
        yield dept

        course_rows = response.xpath('//table/tbody/tr')
        for row in course_rows:
            columns = row.xpath('./td')
            course_details_url = columns[1].xpath('./a/@href').get()

            yield response.follow(course_details_url, callback=self.crawl_course_details, meta={'dept_code': dept['code']})

    def crawl_course_details(self, response: HtmlResponse, **kwargs):
        sections_xpath = '//*[@class="container"]/div/div[contains(@class, "col")]'
        descriptions_xpath = f'{sections_xpath}[h3[text()="Course Description"]]'
        details_xpath = f'{sections_xpath}[h3[text()="Course Details"]]/dl'
        prereqs_xpath = f'{sections_xpath}[h3[text()="Prerequisites"]]/dl'

        course_ldr = CourseLoader(item=Course(), response=response)
        course_ldr.add_value(
            'dept_code', response.meta['dept_code'])
        course_ldr.add_value(
            'details_page', response.url)

        description_ldr = course_ldr.nested_xpath(descriptions_xpath)
        description_ldr.add_xpath(
            'id', './/h2/small/text()')
        description_ldr.add_xpath(
            'name', './/h2/text()')
        description_ldr.add_xpath(
            'description', './/p[1]/text()')
        description_ldr.add_xpath(
            'outline_page', './/p[2]/a/@href',
            MapCompose(CourseLoader.default_input_processor, response.urljoin))

        details_ldr = course_ldr.nested_xpath(details_xpath)
        details_ldr.add_xpath(
            'units', 'dt[text()="Units"]/following-sibling::dd[1]/text()', re=r'\d+[.]?[\d]*')
        details_ldr.add_xpath(
            'hours', 'dt[text()="Hours"]/following-sibling::dd[1]/text()', re=r'(.*)\s\(.*\)')
        details_ldr.add_xpath(
            'total_hours', 'dt[text()="Hours"]/following-sibling::dd[1]/text()', re=r'.*\((.*)\)')
        details_ldr.add_xpath(
            'GE', 'dt[text()="Gen Ed"]/following-sibling::dd[1]/text()')
        details_ldr.add_xpath(
            'program_applicable', 'dt[text()="Program Status"]/following-sibling::dd[1]/text()')
        details_ldr.add_xpath(
            'credit_degree_applicable', 'dt[text()="Credit"]/following-sibling::dd[1]/text()')
        details_ldr.add_xpath(
            'grading_method', 'dt[text()="Grading Method"]/following-sibling::dd[1]/text()')

        prereqs_ldr = course_ldr.nested_xpath(prereqs_xpath)
        prereqs_ldr.add_xpath(
            'prereqs', 'dt[text()="Prerequisite"]/following-sibling::dd[1]/text()')
        prereqs_ldr.add_xpath(
            'advisory', 'dt[text()="Advisory"]/following-sibling::dd[1]/text()')
        prereqs_ldr.add_xpath(
            'coreqs', 'dt[text()="Corequisite"]/following-sibling::dd[1]/text()')
        prereqs_ldr.add_xpath(
            'notes', 'dt[text()="Note"]/following-sibling::dd[1]/text()')

        yield course_ldr.load_item()
