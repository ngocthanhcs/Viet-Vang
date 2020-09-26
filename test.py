from flask import Flask, render_template, url_for, redirect
from flask_mysqldb import MySQL
import requests, json, yaml

app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)
    
@app.route('/')
def home():
    cur = mysql.connection.cursor()
    results = cur.execute("SELECT * FROM vv_table")
    if results > 0:
        data = cur.fetchall()
        return render_template('home.html', data = data)

@app.route('/insert')
def insert_data():
    cur = mysql.connection.cursor()

    res = requests.get("http://data.fixer.io/api/latest?access_key=0cf7e4582cfe4e7de960de93c6c4bf9a")
    data = json.loads(res.content)
    data = data["rates"]

    for k,v in data.items():
        cur.execute("INSERT INTO vv_table(name, value_1, value_2) VALUES(%s, %s, %s)",(k, v, v+10.0002))
        mysql.connection.commit()
    cur.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)