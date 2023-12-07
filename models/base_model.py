#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
	"""
        Base class for all other sub classes.
        Defines all common attributes and methods for subclasses
    """
    
	def __init__(self, *args, **kwargs):
    	""" initializes self """
     
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now
		self.updated_at = datetime.now
    
    def __str__(self):
        """A string reprensentation of instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.now()
        
    def to_dict(self):
          """instance that returns a dictionary containing all keys/values"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict