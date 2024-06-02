import pytest
from src.server import app
from flask import url_for
import mongomock
from src import db


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    client = app.test_client()
    with app.app_context():
        db.client = mongomock.MongoClient()
        db.db = db.client[db.db_name]
    yield client


def test_home(client):
    response = client.get(url_for('home'))
    assert response.status_code == 200


def test_signup(client):
    response = client.post(url_for('signup'), data={'email': 'test@test.com', 'password': 'test'})
    assert response.status_code == 302  # Redirect to login


def test_login(client):
    client.post(url_for('signup'), data={'email': 'test@test.com', 'password': 'test'})
    response = client.post(url_for('login'), data={'email': 'test@test.com', 'password': 'test'})
    assert response.status_code == 302  # Redirect to weather


def test_login_fail(client):
    client.post(url_for('signup'), data={'email': 'test@test.com', 'password': 'test'})
    response = client.post(url_for('login'), data={'email': 'test@test.com', 'password': 'wrongpassword'})
    assert response.status_code == 400


def test_weather_forecast(client, monkeypatch):
    def mock_getforecast(city):
        return {
            "temperature": 25,
            "pressure": 1000,
            "humidity": 50
        }
    
    monkeypatch.setattr('src.weather.getforecast', mock_getforecast)
    
    response = client.post(url_for('weather_forecast'), data={'city': 'TestCity'})
    assert response.status_code == 200
    assert b"temperature" in response.data
