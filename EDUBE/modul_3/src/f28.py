"""
Inheritance – why and how?
Objekte schön ausgeben mit __str__()

-----------------------------------------------------------
Was passiert bei print(objekt)?
-----------------------------------------------------------
Wenn ein Objekt an print() übergeben wird, versucht Python:

1) die Methode __str__() des Objekts aufzurufen
2) den von __str__() zurückgegebenen Text auszugeben

Falls KEINE eigene __str__()-Methode existiert:
→ Python nutzt die Standardversion aus der Basisklasse „object“
→ Ausgabe ist technisch und unschön:
   <__main__.Klasse object at 0x...>

-----------------------------------------------------------
Lösung: Eigene __str__()-Methode definieren
-----------------------------------------------------------
• __str__() MUSS eine Zeichenkette (str) zurückgeben
• Sie bestimmt, wie das Objekt für Menschen angezeigt wird
• Sehr wichtig für:
    – Debugging
    – Ausgaben
    – Prüfungen (PCAP / PCPP)

-----------------------------------------------------------
Beispiel unten:
-----------------------------------------------------------
• Die Klasse speichert Name und Galaxie eines Sterns
• __str__() kombiniert beide Informationen zu einem Text
• print(objekt) nutzt automatisch diese Methode

Erwartete Ausgabe:
    Sun in Milky Way

✅ Merksatz (prüfungsrelevant):
print(objekt) → ruft immer objekt.__str__() auf (falls vorhanden)
"""

class Stern:
    def __init__(self, name, galaxie):
        self.name = name                              # Name des Sterns speichern
        self.galaxie = galaxie                        # Name der Galaxie speichern

    def __str__(self):
        return self.name + " in " + self.galaxie      # menschenlesbare Darstellung des Objekts


sonne = Stern("Sun", "Milky Way")                     # Objekt erzeugen
print(sonne)                                         # ruft automatisch __str__() auf
