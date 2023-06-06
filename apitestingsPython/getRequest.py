import requests


url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=en-US&page=1'

response = requests.get(url)

if response.status_code == 200:
    results = response.json()['results']
    print(f'Total results: {len(results)}')
    for movie in results:
        print(f'{movie["title"]} ({movie["release_date"]})')
else:
    print(f'Request failed with status code {response.status_code}')
