"""
Strings vs. Numbers
Manchmal müssen Zahlen in Strings umgewandelt werden (z.B. für Ausgaben)
oder Strings in Zahlen (z.B. für Berechnungen).

1) Zahl → String
   Dies funktioniert immer.
   Dafür verwendet man die Funktion str():
"""
itg = 13
flt = 1.3
si = str(itg)     # int -> string
sf = str(flt)     # float -> string

print(si + ' ' + sf)   # Ausgabe: 13 1.3
print()


"""
2) String → Zahl
   Dies ist nur möglich, wenn der String eine gültige Zahl enthält.
   Falls nicht, entsteht ein ValueError.

   • int()  wandelt in eine ganze Zahl um
   • float() wandelt in eine Dezimalzahl um
"""
si = '13'
sf = '1.3'
itg = int(si)      # string -> int
flt = float(sf)    # string -> float

print(itg + flt)   # Ausgabe: 14.3
