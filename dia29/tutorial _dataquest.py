import requests


response = requests.get(" http://api.open-notify.org/astros.json")

print(response.status_code)

print(response.json())

import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

parameters = {
    "lat": 40.71,
    "lon": -74
}

response = requests.get("http://api.open-notify.org/iss-now.json", params=parameters)
jprint(response.json())
pass_times = response.json()['timestamp']
jprint(pass_times)
from datetime import datetime

time = datetime.fromtimestamp(pass_times)

print(time)

