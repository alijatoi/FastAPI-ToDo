from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is in the 'main.py' file

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI To-Do API"}
