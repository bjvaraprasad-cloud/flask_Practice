import os
import pytest
from app import app, mongo

@pytest.fixture
def client():
    app.config["TESTING"] = True
    os.environ["MONGO_URI"] = "mongodb://localhost:27017/testdb"

    app.config["MONGO_URI"] = os.environ["MONGO_URI"]

    with app.app_context():
        mongo.db.students.delete_many({})

    return client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_add_student(client):
    response = client.post("/add", json={"name": "John", "age": 20})
    assert response.status_code == 200


def test_update_student(client):
    response = client.put("/update/John", json={"age": 21})
    assert response.status_code == 200


def test_delete_student(client):
    response = client.delete("/delete/John")
    assert response.status_code == 200
