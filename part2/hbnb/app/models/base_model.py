#!/usr/bin/python3
"""BaseModel module."""

import uuid
from datetime import datetime

class BaseModel:
    """
    Base class for all entities.
    
    """

    def __init__(self):
        
        self.id = str(uuid.uuid4())
        now = datetime.utcnow()
        self.created_at = now
        self.updated_at = now

    def save(self):
        
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        
        data = self.__dict__.copy()

        for key in ("created_at", "updated_at"):
            if key in data and hasattr(data[key], "isoformat"):
                data[key] = data[key].isoformat()

        data["__class__"] = self.__class__.__name__
        return data
