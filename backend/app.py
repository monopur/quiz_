import os
import sqlite3
import csv
from io import TextIOWrapper
from flask import (
    Flask, render_template, request, redirect, url_for,
    send_from_directory, jsonify
)
from flask_socketio import SocketIO, emit
from werkzeug.utils import secure_filename
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

@app.route("/uploads/<path:filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

# Kategoriler
@app.route("/categories", methods=["GET", "POST"])
def categories():
    db = get_db()
    if request.method == "POST":
        name = request.form["name"]
        db.execute("INSERT INTO categories (name) VALUES (?)", (name,))
        db.commit()
    categories = db.execute("SELECT * FROM categories").fetchall()
    return render_template("categories.html", categories=categories)

# Takımlar
@app.route("/teams", methods=["GET", "POST"])
def teams():
    db = get_db()
    if request.method == "POST":
        name = request.form["name"]
        color = request.form.get("color", "#000000")
        db.execute("INSERT INTO teams (name, color) VALUES (?, ?)", (name, color))
        db.commit()
    teams = db.execute("SELECT * FROM teams").fetchall()
    return render_template("teams.html", teams=teams)

# Oyuncu yönetimi
@app.route("/players/manage", methods=["GET", "POST"])
def manage_players():
    db = get_db()
    if request.method == "POST":
        player_id = request.form["player_id"]
        team_id = request.form["team_id"]
        db.execute("UPDATE players SET team_id=? WHERE id=?", (team_id, player_id))
        db.commit()
    players = db.execute("SELECT * FROM players").fetchall()
    teams = db.execute("SELECT * FROM teams").fetchall()
    return render_template("manage_players.html", players=players, teams=teams)

# Sorular listesi (basit)
@app.route("/questions")
def questions():
    db = get_db()
    questions = db.execute("SELECT * FROM questions").fetchall()
    categories = db.execute("SELECT * FROM categories").fetchall()
    return render_template("questions.html", questions=questions, categories=categories)

# Soru ekleme
@app.route("/questions/new", methods=["GET", "POST"])
def new_question():
    db = get_db()
    if request.method == "POST":
        category_id = request.form["category_id"]
        question_text = request.form["question_text"]
        option_a = request.form["option_a"]
        option_b = request.form["option_b"]
        option_c = request.form["option_c"]
        option_d = request.form["option_d"]
        correct_option = request.form["correct_option"]
        difficulty = request.form.get("difficulty", "orta")
        points = request.form.get("points", 10)
        duration = request.form.get("duration", 20)
        # Medya dosyalarını kaydet
        image_path, audio_path, video_path = None, None, None
        for field, upload_dir in [("image", "img"), ("audio", "audio"), ("video", "video")]:
            file = request.files.get(field)
            if file and file.filename:
                filename = secure_filename(file.filename)
                folder = os.path.join(app.config["UPLOAD_FOLDER"], upload_dir)
                os.makedirs(folder, exist_ok=True)
                path = os.path.join(folder, filename)
                file.save(path)
                if field == "image":
                    image_path = f"{upload_dir}/{filename}"
                elif field == "audio":
                    audio_path = f"{upload_dir}/{filename}"
                elif field == "video":
                    video_path = f"{upload_dir}/{filename}"
        db.execute(
            """INSERT INTO questions (category_id, question_text, image_path, audio_path, video_path, option_a, option_b, option_c, option_d, correct_option, difficulty, points, duration)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (category_id, question_text, image_path, audio_path, video_path, option_a, option_b, option_c, option_d, correct_option, difficulty, points, duration)
        )
        db.commit()
        return redirect(url_for("questions"))
    categories = db.execute("SELECT * FROM categories").fetchall()
    return render_template("question_form.html", categories=categories)

# Soruları CSV ile toplu yükleme
@app.route("/questions/import", methods=["GET", "POST"])
def import_questions():
    db = get_db()
    if request.method == "POST":
        file = request.files["csvfile"]
        reader = csv.DictReader(TextIOWrapper(file, "utf-8"))
        for row in reader:
            db.execute(
                """INSERT INTO questions (category_id, question_text, option_a, option_b, option_c, option_d, correct_option, difficulty, points, duration)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    row["category_id"], row["question_text"],
                    row["option_a"], row["option_b"], row["option_c"], row["option_d"],
                    row["correct_option"], row.get("difficulty", "orta"),
                    row.get("points", 10), row.get("duration", 20)
                )
            )
        db.commit()
        return redirect(url_for("questions"))
    return render_template("import_questions.html")

# Websocket ile ESP32 oyuncu bağlantısı
@socketio.on("connect_player")
def on_connect_player(data):
    emit("player_connected", {"status": "ok"}, broadcast=True)

@socketio.on("player_answer")
def on_player_answer(data):
    emit("answer_update", data, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
