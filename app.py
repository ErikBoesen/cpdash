from flask import Flask, render_template

import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__)

TEAM_PATH = 'http://54.243.195.23/team.php?team='
with open('teams.json', 'r') as f:
    targets = json.load(f)

@app.route('/')
def hello_world():
    teams = []
    for number, name in targets.items():
        page = requests.get(TEAM_PATH + number).content
        soup = BeautifulSoup(page, 'html.parser')
        main_table = soup.find('table', class_='CSSTableGenerator')
        table_data = soup.find_all('tr')[1]
        play_time = table_data.select('td')[6].text
        score = table_data.select('td')[8].text
        warnings = table_data.select('td')[7].text
        chart_script = soup.find_all('script')[-1]
        teams.append({
            'number': number,
            'name': name,
            'play_time': play_time,
            'score': score,
            'warnings': warnings,
            'main_table': main_table,
            'chart_script': str(chart_script).replace('chart_div', 'chart_div_' + number),
        })
    teams = sorted(teams, key=lambda team: team['score'], reverse=True)
    return render_template('index.html', team_path=TEAM_PATH, teams=teams)
