from urllib.request import urlopen
import json


apiKey = "c5ffff1a95a4ab5a9e440d76ad56f247"
api_secret = "1bdc766eee4d312f"

def userIDmod(str):
	str2 = str.replace("@","%40")
	return str2

def urlconcat(method,bbox):
	url = "https://api.flickr.com/services/rest/?method=" + method + \
	"&api_key=c5ffff1a95a4ab5a9e440d76ad56f247&bbox="+ bbox + \
	"&format=json&nojsoncallback=1"
	return url

r = urlopen(urlconcat("flickr.photos.search",".skCPTpTVr.Q3WKW"))

text = r.read()

print(text)

json_string = '{"Huy":"Awesome", "second" : "Rossum"}'
print(r['37623919984'])