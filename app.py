from flask import Flask

import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__)

CP_HOST = 'http://54.243.195.23'

@app.route('/')
def hello_world():

    with open('teams.json', 'r') as f:
        teams = json.load(f)

    for number, name in teams.items():
        page = requests.get(CP_HOST + '/team.php?team=' + number).content
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
    return "It worked!"
