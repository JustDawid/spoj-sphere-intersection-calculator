# Obliczanie Pola Przekroju Dwóch Sfer (ETI06F1)

## Opis
Projekt jest symulacją rozwiązania problemu algorytmicznego [SPOJ ETI06F1](https://pl.spoj.com/problems/ETI06F1/).
Skrypt generuje losowe przypadki testowe dla dwóch identycznych sfer o promieniu $r$, oddalonych od siebie o odległość $d$, a następnie oblicza pole powierzchni koła, które powstaje w wyniku ich przecięcia.

## Matematyka rozwiązania
Problem sprowadza się do znalezienia promienia koła $R$, które powstaje na styku sfer. Wykorzystujemy **Twierdzenie Pitagorasa** na trójkącie prostokątnym utworzonym przez:
1.  Promień sfery ($r$) - przeciwprostokątna.
2.  Połowę odległości między środkami sfer ($d/2$) - przyprostokątna.
3.  Promień szukanego przekroju ($R$) - przyprostokątna.

**Wzór:**
$$R = \sqrt{r^2 - (\frac{d}{2})^2}$$

Pole przekroju to standardowe pole koła:
$$P = \pi \cdot R^2$$

## Uruchomienie
Wymagany Python 3.

```bash
python main.py
