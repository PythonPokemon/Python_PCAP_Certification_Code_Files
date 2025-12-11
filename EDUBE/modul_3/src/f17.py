"""
Überprüfung der Existenz eines Attributs: Fortsetzung

Die Funktion hasattr() kann nicht nur Objektattribute prüfen,
sondern auch **Klassenattribute**. Dadurch lässt sich leicht
feststellen, ob eine Klasse eine bestimmte Klassenvariable besitzt.

-----------------------------------------------------------
Wie funktioniert hasattr()?
-----------------------------------------------------------
hasattr(objekt_oder_klasse, 'attributname')

• das zweite Argument ist immer eine Zeichenkette
• Rückgabe: True oder False
• funktioniert für Instanzvariablen UND Klassenvariablen

-----------------------------------------------------------
Beispiel 1: Prüfung von Klassenvariablen
-----------------------------------------------------------

class BeispielKlasse:
    attribut = 1

print(hasattr(BeispielKlasse, 'attribut'))   # True
print(hasattr(BeispielKlasse, 'eigenschaft'))# False

-----------------------------------------------------------
Beispiel 2: Mischung aus Instanz- und Klassenvariablen
-----------------------------------------------------------

class BeispielKlasse:
    a = 1                                     # Klassenvariable

    def __init__(self):
        self.b = 2                            # Instanzvariable


objekt = BeispielKlasse()

Erwartete Ergebnisse:
hasattr(objekt, 'b')        → True   (weil Instanzvariable existiert)
hasattr(objekt, 'a')        → True   (weil Klassenvariable weiterhin sichtbar ist)
hasattr(BeispielKlasse, 'b')→ False  (Klassen besitzen keine Instanzvariablen)
hasattr(BeispielKlasse, 'a')→ True   (Klassenvariable)

-----------------------------------------------------------
Merksatz (PCAP-wichtig):
-----------------------------------------------------------
Objekte sehen Klassenattribute.
Klassen sehen **keine** Objektattribute.
"""

# ---------------------------------------------------------
# Beispiel 1: Klassenvariablen prüfen
# ---------------------------------------------------------
class BeispielKlasse1:
    attribut = 1                                 # Klassenvariable

print(hasattr(BeispielKlasse1, 'attribut'))      # True
print(hasattr(BeispielKlasse1, 'eigenschaft'))   # False


# ---------------------------------------------------------
# Beispiel 2: Klassen- vs. Instanzattribute
# ---------------------------------------------------------
class BeispielKlasse2:
    a = 1                                        # Klassenvariable

    def __init__(self):
        self.b = 2                                # Instanzvariable


objekt = BeispielKlasse2()

print(hasattr(objekt, 'b'))                      # True  → Instanzvariable vorhanden
print(hasattr(objekt, 'a'))                      # True  → Klassenvariable sichtbar
print(hasattr(BeispielKlasse2, 'b'))             # False → Klassen sehen keine Instanzvariablen
print(hasattr(BeispielKlasse2, 'a'))             # True  → Klassenvariable vorhanden
