import pytest
from httpx import AsyncClient
from main import app
import time


@pytest.mark.asyncio
async def test_user_signup_and_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        unique_email = f"testuser{int(time.time())}@example.com"
        signup_data = {"email": unique_email, "password": "testpass"}

        # Sign up
        signup_response = await ac.post("/users/signup", json=signup_data)
        assert signup_response.status_code == 200

        # Log in
        login_response = await ac.post("/users/login", json=signup_data)
        assert login_response.status_code == 200

        token = login_response.json().get("access_token")
        assert token is not None
        return token


@pytest.mark.asyncio
async def test_add_and_get_movie():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        token = await test_user_signup_and_login()
        headers = {"Authorization": f"Bearer {token}"}
        movie_data = {
            "title": f"Inception {int(time.time())}",  # unique title
            "director": "Christopher Nolan",
            "year": 2010,
        }

        # Add movie
        add_response = await ac.post("/movies/", json=movie_data, headers=headers)
        assert add_response.status_code == 200
        movie_id = add_response.json().get("_id")
        assert movie_id is not None

        # Get movies
        get_response = await ac.get("/movies/", headers=headers)
        assert get_response.status_code == 200
        movies = get_response.json()
        assert any(movie["title"] == movie_data["title"] for movie in movies)


@pytest.mark.asyncio
async def test_create_review():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        token = await test_user_signup_and_login()
        headers = {"Authorization": f"Bearer {token}"}

        # First create a movie to review
        movie_data = {
            "title": f"The Matrix {int(time.time())}",
            "director": "Wachowski Sisters",
            "year": 1999,
        }
        movie_resp = await ac.post("/movies/", json=movie_data, headers=headers)
        assert movie_resp.status_code == 200
        movie_id = movie_resp.json().get("_id")
        assert movie_id is not None

        # Now create a review for that movie
        review_data = {
            "movie_id": movie_id,
            "rating": 5,
            "comment": "Mind-blowing sci-fi!",
        }

        response = await ac.post("/reviews/", json=review_data, headers=headers)
        assert response.status_code == 200
        review = response.json()
        assert review["rating"] == 5
        assert review["comment"] == "Mind-blowing sci-fi!"
