#!/usr/bin/python3
from app.models.base_model import BaseModel


class Amenity(BaseModel):


    def __init__(self, name):
        super().__init__()
        self.name = None
        self.places = []
        self.set_name(name, autosave=False)
        self.save()


    def set_name(self, name, autosave=True):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name is required and must be a non-empty string")
        name = name.strip()
        if len(name) > 50:
            raise ValueError("name must not exceed 50 characters")
        self.name = name
        if autosave:
            self.save()

    def update_amenity(self, data):
        if not isinstance(data, dict):
            raise ValueError("data must be a dict")
        if "name" in data:
            self.set_name(data["name"])
