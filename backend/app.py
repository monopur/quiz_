import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, jsonify
from flask_socketio import SocketIO, emit
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
socketio = SocketIO(app, cors_allowed_origins="*")

def get_db():
    conn = sqlite3.connect(app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

# Basit kategori ekle/sil/görüntüle
@app.route("/categories", methods=["GET", "POST"])
def categories():
    db = get_db()
    if request.method == "POST":
        name = request.form["name"]
        db.execute("INSERT INTO categories (name) VALUES (?)", (name,))
        db.commit()
    categories = db.execute("SELECT * FROM categories").fetchall()
    return render_template("categories.html", categories=categories)

# Websocket ile ESP32 oyuncu bağlantısı
@socketio.on("connect_player")
def on_connect_player(data):
    emit("player_connected", {"status": "ok"}, broadcast=True)

@socketio.on("player_answer")
def on_player_answer(data):
    emit("answer_update", data, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
