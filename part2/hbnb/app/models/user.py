#!/usr/bin/python3
import re
from app.models.base_model import BaseModel

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class User(BaseModel):


    def __init__(self, email, password, first_name, last_name, is_admin=False):
        super().__init__()
        self.email = None
        self.password = None
        self.first_name = None
        self.last_name = None
        self.is_admin = False

        self.set_email(email)
        self.set_password(password)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_is_admin(is_admin)

    
    def set_email(self, email):
        if not isinstance(email, str) or not email.strip():
            raise ValueError("email is required and must be a non-empty string")
        email = email.strip()
        if not _EMAIL_RE.match(email):
            raise ValueError("email must be a valid email format")
        self.email = email
        self.save()

    def set_password(self, password):
        if not isinstance(password, str) or not password:
            raise ValueError("password is required and must be a non-empty string")
        self.password = password
        self.save()

    def set_first_name(self, first_name):
        if not isinstance(first_name, str) or not first_name.strip():
            raise ValueError("first_name is required and must be a non-empty string")
        first_name = first_name.strip()
        if len(first_name) > 50:
            raise ValueError("first_name must not exceed 50 characters")
        self.first_name = first_name
        self.save()

    def set_last_name(self, last_name):
        if not isinstance(last_name, str) or not last_name.strip():
            raise ValueError("last_name is required and must be a non-empty string")
        last_name = last_name.strip()
        if len(last_name) > 50:
            raise ValueError("last_name must not exceed 50 characters")
        self.last_name = last_name
        self.save()

    def set_is_admin(self, is_admin):
        if not isinstance(is_admin, bool):
            raise ValueError("is_admin must be a boolean")
        self.is_admin = is_admin
        self.save()

    def update_user(self, data):
        """UML mentions update_user; here it's a model-level update helper."""
        if not isinstance(data, dict):
            raise ValueError("data must be a dict")

        if "email" in data:
            self.set_email(data["email"])
        if "password" in data:
            self.set_password(data["password"])
        if "first_name" in data:
            self.set_first_name(data["first_name"])
        if "last_name" in data:
            self.set_last_name(data["last_name"])
        if "is_admin" in data:
            self.set_is_admin(data["is_admin"])
