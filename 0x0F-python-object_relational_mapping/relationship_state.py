#!/usr/bin/python3
"""
Module for the state table class
This is ORM
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    Represents a state for a MySQL database
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(126), nullable=False)
    cities = relationship(
            'City', back_populates='state', cascade='all, delete'
            )
