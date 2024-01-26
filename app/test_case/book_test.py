from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
import database
from main import app
def test_get_books():
    # Create a TestClient instance with the FastAPI app
    client = TestClient(app)

    # Mock a database session using the dependency
    def override_get_db():
        try:
            db = next(database.get_db())
            yield db
        finally:
            db.close()

    app.dependency_overrides[database.get_db] = override_get_db

    # Make a request to the endpoint
    response = client.get("/")

    # Assert the response status code is 200 OK
    assert response.status_code == 200

    # Assert the response has a JSON content
    assert response.headers["content-type"] == "application/json"

    # Assuming you are expecting a list of books as a response
    books = response.json()
    assert isinstance(books, list)

    app.dependency_overrides.clear()
