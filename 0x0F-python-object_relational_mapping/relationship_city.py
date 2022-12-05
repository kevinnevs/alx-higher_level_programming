#!/usr/bin/python3
"""
Class definition of a City and an instance Base = declarative_base()
You must use the module SQLAlchemy
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State


class City(Base):
    """
    Class for City
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
