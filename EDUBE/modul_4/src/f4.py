"""
Generatoren – die Rolle von `yield`
Warum `yield` Iteratoren ersetzt (PCAP-relevant)

-----------------------------------------------------------
Problem mit dem klassischen Iterator-Protokoll
-----------------------------------------------------------
Ein manueller Iterator (mit __iter__ und __next__) muss:

• den kompletten Zustand selbst speichern  
  → z. B. Index, letzte Fibonacci-Werte  
• bei jedem __next__() manuell aktualisieren  
• StopIteration selbst auslösen

Das führt zu:
• viel Code
• schwerer zu lesen
• fehleranfällig

Beispiel: Die Klasse Fib musste 5 Variablen speichern (__n, __i, __p1, __p2).

-----------------------------------------------------------
Warum `yield` dieses Problem löst
-----------------------------------------------------------
Eine Funktion mit `yield` wird nicht normal ausgeführt.

Stattdessen wird sie zu einem **Generator**, der:

• den kompletten Ausführungszustand automatisch speichert  
• bei jedem `yield` „pausiert“  
• beim nächsten Durchlauf genau dort weitermacht  
• die StopIteration automatisch erzeugt, wenn die Funktion endet

🔎 Merke:
`yield` = **return + Pause + Speicher des gesamten Funktionszustands**

-----------------------------------------------------------
Wichtiges Prinzip:
-----------------------------------------------------------
Eine Funktion mit `return` liefert EINEN Wert und beendet sich sofort.

Eine Funktion mit `yield` liefert MEHRERE Werte nacheinander  
und beendet sich erst, wenn der Code vollständig abgearbeitet ist.

-----------------------------------------------------------
Warum diese Funktion KEIN Generator ist:
-----------------------------------------------------------

def fun(n):
    for i in range(n):
        return i

• return beendet die Funktion beim ersten Durchlauf  
• Zustand geht verloren  
• nicht iterierbar

-----------------------------------------------------------
Kleine Änderung – große Wirkung:
-----------------------------------------------------------
"""

def fun(n):
    for i in range(n):
        yield i



"""
Durch das Ersetzen von `return` → `yield` wird die Funktion:

• ein Generator  
• speichert den Schleifenzustand  
• erzeugt Zahlen nacheinander

-----------------------------------------------------------
Wie man einen Generator benutzt
-----------------------------------------------------------
"""

for v in fun(5):
    print(v)



"""
-----------------------------------------------------------
PCAP-Prüfungsfalle:
-----------------------------------------------------------
1) Eine Funktion **mit yield wird NIE normal aufgerufen**,  
   sondern liefert ein Generatorobjekt:

g = fun(5)
print(g)   → <generator object fun at 0x...>

2) Man MUSS darüber iterieren:
   - mit for
   - oder mit next(g)

3) Eine Funktion darf NICHT gleichzeitig return und yield
   sinnvoll mischen (return ohne Wert beendet den Generator).

-----------------------------------------------------------
Merksatz:
yield macht Iteratoren automatisch.
Ohne __iter__ und __next__ selbst schreiben zu müssen.
"""
