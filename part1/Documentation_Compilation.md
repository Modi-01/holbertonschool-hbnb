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
## High-Level Architecture
#### Overview
The system is divided into three layers:
- **Presentation Layer (Services, API)**  
Handles user interactions and exposes API endpoints. It delegates application use-cases to the Business Logic layer through a unified entry point (facade).
- **Business Logic Layer (Models)**  
Contains the core domain entities (User, Place, Review, Amenity) and application rules. It provides a **Facade** that orchestrates use-cases and coordinates persistence actions.
- **Persistence Layer**  
Responsible for data storage and retrieval. It provides repositories/DAOs (or equivalent) that the Business Logic layer uses for CRUD operations.
### Facade Pattern Explanation
The Facade Pattern streamlines interactions between layers by providing a single, simplified interface:
- The Presentation Layer calls HBnBFacade.
- The Facade coordinates business workflows (e.g., validate input, apply rules, call repositories).
- The Persistence Layer remains encapsulated behind the Facade and repository access, preventing direct coupling.
