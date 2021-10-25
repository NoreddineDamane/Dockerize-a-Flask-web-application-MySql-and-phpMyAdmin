from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def mois_saison() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'odd'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM mois_saison')
    results = [{mois: saison} for (mois, saison) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'mois_saison': mois_saison()})


if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
