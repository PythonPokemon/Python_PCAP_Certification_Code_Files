"""
Der Stack – objektorientierter Ansatz
Wir bauen nun einen Stack (Stapel) nicht mehr prozedural,
sondern als eigene Klasse.

Grundidee bleibt gleich:
• Wir verwenden eine Liste als Speichercontainer.
• JEDES Stack-Objekt soll SEINE EIGENE Liste besitzen.
  → Keine gemeinsame Liste für mehrere Stacks!

Warum?
Damit jeder Stack unabhängig funktioniert.

----------------------------------------
Verbergen der internen Liste
----------------------------------------
Benutzer der Klasse sollen den internen Speicher NICHT direkt sehen.
Das ist in Python nicht über Sprachregeln erzwungen,
aber durch Konventionen und Konstruktion möglich.

----------------------------------------
Der Konstruktor (__init__)
----------------------------------------
Ein Konstruktor ist eine spezielle Methode, die automatisch aufgerufen wird,
wenn ein neues Objekt erzeugt wird.

Eigenschaften des Konstruktors:
• Name immer: __init__
• Wird automatisch ausgeführt
• Muss mindestens einen Parameter enthalten → self
  (self = Referenz auf das neu erstellte Objekt)
• Hier wird die interne Stack-Liste angelegt

Beispiel:
Beim Erstellen eines neuen Stack-Objekts wird __init__ aufgerufen
(auch wenn im Code KEIN sichtbarer Aufruf steht).

Das folgende Beispiel zeigt nur den Konstruktor,
der beim Erzeugen eines Objekts eine Meldung ausgibt.
"""
# Definition der Stack-Klasse mit Konstruktor
class Stapel:
    def __init__(self):        # Der Konstruktor
        print("Hallo!")        # Wird automatisch aufgerufen


# Ein Objekt erzeugen → Konstruktor läuft automatisch
stapel_objekt = Stapel()
