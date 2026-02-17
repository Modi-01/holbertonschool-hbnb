#!/usr/bin/python3

from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.persistence.repository import InMemoryRepository


class HBnBFacade:

    def __init__(self):
        self.users = InMemoryRepository()
        self.places = InMemoryRepository()
        self.reviews = InMemoryRepository()
        self.amenities = InMemoryRepository()

    # -------- User Methods --------
    def create_user(self, email, password, first_name, last_name, is_admin=False):
        
        for u in self.users.list_all():
            if u.email == email.strip():
                raise ValueError("email must be unique")

        user = User(email=email, password=password,
                    first_name=first_name, last_name=last_name,
                    is_admin=is_admin)
        return self.users.add(user)

    def update_user(self, user_id, data):
        user = self.users.get(user_id)
        if user is None:
            raise ValueError("user not found")
        user.update_user(data)
        return user

    def delete_user(self, user_id):
        return self.users.delete(user_id)

    # -------- Place Methods --------
    def create_place(self, name, owner_id, description="", price_per_night=0,
                     latitude=0.0, longitude=0.0):
        owner = self.users.get(owner_id)
        if owner is None:
            raise ValueError("owner must exist")

        place = Place(name=name, owner=owner, description=description,
                      price_per_night=price_per_night,
                      latitude=latitude, longitude=longitude)
        return self.places.add(place)

    def update_place(self, place_id, data):
        place = self.places.get(place_id)
        if place is None:
            raise ValueError("place not found")

        if "owner_id" in data:
            owner = self.users.get(data["owner_id"])
            if owner is None:
                raise ValueError("owner must exist")
            data = data.copy()
            data["owner"] = owner
            data.pop("owner_id")

        place.update_place(data)
        return place

    def delete_place(self, place_id):
        return self.places.delete(place_id)

    def search_place(self, criteria=None):
        """UML: search_place(). Minimal filter by name substring."""
        if criteria is None:
            return self.places.list_all()

        if not isinstance(criteria, dict):
            raise ValueError("criteria must be a dict")

        name_q = criteria.get("name")
        results = self.places.list_all()
        if isinstance(name_q, str) and name_q.strip():
            q = name_q.strip().lower()
            results = [p for p in results if q in p.name.lower()]

        return results

    # -------- Amenity Methods --------
    def create_amenity(self, name):
        amenity = Amenity(name=name)
        return self.amenities.add(amenity)

    def update_amenity(self, amenity_id, data):
        amenity = self.amenities.get(amenity_id)
        if amenity is None:
            raise ValueError("amenity not found")
        amenity.update_amenity(data)
        return amenity

    def delete_amenity(self, amenity_id):
        return self.amenities.delete(amenity_id)

    # -------- Review Methods --------
    def create_review(self, text, rating, author_id, place_id):
        author = self.users.get(author_id)
        if author is None:
            raise ValueError("author must exist")

        place = self.places.get(place_id)
        if place is None:
            raise ValueError("place must exist")

        review = Review(text=text, rating=rating, author=author, place=place)
        self.reviews.add(review)

        place.add_review(review)
        return review

    def update_review(self, review_id, data):
        review = self.reviews.get(review_id)
        if review is None:
            raise ValueError("review not found")
        review.update_review(data)
        return review

    def delete_review(self, review_id):
        return self.reviews.delete(review_id)

    def add_amenity_to_place(self, place_id, amenity_id):
        place = self.places.get(place_id)
        if place is None:
            raise ValueError("place not found")

        amenity = self.amenities.get(amenity_id)
        if amenity is None:
            raise ValueError("amenity not found")

        place.add_amenity(amenity)
        return place
