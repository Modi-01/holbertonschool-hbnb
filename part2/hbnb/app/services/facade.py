# -------- Place Methods (Task 4 required) --------
    def get_place(self, place_id):
        return self.places.get(place_id)

    def get_all_places(self):
        return self.places.list_all()

    def create_place_from_api(self, place_data):
        """
        place_data expects keys from API:
        title, description, price, latitude, longitude, owner_id, amenities (list of amenity ids)
        """
        if not isinstance(place_data, dict):
            raise ValueError("place_data must be a dict")

        owner_id = place_data.get("owner_id")
        if not owner_id:
            raise ValueError("owner_id is required")

        owner = self.users.get(owner_id)
        if owner is None:
            raise ValueError("owner must exist")

        title = place_data.get("title")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("title is required")

        description = place_data.get("description", "")
        price = place_data.get("price", 0)
        latitude = place_data.get("latitude", 0.0)
        longitude = place_data.get("longitude", 0.0)

        # Place model validates latitude/longitude and price_per_night >= 0
        place = Place(
            name=title,  # mapping title -> name
            owner=owner,
            description=description,
            price_per_night=price,  # mapping price -> price_per_night
            latitude=latitude,
            longitude=longitude
        )

        place = self.places.add(place)

        # handle amenities ids list
        amenity_ids = place_data.get("amenities", [])
        if amenity_ids is None:
            amenity_ids = []
        if not isinstance(amenity_ids, list):
            raise ValueError("amenities must be a list of amenity ids")

        for amenity_id in amenity_ids:
            amenity = self.amenities.get(amenity_id)
            if amenity is None:
                raise ValueError("amenity must exist")
            place.add_amenity(amenity)

        return place

    def update_place_from_api(self, place_id, place_data):
        """
        Update place using API keys:
        title, description, price, latitude, longitude, owner_id, amenities
        """
        place = self.places.get(place_id)
        if place is None:
            raise ValueError("place not found")

        if not isinstance(place_data, dict):
            raise ValueError("place_data must be a dict")

        data = {}

        if "title" in place_data:
            data["name"] = place_data.get("title")
        if "description" in place_data:
            data["description"] = place_data.get("description")
        if "price" in place_data:
            data["price_per_night"] = place_data.get("price")
        if "latitude" in place_data:
            data["latitude"] = place_data.get("latitude")
        if "longitude" in place_data:
            data["longitude"] = place_data.get("longitude")

        # owner update
        if "owner_id" in place_data:
            owner = self.users.get(place_data.get("owner_id"))
            if owner is None:
                raise ValueError("owner must exist")
            data["owner"] = owner

        # apply updates
        if data:
            place.update_place(data)

        # update amenities (replace list)
        if "amenities" in place_data:
            amenity_ids = place_data.get("amenities") or []
            if not isinstance(amenity_ids, list):
                raise ValueError("amenities must be a list of amenity ids")

            # reset current amenities safely
            place.amenity = []
            for amenity_id in amenity_ids:
                amenity = self.amenities.get(amenity_id)
                if amenity is None:
                    raise ValueError("amenity must exist")
                place.add_amenity(amenity)

        return place

    # -------- Review Methods (Task 5 required) --------
    def get_review(self, review_id):
        return self.reviews.get(review_id)

    def get_all_reviews(self):
        return self.reviews.list_all()

    def get_reviews_by_place(self, place_id):
        place = self.places.get(place_id)
        if place is None:
            raise ValueError("place not found")
        # Place model keeps reviews in place.review list
        return list(place.review)

    def create_review_from_api(self, review_data):
        """
        review_data expects keys from API:
        text, rating, user_id, place_id
        """
        if not isinstance(review_data, dict):
            raise ValueError("review_data must be a dict")

        text = review_data.get("text")
        rating = review_data.get("rating")
        user_id = review_data.get("user_id")
        place_id = review_data.get("place_id")

        if not user_id:
            raise ValueError("user_id is required")
        if not place_id:
            raise ValueError("place_id is required")

        author = self.users.get(user_id)
        if author is None:
            raise ValueError("author must exist")

        place = self.places.get(place_id)
        if place is None:
            raise ValueError("place must exist")

        review = Review(text=text, rating=rating, author=author, place=place)
        self.reviews.add(review)
        place.add_review(review)

        return review

    def update_review_from_api(self, review_id, review_data):
        review = self.reviews.get(review_id)
        if review is None:
            raise ValueError("review not found")
        if not isinstance(review_data, dict):
            raise ValueError("review_data must be a dict")

        allowed = {}
        if "text" in review_data:
            allowed["text"] = review_data.get("text")
        if "rating" in review_data:
            allowed["rating"] = review_data.get("rating")

        if not allowed:
            raise ValueError("no valid fields to update")

        review.update_review(allowed)
        return review

    def delete_review_from_api(self, review_id):
        review = self.reviews.get(review_id)
        if review is None:
            raise ValueError("review not found")

        # remove from place.review list too
        place = review.place
        if place and hasattr(place, "review") and review in place.review:
            place.review.remove(review)

        deleted = self.reviews.delete(review_id)
        return deleted
