import requests
from bs4 import BeautifulSoup
from pick import pick
from urllib.parse import unquote
import argparse

HOST = 'http://54.243.195.23'

team_number = '11-1091'
page = requests.get(HOST + '/team.php?team=' + team_number).content
soup = BeautifulSoup(page, 'html.parser')

print(soup)
#print(soup.prettify())
