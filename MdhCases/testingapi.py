import requests
url = "http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api"
response_dictionary = requests.get(url+"/2000").json()
print(response_dictionary["gamedays"])