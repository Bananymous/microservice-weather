from dotenv import load_dotenv
from flask import Flask
import os
import requests

load_dotenv()
api_key = os.getenv('API_KEY')
if not api_key:
	print('No API_KEY found in the environment')
	exit(1)

app = Flask(__name__)

@app.get('/weather/<city>')
def get_weather(city: str):
	location_response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}')
	if location_response.status_code != 200:
		return location_response.json(), location_response.status_code
	location_json = location_response.json()
	if not location_json:
		return { 'error': f'No location information for {city}' }, 400
	location_json = location_json[0]

	lat = location_json.get('lat')
	lon = location_json.get('lon')
	if not lat or not lon:
		return { 'error': f'No location information for {city}' }, 400

	weather_response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')
	return weather_response.json(), weather_response.status_code
