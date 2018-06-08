import requests
from bs4 import BeautifulSoup
import urllib.request


page = requests.get('https://simple.wikipedia.org/wiki/List_of_United_States_cities_by_population')
soup = BeautifulSoup(page.text, 'html.parser')
state = ''
city =  soup.find('table')
cities_list = city.find_all('a')
temp__List =[]

new_dict = {}
for cities_name in cities_list:
	temp__List.append(cities_name['title'])
	#state = cities_name['title'][(cities_name['title'].find(',')):]

	#new_dict.update({cities_name['title'] : 'test'})
#print (new_dict)
#print (temp__List)


for idx in range (0 , len(temp__List), 2)
	if (idx < len(temp__List)-1):
		new_dict.update({temp__List[idx] : temp__List[idx+1]})
print(new_dict)