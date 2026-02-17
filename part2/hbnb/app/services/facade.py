# Business Logic Layer (Facade Pattern)

from app.persistence.repository import InMemoryRepository


class HBnBFacade:
    """
    Facade that centralizes all use-cases.
    
    """

    def __init__(self):
      
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # -----Placeholder methods------

    def create_user(self, user_data):
        """
        Placeholder for creating a user.
        
        """
        return None

    def get_user(self, user_id):
        """
        Placeholder for fetching a user by ID.
        """
        return self.user_repo.get(user_id)

    def create_place(self, place_data):
        """
        Placeholder for creating a place.
        """
        return None

    def get_place(self, place_id):
        """
        Placeholder for fetching a place by ID.
        """
        return self.place_repo.get(place_id)

    def create_review(self, review_data):
        """
        Placeholder for creating a review.
        """
        return None

    def create_amenity(self, amenity_data):
        """
        Placeholder for creating an amenity.
        """
        return None
