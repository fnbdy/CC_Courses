from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text)
from scrapy.utils.project import get_project_settings
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import ARRAY

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    Base.metadata.create_all(engine)


class Course(Base):
    __tablename__ = "course"

    id = Column(Text, primary_key=True, unique=True)
    name = Column(Text, nullable=False)
    dept_code = Column(ForeignKey('department.code'), nullable=False)
    description = Column(Text)
    units = Column(Float)
    hours = Column(Text)
    total_hours = Column(Text)
    GE = Column(Boolean)
    program_applicable = Column(Boolean)
    credit_degree_applicable = Column(Boolean)
    grading_method = Column(Text)
    prereqs = Column(Text)
    advisory = Column(Text)
    notes = Column(ARRAY(Text))
    coreqs = Column(Text)
    details_page = Column(Text)
    outline_page = Column(Text)
    last_updated = Column(DateTime)

    department = relationship('Department', back_populates='courses')


class Department(Base):
    __tablename__ = "department"

    code = Column(Text, primary_key=True)
    id = Column(Text)
    name = Column(Text, nullable=False)
    loc = Column(Text)
    phone = Column(Text)
    home_page = Column(Text)
    last_updated = Column(DateTime)

    courses = relationship(
        'Course', back_populates='department', order_by=Course.id)
