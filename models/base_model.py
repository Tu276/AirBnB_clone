<<<<<<< HEAD
#!/usr/bin/python3
"""
Module  class: BaseModel.
"""
import uuid
from datetime import datetime
import models

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    Superclass for all subsequent classes of
    the AirBnB clone project
    """

    def __init__(self, *args, **kwargs):
        """
        Obj Initialization
        """
        if kwargs:
            for key in kwargs:
                if "created_at" in kwargs:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        time)
                if "updated_at" in kwargs:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        time)
                if key != ('__class__'):
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        models.storage.new(self)

    def __str__(self):
        """
        String representation for printing.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates 'updated_at' with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary of all keys/values of the object.
        """
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = self.created_at.isoformat()
        if "updated_at" in new_dict:
            new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
=======
#!/user/bin/python3

import uuid
from datetime import datetime

class BaseModel:

    def __init__(self, *args, **kwargs):
        
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key ["__class__"]:
                    continue;
            if key == "updated_at" or key == "created_at":
                self.__dict__[key] = datetime.fromisoformat(value);
                    else:
                        self.__dict__[key] = value;
    else:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
>>>>>>> master
