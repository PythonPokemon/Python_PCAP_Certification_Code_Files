"""
Ein kurzer Blick auf Closures (Schließungen)
Funktionen mit gespeichertem Kontext

-----------------------------------------------------------
Was ist eine Closure?
-----------------------------------------------------------
Eine Closure (Schließung) ist eine Funktion, die sich
**Werte aus ihrem ursprünglichen Entstehungskontext merkt**,
auch wenn dieser Kontext eigentlich schon beendet ist.

Kurz gesagt:
• Eine innere Funktion merkt sich Variablen der äußeren Funktion
• Diese Variablen bleiben erhalten
• Auch NACHDEM die äußere Funktion fertig ist

-----------------------------------------------------------
Warum ist das besonders?
-----------------------------------------------------------
Normalerweise gelten:
• Lokale Variablen existieren NUR während des Funktionsaufrufs
• Danach sind sie nicht mehr erreichbar

Closures durchbrechen genau das:
→ Werte bleiben „eingefroren“ im Funktionsobjekt erhalten.

-----------------------------------------------------------
Beispiel aus der Aufgabe
-----------------------------------------------------------
"""
def outer(par):
    loc = par                              # lokale Variable der äußeren Funktion

    def inner():
        return loc                         # nutzt Variable aus outer()

    return inner                           # Rückgabe der inneren Funktion


var = 1
fun = outer(var)                           # outer() ist beendet
print(fun())                               # inner() greift trotzdem auf loc zu



"""
-----------------------------------------------------------
Was passiert hier?
-----------------------------------------------------------
1) outer(var) wird aufgerufen
   • par = 1
   • loc = 1

2) inner() wird definiert
   • benutzt die Variable loc aus outer()

3) outer() gibt inner() zurück
   • outer() endet
   • loc existiert eigentlich nicht mehr

4) ABER:
   • inner() merkt sich loc
   • dieser Wert wird im Funktionsobjekt gespeichert

5) fun() ruft inner() auf
   • Zugriff auf gespeichertes loc → Ausgabe: 1

Die zurückgegebene Funktion ist eine **Closure**.

-----------------------------------------------------------
⚠️ WICHTIG FÜR AUFGABEN / PRÜFUNG (EDUBE / PCAP)
-----------------------------------------------------------
• Eine Closure entsteht, wenn:
  - eine Funktion IN einer anderen definiert ist
  - die innere Funktion Variablen der äußeren nutzt
• Die äußere Funktion muss NICHT mehr aktiv sein
• Die Werte bleiben im Funktionsobjekt gespeichert

-----------------------------------------------------------
Typische Prüfungsfallen:
-----------------------------------------------------------
• print(loc) außerhalb von outer() → NameError
• Closures speichern WERTE, nicht den ganzen Scope
• Jede Closure hat ihren EIGENEN gespeicherten Zustand

-----------------------------------------------------------
Merke:
-----------------------------------------------------------
Closures = Funktionen mit Gedächtnis.
Sie behalten Werte aus ihrem Entstehungskontext,
auch wenn dieser längst beendet ist.
"""
