# washing_machine

**Description**

This code implements a versatile system that controls a rotary LED display and interacts with buttons to provide user control.  The rotary LED display, composed of seven individual segments (A-G), can be manipulated by an analog input, typically a potentiometer. By adjusting the potentiometer, users can influence which segments light up, creating various patterns or numerical displays.

The system also features dedicated buttons for selection, pause/resume, and system power control. The selection button allows users to interact with specific functionalities within the system, potentially changing the behavior of the rotary LED display based on user choices. The pause/resume button provides a way to temporarily halt the updating of the rotary LED display, giving users control over the display's responsiveness. Finally, the system power control button allows users to turn the entire system on or off.

By separating the rotary LED control logic into its own library (crotary_led.h), the code promotes better organization and potential reusability. This modular approach makes the code easier to understand, maintain, and potentially integrate into other projects that require similar rotary LED control functionality. It allows developers to focus on the specific application logic without needing to rewrite the core LED control functions.

<br>
<br>

**Pin Definitions (pin_list.h)**

*Purpose*: Defines constants for pin assignments used throughout the project.

Details:

*PIN_A* to *PIN_G*: Define the digital pins connected to the seven-segment rotary LED display (indices correspond to LED segments A-G).

*ANALOG_PIN*: Defines the analog pin used for reading the potentiometer value.

*LED_PIN_SELECTION*: Defines the digital pin connected to the LED for selection indication.

*SWITCH_PIN_SELECTION*: Defines the digital pin connected to the button for selection control.

*LED_PIN_PAUSE*: Defines the digital pin connected to the LED for pause indication.

*SWITCH_PIN_PAUSE*: Defines the digital pin connected to the button for pausing the rotary LED function.

*SWITCH_PIN_ON_OFF*: Defines the digital pin connected to the button for system power control.

<br>
<br>

**Rotary LED Library (crotary_led.h)**

Purpose: Provides functions for controlling the rotary LED display.

Details:

*PINS_SIZE*: Defines the constant size of the pins array.

*pins*: Declares a static array of uint32_t to store the digital pin assignments for the seven-segment LED.

*rl_mask*: Declares a static uint32_t variable to hold the bit mask representing the active LED(s).

*rl_delay*: Defines the constant delay (in milliseconds) between reading the potentiometer and updating the LED.

*rl_construct(const int a[])*: Initializes the pins array with the provided pin assignments.

*rl_init()*: Initializes the digital pins for the rotary LED as outputs and initializes the analog pin for potentiometer reading.

*rl_read_value()*: Reads the analog value from the potentiometer and converts it to a bit mask representing the active LED(s).

*rl_turn_led_on()*: Turns on the LED(s) determined by the rl_mask value.

*rl_clear()*: Turns off all LEDs in the rotary display.

*rotary_led()*: Calls rl_read_value to determine the active LED(s), turns them on, delays briefly, and then turns them off.

<br>
<br>

**LED and Switch Control (led.c)**

*Purpose*: Implements functionalities for LED and switch control.

Details:

*rl_construct, rl_init, rl_read_value, rl_turn_led_on,* and *rl_clear* are included from crotary_led.h.

*rotary_led()*: Calls rl_read_value to determine the active LED(s), turns them on, delays briefly, and then turns them off. Prints debug messages based on the read value.

<br>
<br>

**Main Program (test.c)**

Purpose: The main program that controls the overall system behavior.

Details:

*led_state*: Stores the state (on/off) of the selection indicator LED.

*is_paused*: Flags whether the rotary LED function is paused.

*blink_state*: Controls blinking behavior of the selection indicator LED.

*system_on*: Flags whether the system is powered on.

*main()*: Performs the following:

Initializes LED and switch pins with appropriate directions and pull-up resistors.

Initializes rotary LED pins and ADC.

Enters an infinite loop that continuously reads switch states and performs actions based on them.

*System power control*: Toggles system_on on power button press.

<br>
<br>

**Required Components**:

Microcontroller Board: - A microcontroller board Raspberry Pi Pico or any board compatible with Pico C/C++ libraries.

