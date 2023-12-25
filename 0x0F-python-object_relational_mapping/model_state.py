#!/usr/bin/python3
"""State"""

from sqlalchemy import Column, Integer, String,
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class State(Base):
    """Introduce state"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)