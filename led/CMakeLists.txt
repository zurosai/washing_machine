add_executable(led
        led.c
        test.c
)

target_include_directories(led
        PRIVATE
        ../include
)

target_link_libraries(led pico_stdlib hardware_gpio hardware_adc)

pico_enable_stdio_usb(led 1)
pico_enable_stdio_uart(led 0)

pico_add_extra_outputs(led)