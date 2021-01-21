import requests
from bs4 import BeautifulSoup
import pandas as pd

prefix = "https://content.codecademy.com/courses/beautifulsoup/"
webpage = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html').content

soup = BeautifulSoup(webpage, 'html.parser')

links = []
for a in soup.find_all("a"):
    links.append(prefix + a["href"])

turtle_data = {}
for link in links:
    turtle_page = requests.get(link).content
    turtle_soup = BeautifulSoup(turtle_page, 'html.parser')
    turtle_name = turtle_soup.select(".name")[0].get_text()
    turtle_info = turtle_soup.find("ul").get_text('|').split('|')
    turtle_info = [value for value in turtle_info if value != '\n']
    turtle_data[turtle_name] = turtle_info


turtles_df = pd.DataFrame.from_dict(turtle_data, orient='index')
turtles_df.to_excel('table.xlsx')

print(turtles_df)