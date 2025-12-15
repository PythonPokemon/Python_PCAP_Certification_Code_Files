"""
Wie Python Eigenschaften und Methoden findet – Fortsetzung
Instanzvariablen und Vererbung
-----------------------------------------------------

Jetzt betrachten wir denselben Mechanismus wie zuvor,
aber diesmal mit **Instanzvariablen** statt Klassenvariablen.

-----------------------------------------------------------
Wichtige Regel:
-----------------------------------------------------------
• Instanzvariablen entstehen **nur**, wenn der Konstruktor (__init__)
  ausgeführt wird.
• Wird der Konstruktor der Superklasse NICHT aufgerufen,
  existieren deren Instanzvariablen im Objekt NICHT.
• Unterklassen können:
    – eigene Instanzvariablen hinzufügen
    – Instanzvariablen der Superklasse übernehmen (durch super().__init__())

-----------------------------------------------------------
Beispiel:
-----------------------------------------------------------
• Super erstellt im Konstruktor:
      self.super_wert = 11
• Sub ruft den Super-Konstruktor auf UND erstellt zusätzlich:
      self.sub_wert = 12

Dadurch besitzt das Objekt BEIDE Instanzvariablen.

-----------------------------------------------------------
Erwartete Ausgabe:
-----------------------------------------------------------
12
11

✅ Merksatz (prüfungsrelevant):
Instanzvariablen der Superklasse existieren nur dann,
wenn deren Konstruktor auch wirklich ausgeführt wurde (super().__init__()).
"""

# ---------------------------------------------------------
# Instanzvariablen in Vererbung
# ---------------------------------------------------------
class Super:
    def __init__(self):
        self.super_wert = 11                         # Instanzvariable der Superklasse


class Sub(Super):
    def __init__(self):
        super().__init__()                           # Superklassen-Konstruktor ausführen (sehr wichtig!)
        self.sub_wert = 12                           # zusätzliche Instanzvariable der Unterklasse


objekt = Sub()                                       # Objekt der Unterklasse erzeugen

print(objekt.sub_wert)                               # Zugriff auf Instanzvariable der Unterklasse → 12
print(objekt.super_wert)                             # Zugriff auf geerbte Instanzvariable → 11
