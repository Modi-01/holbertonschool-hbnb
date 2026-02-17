#!/usr/bin/python3
from app.models.base_model import BaseModel
from app.models.user import User
from app.models.amenity import Amenity


class Place(BaseModel):
    

    def __init__(self, name, owner, description="", price_per_night=0,
                 latitude=0.0, longitude=0.0):
        super().__init__()
        self.name = None
        self.description = ""
        self.price_per_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.owner = None

        
        self.review = []
        self.amenity = []

        self.set_name(name)
        self.set_owner(owner)
        self.set_description(description)
        self.set_price_per_night(price_per_night)
        self.set_latitude(latitude)
        self.set_longitude(longitude)


    def set_name(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name is required and must be a non-empty string")
        name = name.strip()
        if len(name) > 100:
            raise ValueError("name must not exceed 100 characters")
        self.name = name
        self.save()

    def set_description(self, description):
        if description is None:
            description = ""
        if not isinstance(description, str):
            raise ValueError("description must be a string")
        self.description = description
        self.save()

    def set_price_per_night(self, price_per_night):
        if not isinstance(price_per_night, int):
            raise ValueError("price_per_night must be an integer")
        if price_per_night < 0:
            raise ValueError("price_per_night must be >= 0")
        self.price_per_night = price_per_night
        self.save()

    def set_latitude(self, latitude):
        if not isinstance(latitude, (int, float)):
            raise ValueError("latitude must be a number")
        latitude = float(latitude)
        if latitude < -90.0 or latitude > 90.0:
            raise ValueError("latitude must be within -90.0 to 90.0")
        self.latitude = latitude
        self.save()

    def set_longitude(self, longitude):
        if not isinstance(longitude, (int, float)):
            raise ValueError("longitude must be a number")
        longitude = float(longitude)
        if longitude < -180.0 or longitude > 180.0:
            raise ValueError("longitude must be within -180.0 to 180.0")
        self.longitude = longitude
        self.save()

    def set_owner(self, owner):
        if not isinstance(owner, User):
            raise ValueError("owner must be a User instance")
        self.owner = owner
        self.save()


    def add_review(self, review_obj):
        """Add a Review to this Place (one-to-many)."""
        from app.models.review import Review 

        if not isinstance(review_obj, Review):
            raise ValueError("review must be a Review instance")

        
        if review_obj.place is not self:
            raise ValueError("review.place must reference this Place instance")

        self.review.append(review_obj)
        self.save()

    def add_amenity(self, amenity_obj):
        """Link an Amenity to this Place (many-to-many)."""
        if not isinstance(amenity_obj, Amenity):
            raise ValueError("amenity must be an Amenity instance")

        if amenity_obj not in self.amenity:
            self.amenity.append(amenity_obj)

        
        if self not in amenity_obj.places:
            amenity_obj.places.append(self)

        self.save()

    def remove_amenity(self, amenity_obj):
        """Unlink an Amenity from this Place."""
        if not isinstance(amenity_obj, Amenity):
            raise ValueError("amenity must be an Amenity instance")

        if amenity_obj in self.amenity:
            self.amenity.remove(amenity_obj)

        if self in amenity_obj.places:
            amenity_obj.places.remove(self)

        self.save()

    def update_place(self, data):
        """UML mentions update_place; model-level update helper."""
        if not isinstance(data, dict):
            raise ValueError("data must be a dict")

        if "name" in data:
            self.set_name(data["name"])
        if "description" in data:
            self.set_description(data["description"])
        if "price_per_night" in data:
            self.set_price_per_night(data["price_per_night"])
        if "latitude" in data:
            self.set_latitude(data["latitude"])
        if "longitude" in data:
            self.set_longitude(data["longitude"])
        if "owner" in data:
            self.set_owner(data["owner"])
