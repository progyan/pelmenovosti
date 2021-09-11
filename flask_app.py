from flask import Flask, request, session, jsonify, send_from_directory, redirect
from flask.templating import render_template
from markupsafe import escape
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4sdffgQ8z\n\xec]/'
CORS(app)

@app.route("/news")
def news_list():
    with get_connection() as con:
        cur = con.cursor()
        cur.execute('SELECT creator, title, content, news_type, id FROM news;')
        #return jsonify(_news)
        return jsonify(cur.fetchall())

@app.post("/addnews")
def add_news():
    with get_connection() as con:
        cur = con.cursor()
        cur.execute('INSERT INTO news (creator, title, content, news_type) VALUES (%s, %s, %s, %s);',
                request.json)
        con.commit()
        #_news.append(request.json)
        return jsonify("OK")

@app.route("/deletenews/<int:id>")
def delete_news(id):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute('DELETE FROM news WHERE id = %s;', (id,))
        con.commit()
        #_news.append(request.json)
        return jsonify("OK")

@app.post("/login")
def login():
    if request.json[0] == "Пельмень" and request.json[1] == "пельмень21":
        session['username'] = request.json[0]
        return jsonify("OK")
    elif request.json[0] == "Бойстул" and request.json[1] == "байсалбайсогур":
        session['username'] = request.json[0]
        return jsonify("OK")
    elif request.json[0] == "Ян" and request.json[1] == "terrayan1":
        session['username'] = request.json[0]
        return jsonify("OK")
    return jsonify("FAIL")

@app.post("/logout")
def logout():
    session.pop("username")
    return jsonify("OK")

@app.route("/getuser")
def getuser():
    app.logger.debug(session)
    return session.get('username', 'Гость')

@app.route('/pages/<path:path>')
def pages(path):
    return send_from_directory('static', path)

@app.route("/")
def main_page():
    return redirect("/pages/login/index.html")

def get_connection():
    if os.environ.get("ENV") == 'prod':
        # Heroku settings
        app.logger.debug("Database from Heroku")
        return psycopg2.connect(dbname='df3np8aam20708', user='xxheddtkjfbgbk', 
                password='6a8958ddac4956dc14227fe57213ab27be914f5a35f27d16806c9c559fa68029', 
                host='ec2-3-248-103-75.eu-west-1.compute.amazonaws.com', port=5432)
    # return connection to dev server
    return psycopg2.connect(dbname='pelmenovosti', user='pelmenovosti', password='pelmenovosti', 
            host='localhost', port=5432)

#app.run()