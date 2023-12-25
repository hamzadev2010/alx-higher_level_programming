#!/usr/bin/python3
"""State"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mt = MetaData()
Base = declarative_base(mt=mt)

class State(Base):
    """Introduce state"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
