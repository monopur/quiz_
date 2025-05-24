# QuizPi: Raspberry Pi & ESP32 Tabanlı Akıllı Quiz Sistemi

Tamamen açık kaynak, kolay kurulan, öğretmen/yarışma sunucusu dostu, medya destekli, Raspberry Pi üzerinde çalışan ve ESP32 tabanlı kablosuz butonlarla oynanabilen quiz yarışma platformu.

---

## İçindekiler

- [Kısa Özellik Listesi](#kısa-özellik-listesi)
- [Hızlı Kurulum (Raspberry Pi)](#hızlı-kurulum-raspberry-pi)
- [Web Paneli Kullanımı](#web-paneli-kullanımı)
- [Soru Aktarım Yöntemleri](#soru-aktarım-yöntemleri)
  - [PowerPoint ile Aktarım](#powerpoint-ile-aktarım)
  - [CSV ile Aktarım](#csv-ile-aktarım)
- [ESP32 Buton Sistemi](#esp32-buton-sistemi)
- [ESP32 Donanım Bağlantı Rehberi](#esp32-donanım-bağlantı-rehberi)
- [Katkı ve Lisans](#katkı-ve-lisans)

---

## Kısa Özellik Listesi

- Modern Flask tabanlı backend ve Bootstrap tabanlı admin paneli
- Soruya resim, ses, video ekleyebilme
- PowerPoint (.pptx) veya CSV ile toplu aktarım, notlardan kategori/cevap/zorluk otomatik okuma
- Takım ve oyuncu yönetimi, renk ve isim atama
- Sorulara puan ve zaman tanımlama
- Anında medya yükleme ve oynatma
- Raspberry Pi'da otomatik kurulum scripti
- ESP32 ile kablosuz buton desteği
- Kolayca genişletilebilir açık kaynak yapı

---

## Hızlı Kurulum (Raspberry Pi)

### 1. Raspberry Pi Hazırlığı

- Raspberry Pi OS Lite (32/64bit) önerilir.
- İnternete bağlı olduğunuzdan emin olun.
- Terminal açın ve aşağıdaki komutları çalıştırın:

```bash
git clone https://github.com/SENINKLONUN/quizpi.git
cd quizpi/scripts
bash install_on_rpi.sh
bash start_server.sh
```

- Web paneline erişmek için:  
  `http://raspberrypi.local:5000` veya `http://<RPI_IP_ADRESI>:5000`

### 2. (Opsiyonel) Manuel Kurulum

Gerekirse `backend/requirements.txt` içindeki Python kütüphanelerini elle kurabilirsiniz.

---

## Web Paneli Kullanımı

Panelde;
- Kategori/Soru/Takım/Oyuncu ekleyebilir, silebilir, düzenleyebilirsiniz.
- Soru eklerken resim, ses, video yükleyebilirsiniz.
- Menüden toplu aktarım (PowerPoint/CSV) seçebilirsiniz.

---

## Soru Aktarım Yöntemleri

### PowerPoint ile Aktarım

1. **PowerPoint’te her slayta soru, medya ve notlar ekleyin:**
   - Soru metni ve medya slaytta açıkça olmalı.
   - *Notlar bölümüne:*  
     ```
     Doğru: A
     Kategori: Matematik
     Zorluk: Kolay
     ```
2. Dosyanızı `.pptx` olarak kaydedin.
3. Web panelde "PowerPoint'ten Aktar" menüsüne girin, dosyanızı yükleyin.
4. Sonuç ekranında başarılı/eksik slaytları/hataları görebilirsiniz.

**Detaylı rehber için:**  
`backend/tools/powerpoint_kullanim_rehberi.txt`

---

### CSV ile Aktarım

- CSV örnek dosyası:
  | category_id | question_text | image_path | audio_path | video_path | option_a | option_b | option_c | option_d | correct_option | difficulty | points | duration |
  |-------------|--------------|------------|------------|------------|----------|----------|----------|----------|----------------|------------|--------|----------|

- Medya dosyalarını aynı anda ZIP ile yükleyebilirsiniz.

---

## ESP32 Buton Sistemi

- Her butonlu ESP32 cihazı benzersiz ID ile sisteme bağlanır.
- Butona basıldığında cevap paneline anında düşer.
- Pil seviyesi, bağlantı durumu ve cevaplar canlı izlenebilir.

**Donanım bağlantısı ve pin detayları için:**  
`esp32_baglanti_rehberi.txt`

---

## ESP32 Donanım Bağlantı Rehberi

Ayrıntılı bağlantı ve devre şeması için `esp32_baglanti_rehberi.txt` dosyasına bakınız.

---

## Katkı ve Lisans

- Katkı sağlamak isteyenler için örnek issue ve PR şablonları eklidir.
- MIT Lisansı ile açık kaynak.

---

#### Proje Sahibi: [SeninAdın]
#### Her türlü öneri, geliştirme ve katkı için PR veya issue açabilirsiniz!
