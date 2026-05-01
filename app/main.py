import requests
import os


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    url = "http://api.weatherapi.com/v1/current.json"

    params = {"key": api_key, "q": "Paris"}
    response = requests.get(url, params=params)

    data = response.json()
    print(f"Current weather in {data['location']['name']}: {data['current']['temp_c']}°C")


if __name__ == "__main__":
    get_weather()
