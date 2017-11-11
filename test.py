import requests

website = requests.get('https://api.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=c5ffff1a95a4ab5a9e440d76ad56f247')

#what
print website.status_code
