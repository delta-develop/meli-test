from app.app import app
import pytest
from fastapi.testclient import TestClient
from app.tests.test_matrix_ops import bad_matrix


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def not_mutant():
    return {"is_mutant": False}


@pytest.fixture
def is_mutant():
    return {"is_mutant": True}


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}


def test_bad_matrix(client, bad_matrix, not_mutant):
    response = client.post("/mutant/", json={"dna": bad_matrix.dna_sequences})

    assert response.status_code == 403
    assert response.json() == not_mutant
