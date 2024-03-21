#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from os import getevn
from sqlalchemy import Column, String, Foreignkey


class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), Foreignkey("places.id"), nullable=False)
    user_id = Column(String(60), Foreignkey("users.id"), nullable=False)
