# QuizPi Yardım ve Kullanım Rehberi

Bu klasör, QuizPi projesinin kurulum, kullanım, soru aktarım, ESP32 ve Raspberry Pi işlemleri hakkında kapsamlı yardım dosyalarını içerir.

---

## İçindekiler

- [Kurulum ve İlk Başlangıç](#kurulum-ve-ilk-başlangıç)
- [Kullanım Kılavuzu](#kullanım-kılavuzu)
- [Soru Yükleme Yöntemleri](#soru-yükleme-yöntemleri)
- [PowerPoint ile Soru Aktarma](#powerpoint-ile-soru-aktarma)
- [CSV ile Soru Aktarma](#csv-ile-soru-aktarma)
- [ESP32 Buton Sistemi](#esp32-buton-sistemi)
- [Donanım Gereksinimleri ve Bağlantılar](donanim-yardim.md)
- [Sık Sorulan Sorular & İpuçları](#sık-sorulan-sorular--ipuçları)

---

## Kurulum ve İlk Başlangıç

### Raspberry Pi Otomatik Kurulum

1. Raspberry Pi OS (Lite veya Desktop) kurulu olmalıdır.
2. Terminal açın ve şu komutları çalıştırın:
   ```bash
   git clone https://github.com/SENINKLONUN/quizpi.git
   cd quizpi/scripts
   bash install_on_rpi.sh
   bash start_server.sh
   ```
3. Web arayüzüne Pi'nin IP adresi üzerinden `http://<RPI_IP>:5000` ile erişebilirsiniz.

---

## Kullanım Kılavuzu

- Web panelinde kategori, takım, oyuncu ve soru yönetimi yapılabilir.
- Her soru için resim, ses, video ekleyebilirsiniz.
- Soru eklerken dilerseniz elle, dilerseniz toplu PowerPoint/CSV ile aktarım yapabilirsiniz.
- Takımlara oyuncu atayabilir, isim ve renklerini düzenleyebilirsiniz.

---

## Soru Yükleme Yöntemleri

QuizPi, iki ana yöntemle toplu soru yüklemeyi destekler:

### 1. PowerPoint ile Soru Aktarma

- Her slayt bir soru olacak şekilde sunum hazırlayın.
- Notlar kısmına şu formatta bilgi ekleyin:
  ```
  Doğru: A
  Kategori: Matematik
  Zorluk: Kolay
  ```
- Medya eklemek için slayta resim, ses veya video ekleyebilirsiniz.
- Sistemde "PowerPoint'ten Aktar" menüsünden .pptx dosyanızı yükleyin.
- Aktarımdan sonra sonuç/hata raporu görüntülenir.

Detaylı bilgi için: [powerpoint_kullanim_rehberi.txt](powerpoint_kullanim_rehberi.txt)

### 2. CSV ile Soru Aktarma

- CSV dosyanız aşağıdaki başlıkları içermelidir:
  ```
  category_id, question_text, option_a, option_b, option_c, option_d, correct_option, difficulty, points, duration
  ```
- Dosyanızı "CSV ile Aktar" bölümünden yükleyin.
- Medya dosyalarını aynı dizine koyup ZIP ile yükleyebilirsiniz.

---

## ESP32 Buton Sistemi

- Her ESP32, benzersiz bir oyuncu ID’si ile sisteme bağlanır.
- Butona basıldığında cevaplar web paneline anında iletilir.
- Pil seviyesi ve bağlantı durumu izlenebilir.

Donanım ve yazılım detayları için: [donanim-yardim.md](donanim-yardim.md) ve [esp32_baglanti_rehberi.txt](../esp32_baglanti_rehberi.txt)

---

## Sık Sorulan Sorular & İpuçları

**S: Soru yüklerken hata alıyorum, ne yapmalıyım?**  
C: Dosya formatınızı ve notlar kısmındaki bilgileri kontrol edin. Dosya ve başlıklar eksiksiz olmalı.

**S: ESP32 bağlanmıyor, neden?**  
C: Wi-Fi ayarlarını, IP adresini ve sunucu bağlantısını kontrol edin. Her ESP32'ye farklı bir ID verin.

**S: Medya dosyam açılmıyor?**  
C: Desteklenen dosya formatlarını (resim: jpg/png, ses: mp3/wav, video: mp4) kullanın ve dosya boyutunu kontrol edin.

**S: Sistemi nasıl güncellerim?**  
C: Repo güncellemeleri için:
   ```bash
   git pull
   bash install_on_rpi.sh
   ```

---

Daha fazla bilgi ve donanım bağlantı detayları için [donanim-yardim.md](donanim-yardim.md) dosyasına göz atabilirsiniz.
