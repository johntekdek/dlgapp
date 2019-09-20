import pytest
from app.api.main import app


@pytest.yield_fixture(scope="function")
def client():
    """
    Setup an app client, this gets executed for each test function.

    :param app: Pytest fixture
    :return: Flask app client
    """
    yield app.test_client()
