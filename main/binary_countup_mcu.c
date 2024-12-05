#include <stdio.h>
#include <stdbool.h>
#include <unistd.h>
#include "driver/gpio.h"

#define LED_PIN_0 0  // GPIO pin for bit 0
#define LED_PIN_1 1  // GPIO pin for bit 1
#define LED_PIN_2 2  // GPIO pin for bit 2
#define LED_PIN_3 3  // GPIO pin for bit 3

void app_main(void)
{
    // Configure GPIO pins as output
    gpio_set_direction(LED_PIN_0, GPIO_MODE_OUTPUT);
    gpio_set_direction(LED_PIN_1, GPIO_MODE_OUTPUT);
    gpio_set_direction(LED_PIN_2, GPIO_MODE_OUTPUT);
    gpio_set_direction(LED_PIN_3, GPIO_MODE_OUTPUT);

    while (true) {
        for (int i = 0; i <= 12; i++) {
            // Set GPIO pin levels based on the current number in binary
            gpio_set_level(LED_PIN_0, (i >> 0) & 1);  // Bit 0
            gpio_set_level(LED_PIN_1, (i >> 1) & 1);  // Bit 1
            gpio_set_level(LED_PIN_2, (i >> 2) & 1);  // Bit 2
            gpio_set_level(LED_PIN_3, (i >> 3) & 1);  // Bit 3

            printf("Counting: %d\n", i);  // Print current count
            sleep(1);  // Wait for 1 second
        }
    }
}
