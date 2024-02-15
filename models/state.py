<<<<<<< HEAD
s is the state class"""
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
        cities = relationship between state and city tables.
    """

    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            'City', back_populates='state',
            cascade='all, delete, delete-orphan')

    else:
        name = ""

        @property
        def cities(self):
            """returns list of Cities and some relationships"""
            cities_instances = []
            cities_dict = models.storage.all(models.City)
            for key, value in cities_dict.items():
                if self.id == value.state_id:
                    cities_instances.append(value)
            return cities_instances
=======
#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref="state")

    if os.getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """ cities getter attribute """
            cit_lis = []
            all_cit = models.storage.all(City)
            for city in all_cit.values():  # change .items() to values() as it
                # returns an obj that contains values of a dictionary as a list
                if city.state_id == self.id:
                    cit_lis.append(city)
            return cit_lis
>>>>>>> e672fa4cd2dd75e2bb982d1b2215e1758d0ccb56
