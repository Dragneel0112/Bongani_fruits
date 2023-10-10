#!/usr/bin/python3
""" Fruits Class"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String


class Fruits(BaseModel, Base):
    """Representation of Fruits """
    if models.storage_t == "db":
        __tablename__ = 'fruits'
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        image_url = Column(String(128), nullable=False)
        qty = Column(String(128), nullable=False)
        price = Column(String(128), nullable=False)

    else:
        name = ""
        description = ""
        image_url = ""
        qty = ""
        price = ""

    def __init__(self, *args, **kwargs):
        """initializes Fruits"""
        super().__init__(*args, **kwargs)
