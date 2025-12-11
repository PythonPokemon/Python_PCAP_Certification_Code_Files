"""
Methoden im Detail: Fortsetzung

Methoden und Konstruktoren (__init__) sind ganz normale Funktionen,
nur dass sie innerhalb einer Klasse definiert werden. Deshalb gelten
für sie dieselben Regeln wie für Funktionen:

-----------------------------------------------------------
1) Konstruktoren können Standardargumente besitzen
-----------------------------------------------------------
Wenn ein Parameter im Konstruktor einen Standardwert hat, kann
das Objekt mit oder ohne Argument erzeugt werden.

Beispiel:
    def __init__(self, wert = None):

So kann man das Objekt auf zwei Arten erstellen:
    Klasse("abc")
    Klasse()

Erwartete Ausgabe des Beispiels:
    objekt
    None

-----------------------------------------------------------
2) Name-Mangling wirkt auch auf Methodennamen
-----------------------------------------------------------
Wenn eine Methode mit zwei Unterstrichen beginnt, z. B.:

    def __versteckt(self):

wird der Name intern verändert zu:
    _Klassenname__versteckt

• Die Methode ist damit nicht direkt über obj.__versteckt() aufrufbar.
• Der Aufruf über den gemangelten Namen funktioniert aber weiterhin.

Erwartete Ausgabe des Beispiels:
    sichtbar
    fehlgeschlagen
    versteckt

-----------------------------------------------------------
Wichtig:
-----------------------------------------------------------
„Private“ Methoden sind in Python NICHT wirklich privat.
Name-Mangling dient eher zur Vermeidung von Namenskonflikten.

"""

# ---------------------------------------------------------
# Beispiel 1: Konstruktor mit Standardwert
# ---------------------------------------------------------
class Klasse:
    def __init__(self, wert = None):                 # Standardwert definieren
        self.wert = wert                             # Instanzvariable speichern


objekt_1 = Klasse("objekt")                          # Konstruktor mit Argument
objekt_2 = Klasse()                                  # Konstruktor ohne Argument → wert = None

print(objekt_1.wert)                                 # Ausgabe: objekt
print(objekt_2.wert)                                 # Ausgabe: None



# ---------------------------------------------------------
# Beispiel 2: Versteckte Methoden (Name-Mangling)
# ---------------------------------------------------------
class KlasseMitVersteckterMethode:
    def sichtbar(self):                              # normale Methode
        print("sichtbar")

    def __versteckt(self):                           # „private“ Methode → Name-Mangling
        print("versteckt")


obj = KlasseMitVersteckterMethode()
obj.sichtbar()                                       # funktioniert immer

# direkter Aufruf der versteckten Methode → Fehler
try:
    obj.__versteckt()                                # Name existiert so nicht
except:
    print("fehlgeschlagen")                          # bestätigt das Name-Mangling

# Aufruf über den gemangelten Namen
obj._KlasseMitVersteckterMethode__versteckt()        # funktioniert → zeigt "versteckt"
