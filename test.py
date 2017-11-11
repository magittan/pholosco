import requests

website = requests.get('https://api.flickr.com/services')

#what
print (website.status_code)
