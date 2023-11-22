#!/usr/bin/python3
""" Module defines a class to manage file storage for hbnb clone. """

import json


class FileStorage:
    """a class that manages storage of hbnb models in JSON format. """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage
        Filtered by class if cls is specified
        """
        if cls is None:
            return FileStorage.__objects
        return {k: v for k, v in FileStorage.__objects.items() if isinstance(v, cls)}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = obj.to_dict()['__class__'] + '.' + obj.id
        self.all()[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj is not None:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            self.all().pop(key, None)
