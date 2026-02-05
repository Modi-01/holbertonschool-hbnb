# HBnB Evolution - Technical Documentation
## Introduction
### Purpose of the Document
This document provides a comprehensive technical blueprint for the **HBnB application** project. It describes the system architecture, key design decisions, and interactions between components. The goal is to guide the upcoming implementation phases and serve as a reference for developers.
### Project Overview
HBnB application is a simplified Airbnb-like application that allows users to:
- Register and manage user profiles (regular users and administrators).
- List properties (places) with details such as title, description, price, and location (latitude/longitude).
- Leave reviews (rating and comment) for places.
- Manage amenities that can be associated with places.
- The application follows a **three-layer architecture** and uses a **Facade Pattern** to ensure modularity, maintainability, and separation of concerns.
