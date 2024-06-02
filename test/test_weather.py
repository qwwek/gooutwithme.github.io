import pytest
from src.weather import getforecast
from unittest.mock import patch

def test_getforecast():
    with patch('pywttr.Wttr') as MockWttr:
        mock_wttr = MockWttr.return_value
        mock_wttr.en.return_value.weather = [
            {"hourly": [{"temp_c": 20, "pressure": 1000, "humidity": 50}]}
        ]
        forecast = getforecast("TestCity")
        assert forecast is not None
        assert forecast["temperature"] == 20
        assert forecast["pressure"] == 1000
        assert forecast["humidity"] == 50

def test_getforecast_fail():
    with patch('pywttr.Wttr') as MockWttr:
        mock_wttr = MockWttr.return_value
        mock_wttr.en.return_value.weather = []
        forecast = getforecast("TestCity")
        assert forecast is None
