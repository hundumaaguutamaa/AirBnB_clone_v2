#!/usr/bin/python3
""" A New Database Engine. """

from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage():
    """file storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializing values and linking the db. """
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, db))
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query to return a dict. """

        _classes = (Amenity, City, Place, Review, State, User)
        objects = dict()

        if cls is None:
            for item in _classes:
                query = self.__session.query(item)

                for obj in query.all():
                    obj_key = '{}.{}'.format(obj.__class__.name__, obj.id)
                    objects[obj_key] = obj
        else:
            query = self.__session.query(cls)
            for obj in query.all():
                obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects[obj_key] = obj

        return objects

    def new(self, obj):
        """ Add object to the current database session. """
        self.__session.add(obj)

    def save(self):
        """ Save/commit all the changes. """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes current database session. """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all the tables in database. """
        Base.metadata.create_all(self.__engine)

    def close(self):
        """ Closing the query. """
        self.__session.close()
