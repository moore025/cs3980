import pytest
from httpx import AsyncClient
from main import app


@pytest.mark.asyncio
async def test_user_signup_and_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:

        signup_data = {"email": "testuser@example.com", "password": "testpass"}
        signup_response = await ac.post("/users/signup", json=signup_data)
        assert signup_response.status_code == 200

        login_response = await ac.post("/users/login", json=signup_data)
        assert login_response.status_code == 200
        token = login_response.json().get("access_token")
        assert token is not None
        return token


@pytest.mark.asyncio
async def test_add_and_get_movie():
    token = await test_user_signup_and_login()
    headers = {"Authorization": f"Bearer {token}"}
    movie_data = {"title": "Inception", "director": "Christopher Nolan", "year": 2010}

    async with AsyncClient(app=app, base_url="http://test") as ac:

        add_response = await ac.post("/movies/", json=movie_data, headers=headers)
        assert add_response.status_code == 200

        get_response = await ac.get("/movies/", headers=headers)
        assert get_response.status_code == 200
        movies = get_response.json()
        assert any(movie["title"] == "Inception" for movie in movies)


@pytest.mark.asyncio
async def test_create_review():
    token = await test_user_signup_and_login()
    headers = {"Authorization": f"Bearer {token}"}

    review_data = {
        "movie_id": "some_movie_id",
        "rating": 5,
        "comment": "Amazing movie!",
    }

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/reviews/", json=review_data, headers=headers)

        assert response.status_code in (200, 422)
