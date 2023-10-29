from machine import Pin
from time import sleep_ms

pin = Pin("LED", Pin.OUT)


zprava = input("zadej zpravu:")

print(zprava)
print(len(zprava))
print(range(len(zprava)))

abeceda = ["a","b","c","d","e","f","g","h","ch","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
morseovka = [".-","-...","-.-.","-..",".","..-.","--.","....","----","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."," "]

for i in range(len(zprava)):
  pismeno = zprava[i]
  print(abeceda.index(pismeno))
  pozice = abeceda.index(pismeno)
  print(morseovka[pozice])
  morsenko = (morseovka[pozice])
  print(morsenko)
  for i in range(len(morsenko)):
    if morsenko[i] == ".":
        pin.on()
        sleep_ms(100)
        pin.off()
        sleep_ms(100)
    elif morsenko[i] == "-":
        pin.on()
        sleep_ms(300)
        pin.off()
        sleep_ms(100)
    elif morsenko[i] == " ":
        sleep_ms(300)