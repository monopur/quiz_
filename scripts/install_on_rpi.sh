#!/bin/bash
# QuizPi Raspberry Pi Otomatik Kurulum Scripti

set -e

echo "Sistem güncelleniyor..."
sudo apt-get update && sudo apt-get upgrade -y

echo "Gerekli paketler kuruluyor..."
sudo apt-get install -y python3 python3-pip git sqlite3

echo "Python kütüphaneleri kuruluyor..."
cd "$(dirname "$0")/../backend"
pip3 install --upgrade pip
pip3 install -r requirements.txt

echo "Veritabanı başlatılıyor..."
python3 init_db.py

echo "Kurulum tamamlandı! Sunucu başlatmak için scripts/start_server.sh çalıştırın."
