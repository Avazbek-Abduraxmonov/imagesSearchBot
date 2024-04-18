import requests

url = "https://real-time-image-search.p.rapidapi.com/search"

querystring = {"query":"beach"}

headers = {
	"X-RapidAPI-Key": "34fe6d2e50msh7e10501cd13c417p19e723jsnc12607a15468",
	"X-RapidAPI-Host": "real-time-image-search.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
# data = response.json().get('data')['url']
# print(data)
print(response.json())