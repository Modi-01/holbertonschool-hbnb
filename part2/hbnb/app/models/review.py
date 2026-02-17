from app.models.base_model import BaseModel


class Review(BaseModel):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = kwargs.get("text")
        self.rating = kwargs.get("rating")
        self.author = kwargs.get("author")  
        self.place = kwargs.get("place")    

    def create_review(self):
        pass

    def update_review(self):
        pass

    def delete_review(self):
        pass

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "text": self.text,
            "rating": self.rating,
            "author": self.author,
            "place": self.place,
        })
        return data
