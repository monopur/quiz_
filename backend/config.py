import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "gizli-anahtar")
    DATABASE = os.path.join(os.path.dirname(__file__), "db", "quiz.db")
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "static", "uploads")
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "mp3", "wav", "mp4"}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
