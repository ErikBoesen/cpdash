from flask import Flask, render_template

import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__)

CP_HOST = 'http://54.243.195.23'
with open('teams.json', 'r') as f:
    teams = json.load(f)

@app.route('/')
def hello_world():
    content = []
    for number, name in teams.items():
        page = requests.get(CP_HOST + '/team.php?team=' + number).content
        soup = BeautifulSoup(page, 'html.parser')
        main_table = soup.find('table', class_='CSSTableGenerator')
        chart_script = soup.find_all('script')[-1]
        chart = soup.find(id='chart_div')
        content.append({
            'number': number,
            'name': name,
            'main_table': main_table,
            'chart_script': chart_script,
            'chart': chart,
        })
        #print(google_script)
        #print(main_table)
        #print(chart_script)
        #print(chart)
    return render_template('index.html', teams=content)
