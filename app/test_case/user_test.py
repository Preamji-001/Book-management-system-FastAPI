from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from main import app, get_db  # Replace 'your_main_module' with the actual module name
from models import User

def test_create_user():
    # Create a TestClient instance with the FastAPI app
    client = TestClient(app)

    # Mock a database session using the dependency
    def override_get_db():
        try:
            db = next(get_db())
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    # Data for the user creation request
    user_data = {
        "username": "testuser",
        "password": "testpassword",
        # Add other required fields as needed
    }

    # Make a request to create a user
    response = client.post("/user/", json=user_data)

    # Assert the response status code is 201 Created
    assert response.status_code == 201

    # Assert the response has the expec
