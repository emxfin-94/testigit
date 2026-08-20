print("hello")
# helppo komento

import math

# Vaihdettu int -> float, jotta voit antaa esim. 5.5
a = float(input("Anna ympyrän säde: "))
print("a =", a)
ympyränpinta = math.pi * ((a) ** 2)

# Tulostetaan tulos kahden desimaalin tarkkuudella
print("Ympyrän pinta-ala on:", round(ympyränpinta, 2))