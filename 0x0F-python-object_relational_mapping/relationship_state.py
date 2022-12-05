#!/usr/bin/python3
"""
Class definition of a State and an instance Base = declarative_base()
You must use the module SQLAlchemy
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class for State
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='State', cascade='all, delete')
