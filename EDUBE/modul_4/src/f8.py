"""
Mehr zu Listenverständnissen – Generatoren vs. Listen

-----------------------------------------------------------
Kompaktheit & Eleganz
-----------------------------------------------------------
Listenverständnisse (list comprehensions) sind kompakte,
ausdrucksstarke Konstrukte, die Listen direkt erzeugen.

Beispiel:
    [1 if x % 2 == 0 else 0 for x in range(10)]

-----------------------------------------------------------
Generatoren – enge Verbindung zu Comprehensions
-----------------------------------------------------------
Ein Generator sieht FAST genauso aus wie ein Listenverständnis.

Der EINZIGE Unterschied:
• LISTE      → eckige Klammern  [...]
• GENERATOR  → runde Klammern   (...)

Beispiel:
    liste      = [1 if x % 2 == 0 else 0 for x in range(10)]
    generator  = (1 if x % 2 == 0 else 0 for x in range(10))

-----------------------------------------------------------
Wichtigster Unterschied
-----------------------------------------------------------
LISTE:
• erzeugt SOFORT alle Elemente
• liegt vollständig im Speicher vor
• len(liste) funktioniert

GENERATOR:
• erzeugt Werte LAZY – immer nur beim Abruf
• spart Speicher
• len(generator) löst aus:
      TypeError: object of type 'generator' has no len()

-----------------------------------------------------------
Beispielausgabe
-----------------------------------------------------------
Beide Schleifen drucken dieselben Zahlen:
1 0 1 0 1 0 1 0 1 0
1 0 1 0 1 0 1 0 1 0

⚠️ ABER:
• obere Zeile → echte Liste wird vollständig erzeugt
• untere Zeile → Werte entstehen erst beim Iterieren

-----------------------------------------------------------
Prüfungsrelevante Hinweise (PCAP)
-----------------------------------------------------------
• Generatoren sparen Speicher → ideal für große Datenmengen
• list(generator) erzwingt Auswertung → Generator wird „verbraucht“
• Unterschied der Klammern gehört zu den klassischen Fangfragen
• len() funktioniert nur bei Listen, NIE bei Generatoren

-----------------------------------------------------------
Merke:
Eckige Klammern = Liste
Runde Klammern  = Generator
"""

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]   # echte Liste
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))  # Generator

print(the_list)                                           # komplette Liste vorhanden
