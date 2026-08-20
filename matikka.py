print("hello")
# helppo komento

import math

# Vaihdettu int -> float, jotta voit antaa esim. 5.5
a = float(input("Anna ympyrän säde: "))
print("a =", a)
ympyränpinta = math.pi * ((a) ** 2)

# Tulostetaan tulos kahden desimaalin tarkkuudella
print("Ympyrän pinta-ala on:", round(ympyränpinta, 2))

if ympyränpinta < 50:
    print("Pinta-ala on alle 50")
elif ympyränpinta == 50:
    print("Pinta-ala on tasan 50")
else:
    print("Pinta-ala on yli 50")
    