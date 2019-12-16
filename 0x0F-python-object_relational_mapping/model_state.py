#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """The State class"""
    __tablename__ = 'states'
    id = Column(Integer,
                nullable=False,
                primary_key=True,
                unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
