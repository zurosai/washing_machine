# washing_machine

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

Recommendations:
Consider using a more descriptive naming convention for pins (e.g., ROTARY_LED_PIN_A, SELECTION_LED_PIN).
If pin assignments are configurable, provide comments on how to modify these definitions.

Rotary LED Library (crotary_led.h)

Purpose: Provides functions for controlling the rotary LED display.
Details:
PINS_SIZE: Defines the constant size of the pins array.
pins: Declares a static array of uint32_t to store the digital pin assignments for the seven-segment LED.
rl_mask: Declares a static uint32_t variable to hold the bit mask representing the active LED(s).
rl_delay: Defines the constant delay (in milliseconds) between reading the potentiometer and updating the LED.
rl_construct(const int a[]): Initializes the pins array with the provided pin assignments.
rl_init(): Initializes the digital pins for the rotary LED as outputs and initializes the analog pin for potentiometer reading.
rl_read_value(): Reads the analog value from the potentiometer and converts it to a bit mask representing the active LED(s).
rl_turn_led_on(): Turns on the LED(s) determined by the rl_mask value.
rl_clear(): Turns off all LEDs in the rotary display.
rotary_led(): Calls rl_read_value to determine the active LED(s), turns them on, delays briefly, and then turns them off.
Recommendations:
Provide clear comments for each function explaining its purpose and parameters.
Consider adding error handling for invalid pin values in rl_construct.
Document the expected input range for the potentiometer in rl_read_value.
LED and Switch Control (led.c)

Purpose: Implements functionalities for LED and switch control.
Details:
rl_construct, rl_init, rl_read_value, rl_turn_led_on, and rl_clear are included from crotary_led.h.
rotary_led(): Calls rl_read_value to determine the active LED(s), turns them on, delays briefly, and then turns them off. Prints debug messages based on the read value.
Recommendations:
Move the implementation of rotary_led from led.c to crotary_led.c for better organization.
Consider using a lookup table or conditional statements instead of debug messages in rotary_led for more production-ready code.
Main Program (test.c)

Purpose: The main program that controls the overall system behavior.
Details:
led_state: Stores the state (on/off) of the selection indicator LED.
is_paused: Flags whether the rotary LED function is paused.
blink_state: Controls blinking behavior of the selection indicator LED.
system_on: Flags whether the system is powered on.
main(): Performs the following:
Initializes LED and switch pins with appropriate directions and pull-up resistors.
Initializes rotary LED pins and ADC.
Enters an infinite loop that continuously reads switch states and performs actions based on them.
System power control: Toggles system_on on power button press.
Selection LED
