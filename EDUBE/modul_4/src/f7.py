"""
Mehr zu Listenverständnissen
Bedingte Ausdrücke (conditional expressions)

-----------------------------------------------------------
Was ist ein bedingter Ausdruck?
-----------------------------------------------------------
Ein Ausdruck, der abhängig von einer Bedingung
EINEN von ZWEI Werten zurückgibt.

Syntax:
    wert_wenn_true  if  bedingung  else  wert_wenn_false

⚠️ WICHTIG:
• Das ist KEINE if-Anweisung, sondern ein Ausdruck!
• Er liefert IMMER genau einen Wert zurück.
• Ideal einsetzbar in Listenverständnissen.

-----------------------------------------------------------
Beispiel ohne Comprehension
-----------------------------------------------------------
Wir bauen eine Liste aus 0 und 1:
• x gerade  → 1
• x ungerade → 0
"""

liste = []                                      # Ergebnisliste erzeugen

for zahl in range(10):                          # 0..9
    liste.append(1 if zahl % 2 == 0 else 0)     # bedingter Ausdruck

print(liste)                                    # Ausgabe: [1,0,1,0,1,0,1,0,1,0]



"""
-----------------------------------------------------------
⚠️ WICHTIG FÜR AUFGABEN / PRÜFUNG (EDUBE / PCAP)
-----------------------------------------------------------
• Der Ausdruck wird IMMER ausgewertet → er liefert einen Wert.
• Er kann überall stehen, wo ein normaler Wert stehen darf.
• Typische Aufgabenfalle:
  „Warum funktioniert das ohne if-Anweisung?“
   → Weil es ein Ausdruck ist, kein Statement.

-----------------------------------------------------------
Typische Anwendung:
-----------------------------------------------------------
Listenverständnisse mit Bedingungen, z. B.:

[1 if x % 2 == 0 else 0 for x in range(10)]
→ erzeugt dieselbe Liste wie oben, aber kompakter.
"""
