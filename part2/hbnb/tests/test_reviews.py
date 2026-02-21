#!/usr/bin/python3
import unittest
import uuid
from app import create_app


class TestReviewEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    # ---------------------------------
    # Internal helpers (data setup only)
    # ---------------------------------
    def _seed_valid_review_dependencies(self):
        """Create a valid user and place only to obtain IDs for review tests."""
        unique = uuid.uuid4().hex[:8]

        # create user (setup dependency only)
        user_response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": f"jane.{unique}@example.com"
        })
        self.assertEqual(user_response.status_code, 201)
        user_id = user_response.get_json()['id']

        # create place (setup dependency only)
        place_response = self.client.post('/api/v1/places/', json={
            "title": f"Test Place {unique}",
            "description": "Place used only for review endpoint tests",
            "price": 100,
            "latitude": 24.7136,
            "longitude": 46.6753,
            "owner_id": user_id
        })
        self.assertEqual(place_response.status_code, 201)
        place_id = place_response.get_json()['id']

        return user_id, place_id

    def _create_review_for_test(self):
        user_id, place_id = self._seed_valid_review_dependencies()

        response = self.client.post('/api/v1/reviews/', json={
            "text": "Great place!",
            "rating": 5,
            "user_id": user_id,
            "place_id": place_id
        })
        self.assertEqual(response.status_code, 201)
        return response.get_json()['id']

    # -----------------------------
    # Review endpoint tests only
    # -----------------------------
