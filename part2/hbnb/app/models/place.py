from app.models.base_model import BaseModel


class Place(BaseModel):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get("name")
        self.description = kwargs.get("description")
        self.price_per_night = kwargs.get("price_per_night")
        self.latitude = kwargs.get("latitude")
        self.longitude = kwargs.get("longitude")

        
        self.owner = kwargs.get("owner")         
        self.reviews = kwargs.get("reviews", [])  
        self.amenities = kwargs.get("amenities", [])  

    def create_place(self):
        pass

    def update_place(self):
        pass

    def delete_place(self):
        pass

    def search_place(self):
        pass

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "name": self.name,
            "description": self.description,
            "price_per_night": self.price_per_night,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner": self.owner,
            "reviews": self.reviews,
            "amenities": self.amenities,
        })
        return data
