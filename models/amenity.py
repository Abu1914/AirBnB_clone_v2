#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import relationship
from models.place import place_amenity
from os import getenv


class Amenity(BaseModel):
    """Represents an Amenity for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table amenties.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Amenities.
        name (sqlalchemy String): The amenity name.
        place_amenties (sqlalchemyrelationship): place-Amenity relationship.
    """
    __tablename__ = "amenities"
    if getevn("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("place", secondary=place_amenity,
                                       viewonly=False)
