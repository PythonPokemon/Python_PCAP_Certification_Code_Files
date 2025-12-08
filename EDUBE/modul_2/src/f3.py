"""

Operationen auf Strings
Wie andere Arten von Daten haben Strings ihre eigenen zulässigen Operationen, die jedoch im Vergleich zu Zahlen eher begrenzt sind.

Im Allgemeinen können Strings:

Verkettet (verbunden)
repliziert.
Die erste Operation wird vom Operator ausgeführt (Anmerkung: Es ist keine Addition), während die zweite vom Operator ausgeführt wird (nochmals: Es ist keine Multiplikation).+*

Die Fähigkeit, denselben Operator gegen völlig unterschiedliche Arten von Daten (wie Zahlen vs. Zeichenketten) einzusetzen, nennt man Überladung (da ein solcher Operator mit unterschiedlichen Aufgaben überlastet ist).

Analysieren Sie das Beispiel:

Der Operator, der gegen zwei oder mehr Strings verwendet wird, erzeugt eine neue Zeichenkette, die alle Zeichen aus seinen Argumenten enthält 
(Anmerkung: Die Reihenfolge ist wichtig – diese Überlastung ist im Gegensatz zur numerischen Version nicht kommutativ++)
der Operator benötigt eine Zeichenkette und eine Zahl als Argumente; 
In diesem Fall spielt die Reihenfolge keine Rolle – du kannst die Zahl vor die Zeichenkette setzen oder umgekehrt, 
das Ergebnis ist dasselbe – eine neue Zeichenkette, die durch die n-te Replikation des Argumentzeichens erzeugt wird.*

"""

str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)
