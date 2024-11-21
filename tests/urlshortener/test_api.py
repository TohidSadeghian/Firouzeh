from fastapi.testclient import TestClient
from src.main import app
from src.config import URL_SHORTENER_CHAR_LEN
from fastapi import status


client = TestClient(app)


class TestUrlShortener:
    create_url = "/create_url/"

    def test_create_shortened_url(self):
        data = {"original_url": "https://www.google.com"}
        response = client.post(self.create_url, json=data)

        assert response.status_code == status.HTTP_201_CREATED
        assert "original_url" in response.json()
        assert len(response.json()['shortened_url']) == URL_SHORTENER_CHAR_LEN

    def test_create_with_invalid_url(self):
        data = {"original_url": "www.example.com"}
        response = client.post(self.create_url, json=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST


    def test_redirect_with_shortened_link(self):
        data = {"original_url": "https://www.google.com"}
        response = client.post(self.create_url, json=data)

        shortened_url = response.json()['shortened_url']
        response = client.get(f"/{shortened_url}", follow_redirects=False)
        assert response.status_code == 307
        assert response.headers["Location"] == data['original_url']

        response = client.get("/non-existing-path", follow_redirects=False)
        assert response.status_code == 404