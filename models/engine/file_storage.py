#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place, 'State': State,
    'City': City, 'Amenity': Amenity, 'Review': Review
}


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
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        if cls is None:
            return self.__objects
        return {k: v for k, v in self.__objects.items()
                if type(val) == cls}

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        """if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj"""
        self.all().update({obj.to_dict()['__cls__'] + '.' + obj.id: obj})

    def save(self):
        """serialize the file path to JSON file path
        """
        with open(self.__file_path, 'w') as f:
            my_dict = {}
            my_dict.update(self.__objects)
            for key, value in my_dict.items():
                my_dict[key] = value.to_dict()
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            my_dict = {}
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                my_dict = json.load(f)
                for key, value in my_dict.items():
                    self.all()[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete an object from __objects if inside"""

        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()
