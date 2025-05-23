# Raspberry Pi Quiz Sistemi

Bu repo, Raspberry Pi üzerinde çalışan, ESP32 tabanlı kablosuz oyuncu cihazlarıyla entegre bilgi yarışması (quiz) sistemini içerir.

## Özellikler
- 4 adet ESP32 tabanlı kablosuz oyuncu cihazı
- Soru ve kategoriler için SQLite veritabanı
- Web tabanlı yönetici paneli
- Resim, ses ve video destekli sorular
- WebSocket üzerinden güvenli, şifreli iletişim
- Otomatik kurulum scripti
- Donanım bağlantı şeması ve ayrıntılı kullanım kılavuzları

## Klasör Yapısı
```
backend/      - Raspberry Pi ana makine kodları (Flask, veritabanı, API)
esp32/        - ESP32 oyuncu cihazı kodları
scripts/      - Otomatik kurulum ve ek scriptler
docs/         - Kurulum ve kullanım dökümanları, şemalar
```

## Hızlı Başlangıç
1. `scripts/install.sh` dosyasını çalıştırarak sistemi otomatik kurun.
2. Web arayüzüne erişin, sorularınızı ve kategorilerinizi oluşturun.
3. ESP32 cihazlarını programlayıp donanım bağlantılarını yapın.
4. Oynamaya başlayın!

---

Tüm dökümantasyon ve örnekler için `docs/` klasörüne bakınız.
