#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
<<<<<<< HEAD
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
=======
>>>>>>> e672fa4cd2dd75e2bb982d1b2215e1758d0ccb56


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
<<<<<<< HEAD
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        if cls is None:
            return self.__objects
        else:
            new_dict = {}
            if len(self.__objects) > 0:
                for key, value in self.__objects.items():
                    if type(cls) is str:
                        if cls == key.split('.')[0]:
                            new_dict[key] = value
                    else:
                        if cls is type(value):
                            new_dict[key] = value
            return new_dict

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objecs if its inside
        Not sure if it should also delete from json file
        """

        dict_key = ""
        for key, value in self.__objects.items():
            if obj == value:
                dict_key = key
        if dict_key is not "":
            del self.__objects[dict_key]

    def close(self):
        """ calls reload() for deserializing the JSON file to objects."""
=======
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            fs_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    fs_dict[key] = value
            return fs_dict
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """delete obj from __objects"""
        if (obj is None):
            return
        if (obj):
            del(obj)
        # if (obj is None):
        #     return

        # key = obj.__class__.__name__ + '.' + obj.id

        # try:
        #     del(self.all()[key])
        #     self.save()
        # except KeyError:
        #     print("** no instance found **")

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

    def close(self):
        """ close method """
>>>>>>> e672fa4cd2dd75e2bb982d1b2215e1758d0ccb56
        self.reload()
