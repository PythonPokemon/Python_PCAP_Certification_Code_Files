"""
Der Stack – prozeduraler Ansatz
Ein Stack (Stapel) ist eine Datenstruktur nach dem Prinzip:
LIFO = Last In, First Out
Das zuletzt abgelegte Element wird als erstes wieder entnommen.

Für die Implementierung nutzen wir eine Liste.
Das letzte Listenelement repräsentiert den "obersten" Stack-Eintrag.

1) Der Stack wird als leere Liste angelegt:
       stapel = []

2) Die Funktion push():
   • legt einen Wert oben auf den Stapel
   • nimmt genau EIN Argument entgegen
   • gibt nichts zurück
   • fügt den Wert am Ende der Liste ein

3) Die Funktion pop():
   • nimmt KEINE Argumente entgegen
   • entnimmt den obersten Wert vom Stapel
   • entfernt dieses Element aus der Liste
   • gibt den entnommenen Wert zurück
   Hinweis: Die Funktion prüft NICHT, ob der Stapel leer ist.

Das vollständige Beispiel:
• Wir legen 3 Werte auf den Stapel
• Dann holen wir sie wieder herunter
• Ausgabe erfolgt in umgekehrter Reihenfolge (LIFO)
"""
# Stack als Liste
stapel = []

def push(wert):
    stapel.append(wert)   # Wert oben auf den Stapel legen

def pop():
    oberster_wert = stapel[-1]  # letzten Eintrag lesen
    del stapel[-1]              # obersten Eintrag entfernen
    return oberster_wert        # Wert zurückgeben

# Stack benutzen
push(3)
push(2)
push(1)

print(pop())   # 1
print(pop())   # 2
print(pop())   # 3
