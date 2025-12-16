"""
Wie verwendet man Lambdas und wofür?
Anonyme Kurzfunktionen für einmalige Berechnungen

-----------------------------------------------------------
Was ist die Idee dahinter?
-----------------------------------------------------------
Lambdas eignen sich ideal, wenn man **eine Funktion als Argument
übergeben** möchte, diese Funktion aber:
• sehr kurz ist
• nur einmal verwendet wird
• nicht extra als def-Funktion definiert werden soll

Genau das passiert hier: Wir wollen eine Funktion, die eine Liste
von Argumenten entgegennimmt und eine übergebene Funktion
darauf anwendet.

Syntax:
    lambda parameter: ausdruck

Der Ausdruck wird automatisch zurückgegeben.

-----------------------------------------------------------
Warum gibt es Lambdas?
-----------------------------------------------------------
• um Code zu verkürzen  
• um kleine Einmal-Funktionen direkt beim Funktionsaufruf zu definieren  
• um Funktionen als Parameter zu übergeben  
• ideal für mathematische Ausdrücke, Sortierregeln und Filterlogik  

-----------------------------------------------------------
Beispiele aus der Aufgabe
-----------------------------------------------------------
"""
def drucke_funktion(argumente, funktion):
    for x in argumente:
        print("f(", x, ")=", funktion(x), sep="")

# Aufruf OHNE Lambda (mit eigener Funktion)
def polynom(x):
    return 2 * x**2 - 4 * x + 2

drucke_funktion([x for x in range(-2, 3)], polynom)

# Aufruf MIT Lambda – kein polynom() mehr nötig
drucke_funktion(
    [x for x in range(-2, 3)],
    lambda x: 2 * x**2 - 4 * x + 2
)

"""
-----------------------------------------------------------
Was passiert hier?
-----------------------------------------------------------
• drucke_funktion() ruft für jedes Argument die übergebene
  Funktion auf.
• Erstes Beispiel nutzt eine normale def-Funktion.
• Zweites Beispiel nutzt ein Lambda als einmaligen Kurz-Ersatz
  → gleiche Funktionalität, weniger Code.

Lambda ersetzt also eine komplette Funktionsdefinition, wenn
diese nur sehr kurz ist.

-----------------------------------------------------------
⚠️ PCAP-WICHTIG:
-----------------------------------------------------------
• Ein lambda-Ausdruck enthält **genau einen Ausdruck**
  (keine Schleifen, kein return, keine Blöcke).
• Rückgabewert ist automatisch der Ausdruck.
• Lambdas sind echte Funktionen — nur ohne Namen.
• Ideal, wenn eine Funktion **als Argument** übergeben wird.

-----------------------------------------------------------
Typische Prüfungsfallen:
-----------------------------------------------------------
lambda x: print(x)
→ gültig, aber Rückgabewert ist None (weil print() None liefert)

lambda x: x if x > 0 else -x
→ gültiger Ausdruck (ternärer Operator)

lambda x: (x := x + 1)
→ möglich, aber NICHT prüfungsrelevant

-----------------------------------------------------------
Merke:
-----------------------------------------------------------
Lambdas sind NICHT mächtiger als def — sie sind nur kürzer
und ideal für Einmal-Ausdrücke direkt im Funktionsaufruf.
"""

