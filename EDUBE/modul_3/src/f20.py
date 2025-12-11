"""
Methoden im Detail: Fortsetzung – Der Konstruktor (__init__)

Wenn eine Methode in einer Klasse den Namen __init__ trägt,
handelt es sich nicht um eine normale Methode, sondern um
den *Konstruktor* der Klasse.

-----------------------------------------------------------
Was macht der Konstruktor?
-----------------------------------------------------------
• Er wird **automatisch** ausgeführt, sobald ein Objekt erstellt wird.
• Er muss mindestens einen Parameter besitzen → self
• Er kann weitere Parameter haben (zur Initialisierung).
• Er richtet das Objekt ein:
    - Instanzvariablen anlegen
    - Startwerte setzen
    - andere Objekte erstellen, wenn nötig

-----------------------------------------------------------
Wichtige Regeln:
-----------------------------------------------------------
1) __init__ darf **nichts zurückgeben**  
   (kein return-Wert erlaubt, außer implizit None)

2) Der Konstruktor kann nicht manuell aufgerufen werden,
   sondern nur über die Objekterstellung:

       objekt = Klasse(parameter)

3) Die Art der Objekterzeugung muss der Signatur von __init__
   entsprechen (also gleiche Anzahl von Parametern).

-----------------------------------------------------------
Beispiel unten:
-----------------------------------------------------------
• Die Klasse besitzt einen Konstruktor mit dem Parameter „wert“.
• Der Konstruktor legt eine Instanzvariable self.wert an.
• Beim Erstellen des Objekts wird der Konstruktor automatisch ausgeführt.
• Das Objekt zeigt anschließend den gespeicherten Wert an.

Erwartete Ausgabe:
    objekt
"""

class Klasse:
    def __init__(self, wert):                        # Konstruktor mit einem zusätzlichen Parameter
        self.wert = wert                             # Instanzvariable anlegen und speichern

objekt_1 = Klasse("objekt")                          # Konstruktor wird automatisch aufgerufen

print(objekt_1.wert)                                 # zeigt: objekt
