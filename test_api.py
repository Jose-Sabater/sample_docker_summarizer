import requests

def test_api():
    url = "http://localhost:5000/summarize"
    try:
        response = requests.post(url, json={'text': """Hello this is a test message. I am a developer building an API
                                            and want to see the results of this summary"""})
        response.raise_for_status()  
        print(response.json())
    except requests.RequestException as e:
        print(f"Request error: {e}")


if __name__ == '__main__':
    test_api()
