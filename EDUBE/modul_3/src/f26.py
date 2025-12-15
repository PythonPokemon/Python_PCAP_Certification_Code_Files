"""
Investigating Classes – Klassen untersuchen (Reflection & Introspection)
-----------------------------------------------------

In Python kann man Klassen und Objekte **zur Laufzeit untersuchen und verändern**.
Das nennt man:

• Introspection  → Eigenschaften eines Objekts herausfinden
• Reflection     → Eigenschaften eines Objekts gezielt verändern

Python erlaubt beides vollständig.

-----------------------------------------------------
Ziel dieses Beispiels
-----------------------------------------------------
Wir schreiben eine Funktion, die:

• EIN beliebiges Objekt erhält
• alle Attribute dieses Objekts durchsucht
• nur Attribute betrachtet,
    – deren Name mit dem Buchstaben "i" beginnt
    – deren Wert vom Typ int ist
• und diese Integer-Werte um 1 erhöht

-----------------------------------------------------
Wichtige Werkzeuge dabei
-----------------------------------------------------
• obj.__dict__        → enthält alle Attribute des Objekts
• name.startswith()  → prüft, ob ein Name mit einem Buchstaben beginnt
• getattr(obj, name) → liest den aktuellen Wert eines Attributs
• isinstance(val, int) → prüft, ob der Wert ein Integer ist
• setattr(obj, name, neuer_wert) → setzt einen neuen Wert

-----------------------------------------------------
Erwartete Ausgabe:
-----------------------------------------------------
Vorher:
{'a': 1, 'integer': 4, 'b': 2, 'i': 3, 'z': 5, 'ireal': 3.5}

Nachher:
{'a': 1, 'integer': 5, 'b': 2, 'i': 4, 'z': 5, 'ireal': 3.5}

Nur:
• i
• integer
wurden erhöht (beide int + beginnen mit "i")
"""

# ---------------------------------------------------
# Beispielklasse (leer)
# ---------------------------------------------------
class MeineKlasse:
    pass                                            # leere Klasse


# ---------------------------------------------------
# Objekt erzeugen und Attribute dynamisch hinzufügen
# ---------------------------------------------------
objekt = MeineKlasse()

objekt.a = 1                                        # kein i → bleibt gleich
objekt.b = 2                                        # kein i → bleibt gleich
objekt.i = 3                                        # beginnt mit i + int → wird erhöht
objekt.ireal = 3.5                                  # beginnt mit i, aber float → bleibt gleich
objekt.integer = 4                                  # beginnt mit i + int → wird erhöht
objekt.z = 5                                        # kein i → bleibt gleich


# ---------------------------------------------------
# Funktion zur automatischen Attribut-Manipulation
# ---------------------------------------------------
def erhoehe_ints_mit_i(obj):
    for name in obj.__dict__.keys():                 # alle Attributnamen durchgehen
        if name.startswith('i'):                     # nur Namen mit "i"
            wert = getattr(obj, name)                # aktuellen Wert holen
            if isinstance(wert, int):                # prüfen: ist es ein Integer?
                setattr(obj, name, wert + 1)         # neuen Wert setzen (alter + 1)


# ---------------------------------------------------
# Test
# ---------------------------------------------------
print(objekt.__dict__)                               # Zustand VOR der Änderung
erhoehe_ints_mit_i(objekt)                           # Funktion anwenden
print(objekt.__dict__)                               # Zustand NACH der Änderung
