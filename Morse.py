from machine import Pin
from time import sleep_ms

pin = Pin("LED", Pin.OUT)

zprava = input("Zadej zpravu: ")


for i in range(len(zprava)):
    if zprava[i] == ".":
        pin.on()
        sleep_ms(100)
        pin.off()
        sleep_ms(100)
    elif zprava[i] == "-":
        pin.on()
        sleep_ms(300)
        pin.off()
        sleep_ms(100)
    elif zprava[i] == " ":
        sleep_ms(300)
    else:
        print("Chyba")
        break