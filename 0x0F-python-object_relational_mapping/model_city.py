#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """The City class"""
    __tablename__ = 'cities'
    id = Column(Integer,
                nullable=False,
                primary_key=True,
                unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
                      ForeignKey("states.id"),
                      nullable=False)
