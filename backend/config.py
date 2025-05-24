import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'quizpi-secret-key'
    DATABASE = os.path.join(os.path.dirname(__file__), "db", "quiz.db")
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "static", "uploads")
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100 MB
