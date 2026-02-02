# Explanatory Notes – Sequence Diagrams

This document provides explanatory notes for the sequence diagrams created as part of Task 2.
Each diagram illustrates the interaction between the Presentation Layer, Business Logic Layer,
and Persistence Layer for core API calls in the HBnB application.

---

## User Registration

This sequence diagram illustrates the user registration process within the HBnB application.

The flow begins when the user opens the registration page and enters the required information
(name, email, and password) through the UI. The UI sends the registration request to the API,
which forwards the data to the Business Logic layer for validation.

Once the data is validated, the Business Logic layer stores the new user information in the
database through the Persistence layer. A success response is then returned back to the user.

This diagram demonstrates the separation of responsibilities between system layers and
ensures proper validation and data persistence.

---

## Place Creation

This sequence diagram represents the process of creating a new place listing.

The user fills in the place details through the UI and submits the form. The UI sends the place
data to the API, which passes it to the Business Logic layer for validation and processing.

After validation, the place data is saved in the database via the Persistence layer.
A confirmation response is returned to the user indicating that the place has been created
successfully.

This sequence highlights how user-generated content flows through the system in a structured
and controlled manner.

---

## Review Submission

This sequence diagram describes the workflow for submitting a review for a place.

The user writes a review that includes a rating and comment through the UI. The review data
is sent to the API and then forwarded to the Business Logic layer for validation.

Once validated, the review is stored in the database through the Persistence layer.
A success response is returned to the user confirming that the review has been submitted.

This diagram emphasizes how user feedback is handled while maintaining data integrity.

---

## Fetching a List of Places

This sequence diagram illustrates the process of retrieving a list of places based on
user-defined criteria.

The user requests a list of places through the UI. The request is sent to the API and then
processed by the Business Logic layer, where filtering and sorting rules are applied.

The database is queried to retrieve the matching places. The resulting list is returned
through the API to the UI and displayed to the user.

This sequence demonstrates efficient data retrieval and clear interaction between system layers.
