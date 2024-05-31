from bs4 import BeautifulSoup
import requests

url = "https://hu.wikipedia.org/wiki/Kezd%C5%91lap"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html', features='lxml')

# print(soup)  

# table = soup.find_all('table')[1]
# print(table)

world_titles = soup.find_all('th')
print(world_titles)


