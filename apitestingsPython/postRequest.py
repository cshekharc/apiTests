import requests
import json

# Replace the API key with your own
api_key = "dc77eebca384c96122b8a196f70332f5"

# Define the endpoint URL
rate_url = f"https://api.themoviedb.org/3/movie/550/rating?api_key={api_key}"
get_url = f"https://api.themoviedb.org/3/movie/550/rating?api_key={api_key}"

rate_headers = {
    "Content-Type": "application/json;charset=utf-8",
    "Authorization": f"Bearer {api_key}"
}

rate_data = {
    "value": 8.5
}

rate_response = requests.post(rate_url, headers=rate_headers, data=json.dumps(rate_data))

# Print the response status code and JSON response body for the rating request
print(f"Rate Movie Status code: {rate_response.status_code}")
print(f"Rate Movie Response body: {rate_response.json()}")

# Define the request headers for retrieving the movie's rating
get_headers = {
    "Content-Type": "application/json;charset=utf-8",
    "Authorization": f"Bearer {api_key}"
}

# Send the GET request to the "Get Movie Rating" API endpoint
get_response = requests.get(get_url, headers=get_headers)

# Print the response status code and JSON response body for the get rating request
print(f"Get Movie Rating Status code: {get_response.status_code}")
print(f"Get Movie Rating Response body: {get_response.json()}")
