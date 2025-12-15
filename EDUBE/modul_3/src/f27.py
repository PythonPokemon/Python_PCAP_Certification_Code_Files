"""
Inheritance – why and how?
Objekte stellen sich selbst vor (__str__ / __repr__)

-----------------------------------------------------------
Problem: Standard-Ausgabe von Objekten
-----------------------------------------------------------
Wenn du ein Objekt direkt mit print() ausgibst und die Klasse
KEINE spezielle Methode dafür definiert, zeigt Python nur:

<__main__.Klassenname object at 0x...>

• Das ist die Standard-Repräsentation eines Objekts
• Die Hex-Zahl ist nur eine interne Speicheradresse
• Für Menschen ist diese Ausgabe kaum hilfreich

-----------------------------------------------------------
Warum passiert das?
-----------------------------------------------------------
Weil Python intern eine Methode aufruft, um ein Objekt in eine
Zeichenkette umzuwandeln. Ist keine eigene Definition vorhanden,
verwendet Python die Standard-Implementierung der Basisklasse „object“.

-----------------------------------------------------------
Lösung (kommt gleich im nächsten Abschnitt):
-----------------------------------------------------------
Man definiert spezielle Methoden wie:
• __str__()   → menschenlesbare Darstellung
• __repr__() → technische / Entwickler-Darstellung

Ohne diese Methoden sieht die Ausgabe so aus wie unten gezeigt.

🔎 Merke (PCAP/PCPP-wichtig):
Solange keine __str__- oder __repr__-Methode definiert ist,
zeigt Python nur Klasse + Speicheradresse an.
"""

class Stern:
    def __init__(self, name, galaxie):
        self.name = name                              # Name des Sterns speichern
        self.galaxie = galaxie                        # Name der Galaxie speichern


sonne = Stern("Sonne", "Milchstraße")                # Objekt der Klasse erzeugen
print(sonne)                                         # Standard-Ausgabe ohne __str__()
