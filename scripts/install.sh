#!/bin/bash

set -e

echo "Quiz Sistemi Otomatik Kurulum Başlatılıyor..."

# Sistem güncellemeleri
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y python3 python3-pip python3-venv sqlite3 git

# Proje klasörüne geç
cd "$(dirname "$0")/.." # scripts dizininden projenin köküne çık

# Backend ayarları
cd backend

# Sanal ortam oluştur ve etkinleştir
python3 -m venv venv
source venv/bin/activate

# Gereksinimleri yükle
pip install --upgrade pip
pip install -r requirements.txt

# Veritabanı ve uploads klasörü oluştur
mkdir -p db static/uploads
if [ ! -f db/quiz.db ]; then
    python3 init_db.py
fi

echo "Kurulum tamamlandı!"
echo "Çalıştırmak için:"
echo "source venv/bin/activate && python3 app.py"