Rotary LED Display: - A seven-segment rotary LED display module.

Potentiometer: - A linear potentiometer with a resistance value suitable for your microcontroller's analog input range (e.g., 10kΩ).

Resistors: - Two resistors (values depend on LED forward voltage and desired current) for current limiting on the LEDs.

Jumper Wires: - A set of jumper wires for connecting components.

Breadboard: - A breadboard can be helpful for prototyping and experimenting with the circuit.

LEDs (2-3): - LEDs for selection and pause indication (optional, depending on desired functionality).

Push Buttons (3): - Buttons for selection, pause/resume, and system power control (optional, depending on desired functionality).

OLED Display i2c (128x64): Device used to display the status of the machine.

<br>
<br>

**Diagram**

![Captura de pantalla 2024-05-13 a la(s) 7 44 26 p m](https://github.com/zurosai/washing_machine/assets/169511947/5fed507c-158f-4092-8a83-a9a5a0dfbcaa)

<br>
<br>

# test.py

Functionality

This script demonstrates ESP32 communication with a server over WiFi and displaying information on an OLED display. It is directly related to washing machine output through UART protocol.

<br>
<br>

**Libraries**

_machine_: Provides access to hardware components like I2C, UART, and pins.

_ssd1306_: Controls the OLED display (SSD1306 driver).

_time_: For delays using sleep.

_socket_: Enables network communication using sockets.

<br>
<br>

**Configuration**

Sets up I2C communication for the OLED display.

Defines display dimensions (oled_width and oled_height).

Initializes the OLED display (oled).

Configures UART communication for serial communication.

<br>
<br>

**Functions**

_test_wifi_: Connects the Raspberry Pico to a WiFi network with the specified ssid and password.

_send_message_to_server_: Takes a message, establishes a socket connection to a server at the provided host and port, sends the message, receives a response, and prints it.

_divide_in_paragraphs_: Splits a text string into a list of paragraphs with a maximum length of length characters.

<br>
<br>

**Main Loop**

Continuously clears and updates the OLED display:

  Shows "Wi-Fi conectado" (WiFi connected).
  
  Displays the value of data.
  
  Shows "Timer " (to receive a timer from the Raspberry).
  
  Splits the response2 string (which is initially empty) into paragraphs and displays up to 3 of them.
  
  Checks if there's any data received through UART.
  
    If there's data, reads it into the data variable.
  
  Sends the data to the server using send_message_to_server.
  
  Updates the OLED display with the received and server response data.

<br>
<br>

**Overall Flow**

The script initializes communication with the OLED display and UART.

The main loop continuously:

  Updates the OLED display with static messages and empty data placeholders.
  
  Checks for incoming data on UART.
  
  If data is received on UART:
  
  The data is stored in the data variable.
  
  The data is sent to a server.
  
  The OLED display is updated with the received data and the server's response (if any).

# server.py


![Diagrama sin título drawio](https://github.com/zurosai/washing_machine/assets/169511947/03bfeecf-eab1-4aa9-b249-b774aa60f92f)

**Description**

This code implements a server that receives messages from a client, processes them, and sends a response.

<br>
<br>

**Functionality**

    process_message(message):

Analyzes the received message and returns a response based on the message content.

    start_server():
    
Creates a server socket and configures it to listen on a specific IP address and port.

Accepts incoming connections from clients.

For each connected client:

Receives a message from the client.

Processes the message using the process_message function.

Sends the response to the client.

Closes the connection with the client.

<br>
<br>

**Code Structure**

    process_message(message): 
    
Analyzes the message and returns a response.

    start_server(): 

Creates and runs the server.
    
    Main block (if __name__ == "__main__":):
    
Calls the start_server() function to start the server.

<br>
<br>

**Implementation Details**

Uses the socket library to create sockets and manage network communication.

Defines an IP address (host) and a port (port) for the server.

Sets a limit of one connection at a time (server_socket.listen(1)).

Handles network errors and connection closing.



