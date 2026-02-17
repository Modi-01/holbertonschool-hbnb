from app.models.base_model import BaseModel


class Amenity(BaseModel):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get("name")
        self.places = kwargs.get("places", [])  

    def create_amenity(self):
        pass

    def update_amenity(self):
        pass

    def delete_amenity(self):
        pass

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "name": self.name,
            "places": self.places,
        })
        return data
