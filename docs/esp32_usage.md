# ESP32 Programlama ve Donanım Bağlantı Şeması

## Programlama

- Arduino IDE veya PlatformIO kullanılabilir.
- Gerekli kütüphaneler:
  - WiFi
  - WebSocketsClient
  - Adafruit_SSD1306 (OLED için)
- Kodda SSID, şifre ve sunucu IP'sini güncelleyin.
- Her ESP32'ye benzersiz bir oyuncu/cihaz ID'si tanımlayın.
- ESP32'yi bilgisayara bağlayıp kodu yükleyin.

## Donanım Bağlantısı

| Bağlantı  | ESP32 Pin | Açıklama         |
|-----------|-----------|------------------|
| OLED SDA  | GPIO21    | I2C veri         |
| OLED SCL  | GPIO22    | I2C saat         |
| Buton     | GPIO13    | INPUT_PULLUP     |
| LED       | GPIO12    | OUTPUT           |
| Batarya   | VIN/3V3   | 3.7V LiPo/18650  |

- Devreyi breadboard veya lehimli şekilde kurabilirsiniz.
- Pil kullanıyorsanız koruma devresi önerilir.

## İpuçları

- Kod değişikliği sonrası yeniden yüklemeyi unutmayın.
- Bağlantı koparsa cihaz otomatik olarak tekrar bağlanır.
- OLED ekranda bağlantı ve takım bilgisi görüntülenir.

Daha detaylı donanım için: [donanim-yardim.md](donanim-yardim.md)
