# microservice-weather

A basic python microservice for fetching weather data. This is done using the [openweathermap](https://openweathermap.org) API.

You can find a live demo at [https://weather.bananymous.com/weather/*city*](https://weather.bananymous.com/weather/Tampere)

## Usage

1. Install required python libraries (flask, requests, python-dotenv)
2. Create a file `.env` with `API_KEY` set to your openweathermap API key
3. Start the server using flask `python3 -m flask --app weather run`
4. Go to [http://localhost:5000/weather/*city*](http://localhost:5000/weather/Tampere) and you can see the weather information in json format
