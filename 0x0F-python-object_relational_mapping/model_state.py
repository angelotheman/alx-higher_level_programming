#!/usr/bin/python3
"""
Module for the state table class
This is ORM
"""
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    Class for the table 'State'
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(126), nullable=False)
