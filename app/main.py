import requests
import os


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    URL = "http://api.weatherapi.com/v1/current.json"
    CITY = "Paris"

    PARAMS = {"key": api_key, "q": CITY}
    response = requests.get(URL, params=PARAMS)

    data = response.json()
    print(f"Current weather in {data['location']['name']}: {data['current']['temp_c']}°C")


if __name__ == "__main__":
    get_weather()
