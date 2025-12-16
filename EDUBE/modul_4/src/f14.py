"""
Ein kurzer Blick auf Closures (Schließungen)
Closures mit Parametern – veränderbares Verhalten

-----------------------------------------------------------
Was wird hier erweitert?
-----------------------------------------------------------
Im vorherigen Beispiel war die innere Funktion **parameterlos**.
Jetzt sehen wir eine wichtigere Variante:

• Die innere Funktion kann EIGENE Parameter haben
• Zusätzlich nutzt sie weiterhin gespeicherte Werte
  aus der äußeren Funktion

→ Eine Closure kann also:
  - gespeicherte Werte verwenden
  - UND neue Werte von außen annehmen

-----------------------------------------------------------
Grundidee dieses Beispiels
-----------------------------------------------------------
Wir bauen eine Funktion, die andere Funktionen erzeugt.

Diese erzeugten Funktionen:
• merken sich einen festen Wert (loc)
• führen mit diesem Wert eine Berechnung aus
• können mehrfach und unabhängig voneinander existieren

-----------------------------------------------------------
Beispiel aus der Aufgabe
-----------------------------------------------------------
"""
def make_closure(par):
    loc = par                              # gespeicherter (eingefrorener) Wert

    def power(p):                          # innere Funktion mit Parameter
        return p ** loc                   # nutzt p UND loc

    return power                           # Rückgabe der Closure


fsqr = make_closure(2)                    # loc = 2  → quadrieren
fcub = make_closure(3)                    # loc = 3  → hoch 3

for i in range(5):
    print(i, fsqr(i), fcub(i))



"""
-----------------------------------------------------------
Was passiert hier?
-----------------------------------------------------------
1) make_closure(2)
   • loc = 2 wird gespeichert
   • fsqr(p) berechnet p ** 2

2) make_closure(3)
   • loc = 3 wird gespeichert
   • fcub(p) berechnet p ** 3

3) Beide Closures existieren parallel
   • gleicher Code
   • unterschiedlicher gespeicherter Zustand

Ausgabe:
0 0 0
1 1 1
2 4 8
3 9 27
4 16 64

-----------------------------------------------------------
⚠️ WICHTIG FÜR AUFGABEN / PRÜFUNG (EDUBE / PCAP)
-----------------------------------------------------------
• Jede Closure hat ihren EIGENEN gespeicherten Wert
• Der gespeicherte Wert stammt aus der äußeren Funktion
• Die innere Funktion kann zusätzlich eigene Parameter haben
• Closures werden wie normale Funktionen aufgerufen

-----------------------------------------------------------
Typische Prüfungsfallen:
-----------------------------------------------------------
• make_closure(2) wird NICHT sofort ausgeführt
  → es wird eine Funktion zurückgegeben
• fsqr und fcub teilen sich KEINEN Zustand
• Der gespeicherte Wert ändert sich nicht von selbst

-----------------------------------------------------------
Merke:
-----------------------------------------------------------
Closures sind Funktions-Fabriken:
Gleicher Code – unterschiedliches Verhalten
durch gespeicherte (eingefrorene) Werte.
"""
