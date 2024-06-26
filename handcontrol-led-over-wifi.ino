

#include <WiFi.h>

// Network credentials
const char* ssid = "U+Net564C";
const char* pass = "93121#06J8";

// Create an instance of the server, specify the port to listen on as 80
WiFiServer server(80);

void setup() {
  Serial.begin(115200);
  pinMode(5, OUTPUT);  // LED pin set as output

  // Connecting to a WiFi network
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, pass);

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  // Once connected, print the IP address
  Serial.println("\nWiFi connected.");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  // Start the server
  server.begin();
}

void loop() {
  // Check if a client has connected
  WiFiClient client = server.available();
  if (client) {
    Serial.println("New Client.");
    // An incoming request ends with a newline character
    String currentLine = "";
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        Serial.write(c);
        if (c == '\n') {
          // Check if the current line is blank
          if (currentLine.length() == 0) {
            sendHttpResponse(client);
            break;  // Exit the while loop
          } else {
            currentLine = "";
          }
        } else if (c != '\r') {
          currentLine += c;  // Add the character to the current line
        }

        // Check for specific commands from the client
        checkForCommand(currentLine);
      }
    }
    // Close the connection
    client.stop();
    Serial.println("Client Disconnected.");
  }
}

void sendHttpResponse(WiFiClient &client) {
  // HTTP headers
  client.println("HTTP/1.1 200 OK");
  client.println("Content-type:text/html");
  client.println();

  // Web page content
  client.println("<!DOCTYPE html><html>");
  client.println("<body><h1>ESP32 LED Control</h1>");
  client.println("<p><a href=\"/H\">Turn On LED</a></p>");
  client.println("<p><a href=\"/L\">Turn Off LED</a></p>");
  client.println("</body></html>");

  // The HTTP response ends with another blank line
  client.println();
}

void checkForCommand(const String &line) {
  if (line.endsWith("GET /H")) {
    digitalWrite(5, HIGH);  // Turn the LED on
  } else if (line.endsWith("GET /L")) {
    digitalWrite(5, LOW);   // Turn the LED off
  }
}
