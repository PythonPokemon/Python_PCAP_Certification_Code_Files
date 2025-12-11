"""
Methoden im Detail

Eine Methode ist eine Funktion, die innerhalb einer Klasse definiert ist.
Es gibt einige grundlegende Regeln, die für alle Methoden in Python gelten:

-----------------------------------------------------------
1) Jede Methode MUSS mindestens einen Parameter besitzen.
-----------------------------------------------------------
Auch wenn du die Methode ohne Argumente aufrufst, muss sie mindestens
einen Parameter definieren.

-----------------------------------------------------------
2) Der erste Parameter heißt üblicherweise „self“.
-----------------------------------------------------------
• self verweist auf das aktuelle Objekt.
• Durch self greift die Methode auf Attribute oder andere Methoden
  desselben Objekts zu.
• Du solltest immer „self“ verwenden – das ist Python-Konvention.

-----------------------------------------------------------
3) Beim Aufruf darfst du KEIN Argument für self übergeben.
-----------------------------------------------------------
Python übergibt automatisch das aktuelle Objekt als erstes Argument.

Beispiel:
    objekt.methode()
→ Intern ruft Python auf:
    Klasse.methode(objekt)

-----------------------------------------------------------
Beispiel 1: Methode ohne zusätzliche Parameter
-----------------------------------------------------------
Die Methode hat nur „self“. Beim Aufruf wird self NICHT übergeben.
"""

class Beispiel:
    def zeige_methode(self):                       # Methode mit self als Parameter
        print("Methode wurde ausgeführt")          # einfache Ausgabe

objekt = Beispiel()                                # Objekt erstellen
objekt.zeige_methode()                             # self wird automatisch übergeben



"""
-----------------------------------------------------------
Beispiel 2: Methode mit zusätzlichem Parameter
-----------------------------------------------------------
Wenn eine Methode weitere Parameter hat:

1) stehen sie NACH self in der Definition.
2) werden sie beim Aufruf wie normale Argumente übergeben.
3) self wird weiterhin automatisch durch Python ergänzt.

Erwartete Ausgabe:
    Methode: 1
    Methode: 2
    Methode: 3
"""

class KlasseMitParameter:
    def methode(self, wert):                        # zusätzlicher Parameter "wert"
        print("Methode:", wert)

obj = KlasseMitParameter()
obj.methode(1)                                      # wert = 1
obj.methode(2)                                      # wert = 2
obj.methode(3)                                      # wert = 3
