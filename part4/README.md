# HBnB Part 4 - Simple Web Client

This project phase focuses on building a user-friendly front-end interface for the application using **HTML5**, **CSS3**, and **JavaScript (ES6)**. The client interacts with back-end API services to provide dynamic content and user authentication.

## Overview of Tasks

| Task Number | Task Name | Description |
|---|---|---|
| 0 | Design | Complete the provided HTML and CSS files to match the design specifications for the Login, List, Details, and Review pages. |
| 1 | Login | Implement login functionality using the API, store the JWT token in cookies, and handle the authentication flow. |
| 2 | Index (List) | Display the list of places fetched from the API, implement client-side filtering, and manage authentication state. |
| 3 | Place Details | Show detailed information about a selected place with reviews, and display the add review form for authenticated users. |
| 4 | Add Review Form | Implement the review submission form, restrict access to authenticated users, and handle form submission via the API. |

---

## Objectives

- Build a user-friendly interactive front-end using HTML5, CSS3, and JavaScript ES6.
- Design static pages that follow the provided UI specifications.
- Implement secure authentication using a back-end API.
- Dynamically fetch and display data from the API.
- Enable authenticated users to submit reviews.
- Apply client-side filtering and form validation.

## Learning Goals

By completing this part, the project demonstrates practical use of:

- HTML5 semantic structure
- CSS3 styling and responsive layout basics
- JavaScript ES6 DOM manipulation and event handling
- Fetch API for AJAX requests
- JWT handling through cookies
- Client-side form validation

---

## Project Structure

```text
part4/
├── index.html           # Main landing page / places listing
├── login.html           # User authentication page
├── place.html           # Individual place details page
├── add_review.html      # Review submission page
├── styles.css           # Global stylesheet
├── scripts.js           # Main JavaScript functionality
├── images/              # Image assets
└── README.md
```

---

## Pages

### 1. Home / Places Listing (`index.html`)

Features:
- Display all available places
- Fetch places from the API
- Show place cards dynamically
- Filter places by price range without reloading the page
- Show or hide the login link based on authentication status

Each place card should include:
- Place name
- Price per night
- "View Details" button

### 2. Login (`login.html`)

Features:
- User authentication form
- JWT token management
- Submit email and password to the API
- Store returned token in cookies
- Redirect to `index.html` after successful login
- Display an error message if login fails

### 3. Place Details (`place.html`)

Features:
- Detailed place information
- Amenities list
- Reviews section
- Dynamic loading of place data using place ID from the URL
- Add review functionality for authenticated users only

### 4. Add Review (`add_review.html`)

Features:
- Review form
- Star rating system
- Form validation
- Authentication required
- Submit review data to the API
- Display success or error feedback

---
## Technologies Used

- **HTML5** for structure
- **CSS3** for styling
- **JavaScript (ES6)** for client-side logic
- **Fetch API** for AJAX requests
- **Cookies** for JWT session management

---

## API Interaction Summary

### Authentication
- Endpoint: login endpoint from the back-end API
- Method: `POST`
- Payload: email and password as JSON
- Response: JWT token
- Token storage: browser cookies

### Places
- Endpoint: places listing endpoint
- Method: `GET`
- Purpose: fetch all available places

### Place Details
- Endpoint: place details endpoint using a place ID
- Method: `GET`
- Purpose: fetch one place with details and reviews

### Reviews
- Endpoint: review submission endpoint
- Method: `POST`
- Purpose: submit a review for a place

---

## How to Run

### 1. Backend Setup

Navigate to the back-end directory and run the API server:

```bash
cd ../part3
source venv/bin/activate
python3 run.py
```

The backend should be running at:

```text
http://127.0.0.1:5000
```

### 2. Frontend Setup

#### Run Python HTTP Server

```bash
cd part4
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000
```
---

## Collaboration

Each team member can fork the repository and work on their own version of the project independently. This supports parallel development while keeping the same overall structure and expected functionality.

---

## Author

**Moudhi Almutlaq**.
