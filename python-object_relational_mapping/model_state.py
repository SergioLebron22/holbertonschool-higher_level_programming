#!/usr/bin/python3

"""
This module defines the State class,
which represents a state in the database.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    """
    Represents a state in the database.

    Attributes:
        id (int): The unique identifier of the state.
        name (str): The name of the state.
    """
    __tablename__ = 'states'

    id = Column('id', Integer, unique=True, autoincrement=True, nullable=False, primary_key=True)
    name = Column('name', String(128), nullable=False)
