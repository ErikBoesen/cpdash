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
        table_data = soup.find_all('tr')[1]
        play_time = table_data.select('td')[6].text
        score = table_data.select('td')[8].text
        chart_script = soup.find_all('script')[-1]
        content.append({
            'number': number,
            'name': name,
            'play_time': play_time,
            'score': score,
            'main_table': main_table,
            'chart_script': chart_script.replace('chart_div', 'chart_div_' + number),
        })
        #print(google_script)
        #print(main_table)
        #print(chart_script)
        #print(chart)
    return render_template('index.html', teams=content)
