#First API program
import requests
import json

parameters = {
    "lat": 40.71,
    "lon": -74
}

response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

print(response.status_code)

#200 Everything went well
#301 Server is redirecting you
#400 Bad request
#401 Not authenticated
#403 Forbidden resource
#404 Resource not found
#503 Server not ready

def jprint(obj):
   # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys = True, indent = 4)
    print(text)

jprint(response.json())

