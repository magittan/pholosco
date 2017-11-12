import requests
import shutil
from urllib.request import urlopen
import hashlib

# secret = "1bdc766eee4d312f"
# url1 = "http://api.flickr.com/services/rest/?&method=flickr.photos.getPopular&api_key=c5ffff1a95a4ab5a9e440d76ad56f247&user_id="

# m = hashlib.sha1()
# m.update(secret)
# m.digest()

# def urlconcat(str):
# 	output = url1 + str + "&format=json"
# 	return output

# url3 = urlconcat("47318367%40N08")

# print (url3)

# r = urlopen(url3)

# text = r.read()

# print (text)



url1 = 'https://farm5.staticflickr.com/4526/38306537401_dc945483be_b.jpg'
response = requests.get(url1, stream=True)
with open('38306537401_dc945483be_b.jpg', 'wb') as out_file:
   shutil.copyfileobj(response.raw, out_file)
del response
