#!/usr/bin/env python3
###
### read MCP3002 ADC analog value via RasPi SPI
###

import wiringpi as wp
import time



def main():
    # SPI channle (0 or 1)
    SPI_CH = 0

    # pin base (above 64)
    PIN_BASE=70

    # GPIO number
    LED_PIN = 25

    # threshold
    THRESHOLD = 200

    # setup
    wp.mcp3002Setup (PIN_BASE, SPI_CH)
    wp.wiringPiSetupGpio()
    wp.pinMode(LED_PIN, wp.GPIO.OUTPUT)

    # if a sensor value is over THRESHOLD,
    # flash led.
    while True:
        value = wp.analogRead(PIN_BASE)
        print (value)

        if value > THRESHOLD:
          wp.digitalWrite(LED_PIN, wp.GPIO.HIGH)
          time.sleep(0.2)
          wp.digitalWrite(LED_PIN, wp.GPIO.LOW)
          time.sleep(0.2)

        time.sleep(0.1)


if __name__ == "__main__":
    main()
