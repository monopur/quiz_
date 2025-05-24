#!/bin/bash
# QuizPi Raspberry Pi Otomatik Kurulum Scripti

echo "Sistem güncelleniyor..."
sudo apt-get update && sudo apt-get upgrade -y

echo "Gerekli paketler kuruluyor..."
sudo apt-get install -y python3 python3-pip git sqlite3

echo "Python bağımlılıkları yükleniyor..."
cd ../backend
pip3 install -r requirements.txt

echo "Veritabanı başlatılıyor..."
python3 init_db.py

echo "Kurulum tamamlandı!"
