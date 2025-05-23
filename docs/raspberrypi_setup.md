# Raspberry Pi İşletim Sistemi ve Wi-Fi AP Kurulumu

## 1. Raspberry Pi OS Kurulumu
- Raspberry Pi Imager ile "Raspberry Pi OS Lite" yükleyin.
- SSH ile bağlanın veya doğrudan ekrandan erişin.

## 2. Wi-Fi Access Point (AP) Modu
- `sudo apt-get install hostapd dnsmasq`
- `/etc/hostapd/hostapd.conf` dosyasını şöyle oluşturun:
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
- `/etc/dhcpcd.conf` ve `/etc/network/interfaces` ile statik IP ayarlayın.
- `sudo systemctl enable hostapd`
- Raspberry Pi'yi yeniden başlatın.
