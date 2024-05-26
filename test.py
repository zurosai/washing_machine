from machine import UART, Pin, I2C
from ssd1306 import SSD1306_I2C

# Configuración del bus 12c
i2c = I2C(id=0, scl=Pin(17), sda=Pin(16), freq=400000)

# Configuración OLED
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

# Configuración UART
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

while True:
    oled.fill(0)
    oled.text(data, 0, 0)
    oled.show()

    if uart.any():
        # Lee datos recibidos por UART
        data = uart.read()
        if data:
            oled.fill(0)
            oled.text(data, 0, 0)
            oled.show
            print("Recibido:", data)
