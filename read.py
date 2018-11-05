import requests
from bs4 import BeautifulSoup
from pick import pick
from urllib.parse import unquote
import argparse

HOST = 'http://54.243.195.23'

team_number = '11-1091'
page = requests.get(HOST + '/team.php?team=' + team_number).content
soup = BeautifulSoup(page, 'html.parser')
google_script = soup.find('script')
main_table = soup.find('table', class_='CSSTableGenerator')
chart_script = soup.find_all('script')[-1]
chart = soup.find(id='chart_div')

#print(soup)
#print(soup.prettify())
print(google_script)
print(main_table)
print(chart_script)
print(chart)
