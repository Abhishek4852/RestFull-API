import requests
import json

# Correct URL based on the endpoint definition
url = "http://127.0.0.1:5000/toys/1"

# Data to update the toy
data = {
    "id": 1,  # The ID of the toy to update must match the endpoint
    "name": "Dolly",
    "type": "Dolly chay wala toy"
}

# Send the PUT request with JSON data
response = requests.put(url, json=data)

# Print the response text
print(response.text)
