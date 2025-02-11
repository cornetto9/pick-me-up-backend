# Pick Up Me

## Project Overview

Pick Up Me is a mobile app designed to allow users to post and discover items available for pickup. Users can create accounts, list items with images and locations, and comment on items posted by others. The app is built using a Flask RESTful API for the backend and React Native with Expo for the frontend.

## MVP Features

- **User Authentication**: Users can register and log in using a standard email and password system.
- **Item Listings**: Users can create and update item postings with images and locations.
- **Geolocation**: Item locations are stored using latitude and longitude values.. Google OAuth will be considered for future enhancements.
- **Item Listings**: Users can create and update item postings with images and locations. Deleting items is currently not implemented on the frontend.
- **Geolocation**: Item locations are stored using latitude and longitude values.
- **Commenting System**: Users can leave comments on items.
- **Categories**: Items are categorized into 'General'. The 'Kids' category will be considered for future enhancements.
- **User Profile**: Users can view their posted items. Viewing comments is not currently available.

## Installation Guide

### Backend (Flask API)

#### Prerequisites

- Python (>=3.13)
- Virtual environment (venv or equivalent)
- PostgreSQL database

#### Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/cornetto9/pick-me-up-backend

   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Create a `.env` file in the root directory and add:
     ```sh
     FLASK_ENV=development
     SQLALCHEMY_DATABASE_URI=postgresql://username:password@localhost:5432/pickupme_db
     ```
5. Initialize the database:
   ```sh
   flask db upgrade
   ```
6. Run the server:
   ```sh
   flask run
   ```

### Frontend (React Native with Expo)

#### Prerequisites

- Node.js (>=16.x)
- Expo CLI

#### Steps

1. Clone the frontend repository:
   ```sh
   git clone https://github.com/cornetto9/pick-me-up-frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the development server:
   ```sh
   npm start
   ```

## API Endpoints

### Authentication

- `POST /register` - Register a new user
- `POST /login` - Log in an existing user

### Users

- `GET /users` - Retrieve all users
- `GET /users/<user_id>` - Get a user's profile
- `PATCH /users/<user_id>` - Update user information
- `DELETE /users/<user_id>` - Delete a user account

### Items

- `POST /items` - Create a new item listing
- `GET /items` - Retrieve all items
- `GET /items/user/<user_id>` - Get all items posted by a user
- `PATCH /items/<item_id>` - Update item availability

- `POST /comments` - Create a new comment
- `GET /comments` - Retrieve all comments
- `PATCH /comments/<comment_id>` - Update a comment
- `DELETE /comments/<comment_id>` - Delete a comment

## Deployment

The backend can be deployed on **Heroku**, and the frontend can be hosted using **Expo**. The `DATABASE_URL` environment variable should be set correctly for PostgreSQL.

## Contribution Guidelines

1. Fork the repository and create a new branch.
2. Make your changes and commit them.
3. Push to your branch and create a pull request.
4. Ensure all tests pass before submitting.

## Future Enhancements

- **Google OAuth Authentication**: Future support for signing in with Google.
- **Item Deletion from Frontend**: Implement functionality to delete items from the mobile app.
- **Viewing Comments**: Allow users to view comments on items.
- **Categories Expansion**: Introduce a 'Kids' category for filtering items.

## License

This project is licensed under the MIT License.

