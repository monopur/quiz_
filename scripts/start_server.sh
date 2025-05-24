#!/bin/bash
# QuizPi Flask Sunucusunu Başlatır

cd "$(dirname "$0")/../backend"
export FLASK_APP=app.py
export FLASK_ENV=production
flask run --host=0.0.0.0 --port=5000
