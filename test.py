from machine import UART, Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep
import socket

# Configuración del bus 12c
i2c = I2C(id=0, scl=Pin(17), sda=Pin(16), freq=400000)

# Configuración OLED
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

# Configuración UART
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

data = ""
response2 = ""

def test_wifi() -> None:
    import network
    ssid = 'INFINITUME850_2.4'
    password = 'liGyaaCk3B'
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print('Waiting for connection...')
        sleep(1)
    print('Connected to Internet!')
    print('IP address:', wlan.ifconfig()[0])

test_wifi()
#sleep(1)

def send_message_to_server(message):
    global response2
    host = '192.168.1.65'  # IP del servidor
    port = 12345  # Puerto del servidor

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        client_socket.sendall(message.encode())
        response = client_socket.recv(1024).decode()
        print(f"Mensaje del servidor: {response}")
        response2 = response
    except Exception as e:
        print(f"Error communicating with the server: {e}")
    finally:
        client_socket.close()

def divide_in_paragraphs(text, length):
    paragraphs = []
    for i in range(0, len(text), length):
        paragraphs.append(text[i:i+length])
    return paragraphs


while True:

    oled.fill(0)
    oled.text("Wi-Fi conectado", 0, 0)
    oled.text(data, 32, 10)
    oled.text("Timer ", 0, 20)
    paragraphs = divide_in_paragraphs(response2, 16)
    for idx, para in enumerate(paragraphs[:3]):  # Solo muestra hasta 3 párrafos
        oled.text(para, 0, 30 + idx * 10)
    oled.show()
    oled.show()
   
    
    if uart.any():
        # Lee datos recibidos por UART
        data = uart.read().decode()
        msg = data
        print("Recibido desde UART: ", msg)
        send_message_to_server(msg)
        print("Cadena recibida: ", response2)
        
        if response2:
            oled.fill(0)
            oled.text("Wi-Fi conectado", 0, 0)
            oled.text(data, 32, 10)
            oled.text("Timer ", 0, 20)
            paragraphs = divide_in_paragraphs(response2, 16)
            for idx, para in enumerate(paragraphs[:3]):  # Solo muestra hasta 3 párrafos
                oled.text(para, 0, 30 + idx * 10)
            oled.show()
           
    sleep(0.1)
