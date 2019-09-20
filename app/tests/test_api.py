from app.api.main import app
import json
import pytest


def test_total_endpoint(client):
    """ Should respond with a success 200. """
    response = client.get("/total")
    assert response.status == "200 OK"


def test_data(client):
    """ test that endpoint returns int. """
    response = client.get("/total")
    data = json.loads(response.data.decode("utf-8"))
    assert data == {"total": 50000005000000}
