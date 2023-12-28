#!/usr/bin/python3
"""Model State"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer

Base = declarative_base()


class State(Base):
    """Class representing the states table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
