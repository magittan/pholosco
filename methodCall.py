from urllib.request import urlopen
import json


class Photo:

	def __init__ (self,it, lat,longi,serverID, farmID,secr):
		self.__photo_id = it
		self.__latitude = lat
		self.__longitude = longi
		self.__server_id = serverID
		self.__farm_id = farmID
		self.__seccret = secr

	def get_photo_id(self):
		return self.__photo_id

	def get_latitude(self):
		return self.__latitude

	def get_longitude(self):
		return self.__longitude

	def get_server_id(self):
		return self.__server_id

	def get_farm_id(self):
		return self.__farm_id

	def get_secret(self):
		return self.__seccret

	def __str__(self):
		return str(self.get_photo_id())


class mainPhoto:


	def __init__ (self):
		self.apiKey = "c5ffff1a95a4ab5a9e440d76ad56f247"


	def getData(self, number):
		#get photos id then convert into python list
		photoInfo = []
		url1 = "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=c5ffff1a95a4ab5a9e440d76ad56f247&place_id=.skCPTpTVr.Q3WKW&per_page=5&page=1&format=json&nojsoncallback=1"
		r = urlopen(url1)
		text = r.read()
		parsed_response = json.loads(text)

		# check = json.dumps(parsed_response, indent=4, sort_keys=True)
		# print(check)

		for i in range(number):
			it = parsed_response["photos"]["photo"][i]['id']
			#print(id)
			farm = parsed_response["photos"]["photo"][i]['farm']
			secret = parsed_response["photos"]["photo"][i]['secret']
			server = parsed_response["photos"]["photo"][i]['server']

			url2 = 'https://api.flickr.com/services/rest/?method=flickr.photos.geo.getLocation' + \
			'&api_key=c5ffff1a95a4ab5a9e440d76ad56f247&photo_id='+ it + '&format=json&nojsoncallback=1'
			r2 = urlopen(url2)
			text2 = r2.read()
			parsed_response2 = json.loads(text2)

			lat = parsed_response2["photo"]["location"]["latitude"]
			longi = parsed_response2["photo"]["location"]["longitude"]
			#print (i)

			photoInfo.append(Photo(it,lat,longi,server,farm,secret))
		return photoInfo
