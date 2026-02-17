from app.models.base_model import BaseModel


class User(BaseModel):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")
        self.first_name = kwargs.get("first_name")
        self.last_name = kwargs.get("last_name")
        self.is_admin = kwargs.get("is_admin", False)

  
    def create_user(self):
        pass

    def update_user(self):
        pass

    def delete_user(self):
        pass

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_admin": self.is_admin,
        })
        return data
