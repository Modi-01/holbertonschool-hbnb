#!/usr/bin/python3
from app.models.base_model import BaseModel
from app.models.user import User


class Review(BaseModel):

    def __init__(self, text, rating, author, place):
        super().__init__()
        self.text = None
        self.rating = None
        self.author = None
        self.place = None

        self.set_text(text)
        self.set_rating(rating)
        self.set_author(author)
        self.set_place(place)

    def set_text(self, text):
        if not isinstance(text, str) or not text.strip():
            raise ValueError("text is required and must be a non-empty string")
        self.text = text.strip()
        self.save()

    def set_rating(self, rating):
        if not isinstance(rating, int):
            raise ValueError("rating must be an integer")
        if rating < 1 or rating > 5:
            raise ValueError("rating must be between 1 and 5")
        self.rating = rating
        self.save()

    def set_author(self, author):
        if not isinstance(author, User):
            raise ValueError("author must be a User instance")
        self.author = author
        self.save()

    def set_place(self, place):
        
        from app.models.place import Place  

        if not isinstance(place, Place):
            raise ValueError("place must be a Place instance")
        self.place = place
        self.save()

    def update_review(self, data):
        if not isinstance(data, dict):
            raise ValueError("data must be a dict")
        if "text" in data:
            self.set_text(data["text"])
        if "rating" in data:
            self.set_rating(data["rating"])
