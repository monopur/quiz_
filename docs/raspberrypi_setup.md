# Raspberry Pi İşletim Sistemi ve Wi-Fi AP Kurulumu

## 1. Raspberry Pi OS Kurulumu

- Raspberry Pi Imager ile "Raspberry Pi OS Lite" veya "Desktop" sürümü yükleyin.
- SD kartı yerleştirip cihazı başlatın.
- SSH ile veya HDMI ekran ve klavye ile erişebilirsiniz.

## 2. Wi-Fi Access Point (AP) Modu

1. Gerekli paketleri yükleyin:
   ```bash
   sudo apt-get update
   sudo apt-get install hostapd dnsmasq
   ```
2. `/etc/hostapd/hostapd.conf` dosyasını oluşturun:
   ```
   interface=wlan0
   ssid=QuizAP
   hw_mode=g
   channel=7
   wmm_enabled=0
   macaddr_acl=0
   auth_algs=1
   ignore_broadcast_ssid=0
   wpa=2
   wpa_passphrase=quizpass
   wpa_key_mgmt=WPA-PSK
   wpa_pairwise=TKIP
   rsn_pairwise=CCMP
   ```
3. Statik IP ayarlayın:
   - `/etc/dhcpcd.conf` ve gerekirse `/etc/network/interfaces` dosyalarını düzenleyin.
4. Servisi etkinleştirin ve yeniden başlatın:
   ```bash
   sudo systemctl enable hostapd
   sudo systemctl start hostapd
   sudo reboot
   ```

## 3. Sorun Giderme

- Wi-Fi görünmüyorsa konfigürasyonu ve donanımı kontrol edin.
- SSH ile erişim için `ssh` dosyasını boot dizinine ekleyebilirsiniz.

Daha fazla donanım ve kurulum ayrıntısı için: [donanim-yardim.md](donanim-yardim.md)
