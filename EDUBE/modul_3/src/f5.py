"""
Der Objekt-Ansatz: ein Stapel (Stack) von Grund auf
Jetzt definieren wir die beiden Methoden, die den Stack funktionsfähig machen:
• push() – legt einen Wert oben auf den Stapel
• pop() – nimmt den obersten Wert vom Stapel herunter

Diese Methoden müssen:
• öffentlich sein (Namen ohne führende Unterstriche)
• im Klassenkörper definiert werden
• auf die interne, private Liste zugreifen (__stapel_liste)

Warum keine zwei Unterstriche bei push und pop?
• Öffentlich → Name darf NICHT mit __ beginnen
• Nur interne Attribute (Daten) sollten verborgen sein

Wichtig: Jede Methode einer Klasse benötigt mindestens einen Parameter.
Dieser erste Parameter heißt fast immer 'self'.

Warum 'self'?
• Python übergibt AUTOMATISCH das aktuelle Objekt als erstes Argument.
• self ermöglicht der Methode Zugriff auf:
    - interne Attribute (z. B. self.__stapel_liste)
    - andere Methoden des Objekts

Wenn du eine Methode so definierst:

    def push(self, wert):

und sie so aufrufst:

    objekt.push(5)

dann macht Python intern Folgendes:

    Stapel.push(objekt, 5)

→ 'objekt' wird automatisch als self übergeben!

--------------------------------------------------------------
Aufbau der finalen Stack-Klasse
--------------------------------------------------------------
1) Konstruktor erstellt die private Liste __stapel_liste
2) push() fügt am Ende der Liste einen Wert ein
3) pop() entnimmt und entfernt den letzten Listeneintrag
4) Der Stack arbeitet nach LIFO – Last In, First Out
"""
class Stapel:
    def __init__(self):
        self.__stapel_liste = []   # private Stack-Liste

    def push(self, wert):
        self.__stapel_liste.append(wert)  # Wert oben auf den Stapel legen

    def pop(self):
        oberster_wert = self.__stapel_liste[-1]  # obersten Wert lesen
        del self.__stapel_liste[-1]              # Wert entfernen
        return oberster_wert                    # Wert zurückgeben


# Stack verwenden
stapel_objekt = Stapel()

stapel_objekt.push(3)
stapel_objekt.push(2)
stapel_objekt.push(1)

print(stapel_objekt.pop())   # 1
print(stapel_objekt.pop())   # 2
print(stapel_objekt.pop())   # 3
