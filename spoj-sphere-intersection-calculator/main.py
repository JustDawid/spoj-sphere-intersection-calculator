import math
import random

def main():
    for i in range(1, 6):
        print(f"Przykład {i}")
        i += 1 
        r = float(random.randint(1, 2000))
        d = float(random.randint(1, 200))
        wynik = pole_przeciecia(r,d)
        wynik = round(wynik, 2)
        print(f"""Dla sfer o promieniu r: {r} i odległości d: {d}.
Pole koła, którego okrąg jest przecięciem tych dwóch identycznych sfer wynosi {wynik} """)     

def pole_przeciecia(r, d):

    if d > 2*r:
        return False
    elif d == 2*r:
        return False
    R = math.sqrt(r**2 - (d / 2)**2)
    P = math.pi * R**2
    return P

main()