"""
Der Numbers Processor (eingedeutschte Version)
Dieses Programm liest eine Zeile mit Zahlen ein (durch Leerzeichen getrennt)
und berechnet deren Summe.

Hinweise:
• Jede Zahl muss durch ein Leerzeichen getrennt sein
• Zahlen dürfen Fließkommazahlen (float) sein
• input(), int() und float() allein reichen nicht, um mehrere Werte zu verarbeiten
• Daher wird die Zeile mit split() in einzelne Teilstrings zerlegt


Ablauf:
1) Benutzer gibt eine Zeile mit Zahlen ein
2) split() zerlegt die Eingabe in einzelne Teilstrings
3) summe wird mit 0 gestartet
4) try-except fängt fehlerhafte Eingaben ab
5) Jede Teilzeichenkette wird versucht in float umzuwandeln
6) Erfolgreiche Umwandlungen werden zur Summe hinzugefügt
7) Am Ende Ausgabe der Gesamtsumme
8) Bei Fehler: Ausgabe, welches Element keine Zahl war
"""
# Numbers Processor – eingedeutscht
eingabe_zeile = input("Geben Sie eine Reihe von Zahlen ein – getrennt durch Leerzeichen: ")
teile = eingabe_zeile.split()
summe = 0

try:
    for teil in teile:
        summe += float(teil)
    print("Die Gesamtsumme ist:", summe)
except:
    print(teil, "ist keine gültige Zahl.")
