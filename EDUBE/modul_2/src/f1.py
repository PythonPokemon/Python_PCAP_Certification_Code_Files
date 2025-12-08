"""
Strings – eine kurze Übersicht
Lassen Sie uns einen kurzen Überblick über die Natur der Python-Strings machen.

Zunächst einmal sind Pythons Strings (oder einfach Strings, da wir keine anderen Sprachstrings besprechen) unveränderliche Sequenzen.

Es ist sehr wichtig, das zu beachten, denn das bedeutet, dass man von ihnen ein vertrautes Verhalten erwarten sollte.

Analysieren wir den Code im Editor, um zu verstehen, wovon wir sprechen:

Schau dir Beispiel 1 an. Die für Strings verwendete Funktion gibt eine Anzahl von Zeichen zurück, die von den Argumenten enthalten sind. Der Ausschnitt gibt .len()2
Jede Zeichenkette kann leer sein. Seine Länge ist dann – genau wie in Beispiel 2.0
Vergiss nicht, dass ein Backslash () als Escape-Zeichen nicht in die Gesamtlänge der Schnur einbezogen ist. Der Code in Beispiel 3 gibt daher .\3
Führe die drei Beispielcodes durch und prüfe es.
"""


# Example 1

word = 'by'
print(len(word))


# Example 2

empty = ''
print(len(empty))


# Example 3

i_am = 'I\'m'
print(len(i_am))
