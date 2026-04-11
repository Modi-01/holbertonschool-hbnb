# HBnB Project

## Overview
**HBnB project** is a simplified, AirBnB-like application designed to teach Holberton students how to build web applications end-to-end, from the back end to the front end. The project is divided into four main parts, each part focuses on a distinct set of skills and a core component of full-stack development.


## Part 1 — Technical Documentation
This part provides a structured blueprint of the system before implementation. The goal is to establish a shared understanding of the system’s design, responsibilities, and interactions across layers—making later development phases clearer, faster, and less error-prone.


## Part 2 — Implementation of Business Logic and API Endpoints

This part focuses on turning the Part 1 design into a working implementation using **Python**, **Flask**, and **flask-restx**. The main goal is to build the **Business Logic** and **Presentation** layers of the application in a clean and modular way.

It includes creating the core entities (such as users, places, reviews, and amenities), defining their relationships, and implementing RESTful API endpoints to handle basic CRUD operations. This phase also emphasizes good project structure, clear API design, data serialization, and endpoint testing using **Postman** tool.


## Part 3 — Authentication and Database Integration

In this part, the backend is enhanced with **secure authentication** and **persistent database storage**. The API is protected using **JWT-based authentication** with role-based access control, ensuring that only authorized users can access specific endpoints.

Key improvements include:

- Implementation of **JWT authentication** using Flask-JWT-Extended
- **Role-based authorization** using the `is_admin` attribute
- Integration of **SQLAlchemy ORM** to manage database operations
- Replacement of the in-memory repository with **SQLite** for development
- Preparation for **MySQL** as the production database
- Mapping entities (Users, Places, Reviews, Amenities) to relational database tables
- Ensuring **data validation, consistency, and constraints**
- Designing and visualizing the database schema using **Mermaid.js ER diagrams**

This phase transitions the application from a prototype using temporary storage to a **secure, scalable backend with persistent data storage**, making it closer to a real-world production-ready system.


## Part 4 — Simple Web Client

In this part, the application is brought to life through a simple and interactive web client built with HTML5, CSS3, and JavaScript (ES6). The front end communicates with the back-end API to deliver dynamic content, manage authentication, and provide a smoother end-user experience.

Key improvements include:

- Implementation of the user interface for login, places listing, place details, and review submission
- Integration with the back-end API using Fetch API for asynchronous requests
- JWT-based login flow with token storage in cookies for session persistence
- Dynamic rendering of places and place details using JavaScript DOM manipulation
- Client-side filtering of places by price without reloading the page
- Conditional display of actions and forms depending on the user’s authentication status
- Review submission functionality limited to authenticated users
- Client-side validation for forms and improved navigation across pages

This phase represents the final step in connecting all layers of the project together, resulting in a complete full-stack application that combines structured back-end logic, secure authentication, persistent data storage, and a functional browser-based client.


## Authors
- **Moudhi Almutlaq.**
- **Yara Aldossari.**
- **Randa Baeshen.**
