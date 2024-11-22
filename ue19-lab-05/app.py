import requests

def fetch_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    if response.status_code == 200:
        joke_data = response.json()
        if joke_data.get("type") == "single":
            print(f"Joke: {joke_data['joke']}")
        else:
            print(f"Setup: {joke_data['setup']}")
            print(f"Delivery: {joke_data['delivery']}")
    else:
        print(f"Failed to fetch joke. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_joke()
