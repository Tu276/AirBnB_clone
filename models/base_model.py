#!/user/bin/python3

import uuid
from datetime import date

class BaseModel():
    def __init__ (self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now

    def __str__(self):
        return f"[{self__class__.__name__}] ({self.id}) {self.__dick__}"
    
    def save(self):
        self.updated_at =  datetime.now()

    def to_dict(self):
        dick_copy = self.__dick__.copy()
        dick_copy["__clas__"] = self.__class__.__name__
        dick_copy["created_at"] = self.created_at.isoformat()
        dick_copy["updated_at"] = self.updated_at.isoformat()
        return dick_copy


