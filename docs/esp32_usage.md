# ESP32 Programlama ve Donanım Bağlantı Şeması

## Programlama
- Arduino IDE veya PlatformIO kullanın.
- Gerekli kütüphaneler:
  - WiFi, WebSocketsClient, Adafruit_SSD1306
- Kodda SSID, şifre ve sunucu IP'sini güncelleyin.
- ESP32'yi bilgisayara bağlayıp yükleyin.

## Donanım Bağlantısı
- OLED ekran: SDA - GPIO21, SCL - GPIO22
- Buton: GPIO13 (INPUT_PULLUP)
- LED: GPIO12 (OUTPUT)
- Batarya: 3.7V LiPo veya 18650
- Devreyi breadboard ile kurun.
