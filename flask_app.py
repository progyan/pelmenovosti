from flask import Flask, request, session, jsonify, send_from_directory, redirect
from flask.templating import render_template
from markupsafe import escape
from flask_cors import CORS
import psycopg2
import sys

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4sdffgQ8z\n\xec]/'
CORS(app)

@app.route("/news")
def news_list():
    with psycopg2.connect(dbname='database', user='yanb', 
            password='terrayan', host='localhost') as con:
        cur = con.cursor()
        cur.execute('SELECT creator, title, text, type, id FROM news;')
        #return jsonify(_news)
        return jsonify(cur.fetchall())

@app.post("/addnews")
def add_news():
    with psycopg2.connect(dbname='database', user='yanb', 
            password='terrayan', host='localhost') as con:
        cur = con.cursor()
        cur.execute('INSERT INTO news (creator, title, text, type) VALUES (%s, %s, %s, %s);',
                request.json)
        con.commit()
        #_news.append(request.json)
        return jsonify("OK")

@app.route("/deletenews/<int:id>")
def delete_news(id):
    with psycopg2.connect(dbname='database', user='yanb', 
            password='terrayan', host='localhost') as con:
        cur = con.cursor()
        cur.execute('DELETE FROM news WHERE id = %s;', (id,))
        con.commit()
        #_news.append(request.json)
        return jsonify("OK")

@app.post("/login")
def login():
    if request.json[0] == "Пельмень" and request.json[1] == "п":
        session['username'] = request.json[0]
        return jsonify("OK")
    elif request.json[0] == "Бойстул" and request.json[1] == "б":
        session['username'] = request.json[0]
        return jsonify("OK")
    elif request.json[0] == "Ян" and request.json[1] == "я":
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

#app.run()