"""
Überprüfung der Existenz eines Attributs: Fortsetzung

Wenn ein Objekt ein bestimmtes Attribut NICHT besitzt, löst Python beim
Zugriff eine AttributeError-Ausnahme aus. Um das zu vermeiden, gibt es
zwei übliche Vorgehensweisen:

-----------------------------------------------------------
1) Ausnahmebehandlung (try / except)
-----------------------------------------------------------
Man versucht, auf das Attribut zuzugreifen, und fängt den Fehler ab.
Dieser Ansatz „versteckt“ das Problem jedoch nur – er prüft nicht
wirklich, ob das Attribut existiert.

Beispiel:
    try:
        print(objekt.b)
    except AttributeError:
        pass

-----------------------------------------------------------
2) Attributprüfung mit hasattr()
-----------------------------------------------------------
Python bietet die Funktion hasattr(objekt, 'name_des_attributs').

Wichtig:
• Das zweite Argument ist eine Zeichenkette mit dem Attributnamen.
• Die Funktion gibt True oder False zurück.
• Dadurch kann man sicher prüfen, OB ein Attribut existiert.

Beispiel:
    if hasattr(objekt, 'b'):
        print(objekt.b)

-----------------------------------------------------------
Warum ist hasattr() besser?
-----------------------------------------------------------
• Der Code wird klarer.
• Fehler werden nicht „unterdrückt“, sondern vermieden.
• Der Programmfluss bleibt verständlicher und sauberer.

"""

class BeispielKlasse:
    def __init__(self, wert):
        if wert % 2 != 0:
            self.a = 1                                # Attribut a existiert nur bei ungeraden Zahlen
        else:
            self.b = 1                                # Attribut b existiert nur bei geraden Zahlen


objekt = BeispielKlasse(1)                            # erzeugt nur das Attribut a
print(objekt.a)                                       # funktioniert

# -------------------------------------------------------
# Methode 1: try/except (nicht ideal, aber möglich)
# -------------------------------------------------------
try:
    print(objekt.b)                                   # führt zu AttributeError
except AttributeError:
    pass                                               # Fehler wird „geschluckt“

# -------------------------------------------------------
# Methode 2: hasattr() → saubere Attributprüfung
# -------------------------------------------------------
if hasattr(objekt, 'b'):                              # prüft sicher, ob 'b' existiert
    print(objekt.b)
