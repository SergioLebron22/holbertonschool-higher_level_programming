#!/usr/bin/python3

"""
This module defines the City class,
which represents cities of a state in the database.
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """
    Represents a state in the database.

    Attributes:
        id (int): The unique identifier of the state.
        name (str): The name of the state.
    """
    __tablename__ = 'cities'

    id = Column('id', Integer, unique=True,
                autoincrement=True, nullable=False, primary_key=True)
    name = Column('name', String(128), nullable=False)

    state_id = Column('state_id', Integer, ForeignKey('states.id'), nullable=False)
