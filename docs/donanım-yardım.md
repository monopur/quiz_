# QuizPi Donanım Gereksinimleri ve Bağlantı Rehberi

## 1. Sunucu: Raspberry Pi Gereksinimleri

| Bileşen        | Minimum | Önerilen   |
|----------------|---------|------------|
| Model          | Pi 3B   | Pi 4 (2GB+)|
| Güç Adaptörü   | 2A      | 3A         |
| SD Kart        | 8GB     | 16GB+      |
| WiFi           | Dahili  | Dahili     |

- Raspberry Pi OS (Lite veya Desktop) önerilir.
- Kablolu veya kablosuz ağ bağlantısı kullanılabilir.

## 2. Kablosuz Butonlar için ESP32 Gereksinimleri

- ESP32 DevKitC veya NodeMCU kartı (her oyuncu için 1 adet)
- Tactile Button (her kart için 1 adet)
- 3.7V LiPo pil veya 18650 pil (isteğe bağlı portatif kullanım için)
- (Opsiyonel) OLED Ekran (I2C: SSD1306)

## 3. ESP32 Buton Bağlantı Şeması

```
ESP32 GPIO Pinleri:
- Buton:    GPIO13 (INPUT_PULLUP)
- LED:      GPIO12 (OUTPUT)
- OLED SDA: GPIO21
- OLED SCL: GPIO22
```

Tablo:
| Bağlantı       | ESP32 Pin | Açıklama         |
|----------------|-----------|------------------|
| Buton          | GPIO13    | INPUT_PULLUP     |
| LED            | GPIO12    | OUTPUT           |
| OLED SDA       | GPIO21    | I2C veri         |
| OLED SCL       | GPIO22    | I2C saat         |

## 4. Donanım Özellikleri & Önerileri

- Tüm ESP32'ler aynı WiFi ağına ve sunucu IP'sine bağlanmalıdır.
- Her ESP32 için farklı `player_id` atanmalıdır.
- 3D baskı veya kutu ile korumalı bir buton kutusu önerilir.
- Pil koruma devresi önerilir.

## 5. Toplu Donanım Listesi

| Ürün            | Adet      | Notlar           |
|-----------------|-----------|------------------|
| Raspberry Pi    | 1         | Sunucu           |
| SD Kart         | 1         | 16GB+            |
| ESP32           | 4-8       | Oyuncu sayısına göre |
| Buton           | 4-8       |                  |
| LED             | 4-8       |                  |
| OLED Ekran      | 4-8       | Opsiyonel        |
| Pil             | 4-8       | Opsiyonel        |
| Kablo/Breadboard| Yeterli   |                  |

## 6. Kaynaklar ve Yazılım

- [ESP32 Arduino Kodu](../esp32/quiz_button.ino)
- [Raspberry Pi Kurulum Scripti](../scripts/install_on_rpi.sh)
- Yazılım ve entegrasyon için docs/README.md ve diğer yardım dosyalarını inceleyin.
