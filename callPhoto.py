import requests
import shutil

url = 'https://farm5.staticflickr.com/4526/38306537401_dc945483be_b.jpg'
response = requests.get(url, stream=True)
with open('38306537401_dc945483be_b.jpg', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response
