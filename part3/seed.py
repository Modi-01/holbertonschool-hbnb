from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity
from app.models.review import Review

app = create_app()

with app.app_context():
    print("Starting seed...")

    # -------------------------
    # 1) USERS
    # -------------------------
    owner = User.query.first()
    if not owner:
        raise Exception("No user found in the database. Create your first user before running this seed file.")

    reviewer = User.query.filter_by(email="reviewer@test.com").first()
    if not reviewer:
        reviewer = User(
            email="reviewer@test.com",
            first_name="Review",
            last_name="User",
            password="123456",
            is_admin=False
        )
        db.session.add(reviewer)
        db.session.commit()

    # -------------------------
    # 2) AMENITIES
    # -------------------------
    amenity_names = ["WiFi", "Parking", "Pool"]
    amenity_objects = {}

    for name in amenity_names:
        amenity = Amenity.query.filter_by(name=name).first()
        if not amenity:
            amenity = Amenity(name=name)
            db.session.add(amenity)
            db.session.commit()
        amenity_objects[name] = amenity

    # -------------------------
    # 3) PLACES
    # -------------------------
    place_data = [
    {
        "name": "Nice Apartment",
        "description": "Clean and modern apartment in Riyadh",
        "price_per_night": 100.0,
        "latitude": 24.7136,
        "longitude": 46.6753,
        "country": "Saudi Arabia",
        "amenities": ["WiFi", "Parking"]
    },
    {
        "name": "Cozy Studio",
        "description": "Small but comfortable studio in Dubai",
        "price_per_night": 80.0,
        "latitude": 25.2048,
        "longitude": 55.2708,
        "country": "UAE",
        "amenities": ["WiFi", "Pool"]
    },
    {
        "name": "Family Villa",
        "description": "Spacious villa in Cairo",
        "price_per_night": 250.0,
        "latitude": 30.0444,
        "longitude": 31.2357,
        "country": "Egypt",
        "amenities": ["WiFi", "Parking", "Pool"]
    },
    {
        "name": "Budget Room",
        "description": "Affordable room in Amman",
        "price_per_night": 50.0,
        "latitude": 31.9539,
        "longitude": 35.9106,
        "country": "Jordan",
        "amenities": ["WiFi"]
    },
    {
        "name": "City View Apartment",
        "description": "Modern apartment in Paris",
        "price_per_night": 130.0,
        "latitude": 48.8566,
        "longitude": 2.3522,
        "country": "France",
        "amenities": ["WiFi", "Parking"]
    },
    {
        "name": "Beach House",
        "description": "Relaxing house in Barcelona",
        "price_per_night": 300.0,
        "latitude": 41.3851,
        "longitude": 2.1734,
        "country": "Spain",
        "amenities": ["WiFi", "Pool"]
    },
    {
        "name": "Mountain Cabin",
        "description": "Cabin in Swiss Alps",
        "price_per_night": 170.0,
        "latitude": 46.8182,
        "longitude": 8.2275,
        "country": "Switzerland",
        "amenities": ["WiFi"]
    },
    {
        "name": "Luxury Suite",
        "description": "Luxury stay in New York",
        "price_per_night": 420.0,
        "latitude": 40.7128,
        "longitude": -74.0060,
        "country": "USA",
        "amenities": ["WiFi", "Parking", "Pool"]
    },
    {
        "name": "Studio Flat",
        "description": "Compact flat in London",
        "price_per_night": 75.0,
        "latitude": 51.5074,
        "longitude": -0.1278,
        "country": "UK",
        "amenities": ["WiFi"]
    },
    {
        "name": "Desert Camp",
        "description": "Desert experience in Morocco",
        "price_per_night": 210.0,
        "latitude": 31.7917,
        "longitude": -7.0926,
        "country": "Morocco",
        "amenities": ["Parking"]
    },
    {
        "name": "Business Hotel Room",
        "description": "Business stay in Tokyo",
        "price_per_night": 190.0,
        "latitude": 35.6762,
        "longitude": 139.6503,
        "country": "Japan",
        "amenities": ["WiFi", "Parking"]
    },
    {
        "name": "Farm Stay",
        "description": "Countryside stay in Germany",
        "price_per_night": 95.0,
        "latitude": 51.1657,
        "longitude": 10.4515,
        "country": "Germany",
        "amenities": ["Parking", "Pool"]
    }
]

    created_places = []

    for item in place_data:
        place = Place.query.filter_by(title=item["name"]).first()
        if not place:
            place = Place(
                name=item["name"],
                owner=owner,
                description=item["description"],
                price_per_night=item["price_per_night"],
                latitude=item["latitude"],
                longitude=item["longitude"]
            )
            place.country = item["country"]
            db.session.add(place)
            db.session.commit()

        selected_amenities = [amenity_objects[a] for a in item["amenities"]]
        place.set_amenities(selected_amenities)
        db.session.commit()

        created_places.append(place)

    # -------------------------
    # 4) REVIEWS
    # -------------------------
    review_data = [
        {
            "place_title": "Nice Apartment",
            "text": "Very clean and comfortable place.",
            "rating": 5
        },
        {
            "place_title": "Cozy Studio",
            "text": "Nice location and good value.",
            "rating": 4
        },
        {
            "place_title": "Family Villa",
            "text": "Large space and perfect for families.",
            "rating": 5
        },
        {
            "place_title": "Budget Room",
            "text": "Simple room but worth the price.",
            "rating": 4
        },
        
    ]

    for item in review_data:
        place = Place.query.filter_by(title=item["place_title"]).first()
        if not place:
            continue

        existing_review = Review.query.filter_by(
            text=item["text"],
            rating=item["rating"]
        ).first()

        if not existing_review:
            review = Review(
                text=item["text"],
                rating=item["rating"],
                author=reviewer,
                place=place
            )
            db.session.add(review)
            db.session.commit()

    print("Seed completed successfully.")
    print(f"Users: {User.query.count()}")
    print(f"Amenities: {Amenity.query.count()}")
    print(f"Places: {Place.query.count()}")
    print(f"Reviews: {Review.query.count()}")
