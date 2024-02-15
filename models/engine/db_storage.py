#!/usr/bin/python3
<<<<<<< HEAD
"""Module to create a mysql engine"""

import os
from models.base_model import BaseModel, Base
from models.user import User
=======
""" New engine DBStorage """
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
>>>>>>> e672fa4cd2dd75e2bb982d1b2215e1758d0ccb56
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
<<<<<<< HEAD
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """This class creates the engine for a mysql database
    storage system"""

    all_classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}
=======
import os


classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}


class DBStorage:
    """ DBStorage Class """
>>>>>>> e672fa4cd2dd75e2bb982d1b2215e1758d0ccb56
    __engine = None
    __session = None

    def __init__(self):
<<<<<<< HEAD
        """Instatiate the engine and drop if test database"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            os.environ['HBNB_MYSQL_USER'],
            os.environ['HBNB_MYSQL_PWD'],
            os.environ['HBNB_MYSQL_HOST'],
            os.environ['HBNB_MYSQL_DB']), pool_pre_ping=True)
=======
        """ init method """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)

>>>>>>> e672fa4cd2dd75e2bb982d1b2215e1758d0ccb56
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
<<<<<<< HEAD
        """Query all objects for curent session based on class name"""
        obj_dict = {}
        cls = self.all_classes[cls]
        if cls is not None:
            objects = self.__session.query(cls).all()
        else:
            objects = self.__session.query(
                State, City, User, Amenity, Place, Review)
        for obj in objects:
            key = obj.__class__.__name__ + '.' + obj.id
            value = obj
            obj_dict[key] = value
        return obj_dict

    def new(self, obj):
        """Add object to current database session"""
        self.__session.add(obj)
        self.__session.flush()

    def save(self):
        """Commit changes to the current databases session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create tables and current database session"""
        Base.metadata.create_all(self.__engine)

=======
        """ all method """
        dict_objs = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dict_objs[key] = obj
        return (dict_objs)

    def new(self, obj):
        """ new method """
        self.__session.add(obj)

    def save(self):
        """ save method """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete method """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ reload method """
        Base.metadata.create_all(self.__engine)
>>>>>>> e672fa4cd2dd75e2bb982d1b2215e1758d0ccb56
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
<<<<<<< HEAD
        """ call close on private session. """
        self.__session.close()
=======
        """ close method """
        if self.__session:
            self.__session.close()
>>>>>>> e672fa4cd2dd75e2bb982d1b2215e1758d0ccb56
