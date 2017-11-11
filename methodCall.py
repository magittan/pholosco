from urllib.request import urlopen
import json


apiKey = "c5ffff1a95a4ab5a9e440d76ad56f247"
api_secret = "1bdc766eee4d312f"

def userIDmod(str):
	str2 = str.replace("@","%40")
	return str2

def urlconcat(method,placeID):
	url = "https://api.flickr.com/services/rest/?method=" + method + \
	"&api_key=c5ffff1a95a4ab5a9e440d76ad56f247&place_id="+ placeID + \
	"&per_page=5&page=1&format=json&nojsoncallback=1"
	return url

def getPhotoID(int):
	idNumber = parsed_response["photos"]["photo"][int]['id']
	return idNumber

def getPhotoLat(int):
	photo_ID = getPhotoID(int)
	r2 = urlopen('https://api.flickr.com/services/rest/?method=flickr.photos.geo.getLocation' + \
	'&api_key=c5ffff1a95a4ab5a9e440d76ad56f247&photo_id='+ photo_ID + '&format=json&nojsoncallback=1')

	text2 = r2.read()
	parsed_text2 = json.loads(text2)

	lat = parsed_text2["photo"]["location"]["latitude"]
	return lat

def getPhotoLong(int):
	photo_ID = getPhotoID(int)
	r2 = urlopen('https://api.flickr.com/services/rest/?method=flickr.photos.geo.getLocation' + \
	'&api_key=c5ffff1a95a4ab5a9e440d76ad56f247&photo_id='+ photo_ID + '&format=json&nojsoncallback=1')

	text2 = r2.read()
	parsed_text2 = json.loads(text2)

	longitude = parsed_text2["photo"]["location"]["longitude"]
	return longitude

#get photos id then convert into python list
r = urlopen(urlconcat("flickr.photos.search",".skCPTpTVr.Q3WKW"))
text = r.read()
parsed_response = json.loads(text)

#creating a dictionary from the json file from first url call



# PhotoLat = getPhotoLat(0)
# PhotoLongitude = getPhotoLong(0)
# print (PhotoLat + "  ,  " + PhotoLongitude)

#check = json.dumps(parsed_response, indent=4, sort_keys=True)



