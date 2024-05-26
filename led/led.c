#include <stdio.h>
#include <stdlib.h>
#include "pico/stdlib.h"
#include "pin_list.h"
#include "crotaryled.h"
#include "hardware/adc.h"


void rl_construct(const int a[]) 
  {
      for (int i=0; i<PINS_SIZE-1; i++) 
        {
            pins[i] = a[i];
        }
      rl_mask = 0;
  }

void rl_init() 
  {
      // Initializes digital output for rotary LEDs
      for (int i = 0; i < PINS_SIZE; i++) 
        {
            gpio_init(pins[i]);
            gpio_set_dir(pins[i], GPIO_OUT);
        }

      // Initializes analog input for the micro switch
      adc_init();
      adc_gpio_init(ANALOG_PIN);
      adc_select_input(0);
  }

uint32_t rl_read_value() 
  {
      uint16_t analog_read = adc_read();
      uint16_t pin = (analog_read > 3410) ? 5
                    : (analog_read > 2728) ? 4
                    : (analog_read > 2046) ? 3
                    : (analog_read > 1364) ? 2
                    : (analog_read > 682) ? 1
                    : 0;
      rl_mask = 1 << pins[pin];
      return rl_mask;
  }

void rl_turn_led_on() 
  {
      gpio_set_mask(rl_mask);
  }

void rl_clear() 
  {
      gpio_clr_mask(rl_mask);
  }

void rotary_led()
  {
    uint32_t val = rl_read_value();
                
    if(val==256)
      //printf("Delicado\n");
      uart_puts(UART_ID, "Ciclo delicado");
    if(val==1024)
      //printf("Blanco\n");
      uart_puts(UART_ID, "Ropa blanca");
    if(val==2097152)
      //printf("Pesado\n");
      uart_puts(UART_ID, "Carga pesada");
    if(val==131072)
      //printf("Normal\n");
      uart_puts(UART_ID, "Lavado normal");
    if(val==65536)
      //printf("Rápido\n");
      uart_puts(UART_ID, "Ciclo rapido");
    if(val==2048)
      //printf("Color\n");
      uart_puts(UART_ID, "Ropa de color");
    
    rl_turn_led_on();
    sleep_ms(rl_delay);
    rl_clear();
  }
