#include <WiFi.h>
#include <WebSocketsClient.h>
#include <Adafruit_SSD1306.h>
#include <Wire.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET    -1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

const char* ssid = "QuizAP";
const char* password = "quizpass";
const char* host = "192.168.4.1"; // Raspberry Pi'nin AP IP adresi
const uint16_t port = 5000;

WebSocketsClient webSocket;

#define BUTTON_PIN  13
#define LED_PIN     12

void showStatus(const char* msg) {
  display.clearDisplay();
  display.setTextSize(1); display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println(msg);
  display.display();
}

void webSocketEvent(WStype_t type, uint8_t * payload, size_t length) {
  switch(type) {
    case WStype_CONNECTED:
      showStatus("Baglandi!");
      break;
    case WStype_DISCONNECTED:
      showStatus("Baglanti koptu!");
      break;
    case WStype_TEXT:
      // Gelen mesajı işleyin
      break;
    default:
      break;
  }
}

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);

  Serial.begin(115200);
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  showStatus("WiFi Baglaniyor...");

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    showStatus("WiFi bekleniyor...");
  }
  showStatus("WebSocket baglan...");
  webSocket.begin(host, port, "/socket.io/?EIO=4&transport=websocket");
  webSocket.onEvent(webSocketEvent);
}

void loop() {
  webSocket.loop();
  if (digitalRead(BUTTON_PIN) == LOW) {
    webSocket.sendTXT("{\"event\":\"player_answer\",\"answer\":\"A\"}");
    digitalWrite(LED_PIN, HIGH);
    delay(200);
    digitalWrite(LED_PIN, LOW);
  }
}
