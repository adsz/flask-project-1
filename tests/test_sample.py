import pytest
from flask import Flask

# Assume your main Flask app is in a file called hello.py
from hello import app as flask_app

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_home_page(client):
    """Test the home page returns a successful response and correct content."""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Hello, World!' in rv.data

def test_about_page(client):
    """Test the about page returns a successful response and correct content."""
    rv = client.get('/about')
    assert rv.status_code == 200
    assert b'This is the about page.' in rv.data

def test_404_page(client):
    """Test that a non-existent page returns a 404 error."""
    rv = client.get('/non-existent-page')
    assert rv.status_code == 404
