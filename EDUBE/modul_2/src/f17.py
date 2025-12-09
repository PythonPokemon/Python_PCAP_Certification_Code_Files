"""
Die Center()-Methode
Die Ein-Parameter-Variante der Methode erstellt eine Kopie der ursprünglichen Zeichenkette und versucht, sie innerhalb eines Feldes einer bestimmten Breite zu zentrieren.center()

Die Zentrierung erfolgt tatsächlich, indem einige Zwischenräume vor und nach der Saite hinzugefügt werden.

Erwarten Sie nicht, dass diese Methode fortgeschrittene Fähigkeiten demonstriert. Es ist ziemlich einfach.

Das Beispiel im Editor verwendet Klammern, um klar zu zeigen, wo die zentrierte Zeichenkette tatsächlich beginnt und endet.

Sein Ergebnis sieht wie folgt aus:

[  alpha   ]
Ausgabe

Ist die Länge des Zielfeldes zu klein, um die Saite unterzubringen, wird die ursprüngliche Saite zurückgegeben.
"""
# Demonstrating the center() method:
print('[' + 'alpha'.center(10) + ']')


# Sie können die Methode in weiteren Beispielen hier sehen:center()
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')


# Die Zwei-Parameter-Variante von center() verwendet das Zeichen des zweiten Arguments anstelle eines Leerzeichens.
print('[' + 'gamma'.center(20, '*') + ']')

