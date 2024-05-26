#include <stdio.h>
#include <stdlib.h>
#include "pico/stdlib.h"
#include "pin_list.h"
#include "crotaryled.h"
#include "hardware/adc.h"
#include "hardware/uart.h"

// LED states
int led_state = 0; // LED 2 (selection indicator) state variable
int is_paused = 0; // Pause flag
int blink_state = 0; // Blink flag
int system_on = 0; // System state (1:on, 0:off)


int main() 
  {
    // Initialize LED pins
    stdio_init_all();

    gpio_init(LED_PIN_SELECTION);
    gpio_set_dir(LED_PIN_SELECTION, GPIO_OUT);

    gpio_init(LED_PIN_PAUSE);
    gpio_set_dir(LED_PIN_PAUSE, GPIO_OUT);

    gpio_init(LED_PIN_ON_OFF);
    gpio_set_dir(LED_PIN_ON_OFF, GPIO_OUT);

    // Initialize switch pins and pull-up resistors
    gpio_init(SWITCH_PIN_SELECTION);
    gpio_set_dir(SWITCH_PIN_SELECTION, GPIO_IN);
    gpio_pull_up(SWITCH_PIN_SELECTION);

    gpio_init(SWITCH_PIN_PAUSE);
    gpio_set_dir(SWITCH_PIN_PAUSE, GPIO_IN);
    gpio_pull_up(SWITCH_PIN_PAUSE);

    gpio_init(SWITCH_PIN_ON_OFF);
    gpio_set_dir(SWITCH_PIN_ON_OFF, GPIO_IN);
    gpio_pull_up(SWITCH_PIN_ON_OFF);

    // Initialize rotary LED pins and ADC
    int pins[] = {PIN_A, PIN_B, PIN_C, PIN_D, PIN_E, PIN_F, ANALOG_PIN};
    rl_construct(pins);
    rl_init();

    // Inicializa el UART
    uart_init(UART_ID, BAUD_RATE);
    gpio_set_function(UART_TX_PIN, GPIO_FUNC_UART);
    gpio_set_function(UART_RX_PIN, GPIO_FUNC_UART);

    //uart_puts(UART_ID, "Hola, este es un mensaje enviado a traves de una serializacion UART");

    while(true) 
    {
        // Read switch states
        int selection_state = gpio_get(SWITCH_PIN_SELECTION);
        int pause_resume_state = gpio_get(SWITCH_PIN_PAUSE);
        int on_off_state = gpio_get(SWITCH_PIN_ON_OFF);

        // General system switch logic
        if(on_off_state == 0) 
          {
            system_on = !system_on; // System status change
            sleep_ms(250); // Debounce delay
          }

        gpio_put(LED_PIN_ON_OFF, system_on);

        if (uart_is_readable(UART_ID)) 
        {
            char ch = uart_getc(UART_ID);
            uart_putc(UART_ID, ch);
        }

        if(system_on)
          {
          // Selection button press logic
          if(!is_paused) 
            {
              if(selection_state == 0) 
                {
                  blink_state = !blink_state; // Toggle blinking flag on button press
                }
              selection_state = blink_state; // Update LED state based on blinking flag
              gpio_put(LED_PIN_SELECTION, !selection_state);
              sleep_ms(250);
            }

          // Pause button press logic
          if (pause_resume_state == 0) 
            {
              is_paused = !is_paused;
              led_state = is_paused; // Update selection indicator LED state
              gpio_put(LED_PIN_PAUSE, led_state);
              sleep_ms(250);
            }

          if(selection_state) 
            {
              rotary_led(); // Call to rotary_led_function
            }
          }
    }
    return 0;
  }

