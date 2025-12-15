"""
Wie Python Eigenschaften und Methoden findet – Fortsetzung
Mehrfache Vererbung (Multiple Inheritance)
-----------------------------------------------------

Multiple Vererbung liegt vor, wenn eine Klasse **mehr als eine Superklasse**
besitzt.

Syntax:
    class Unterklasse(Superklasse1, Superklasse2, ...):

Die Superklassen werden **kommagetrennt** in Klammern angegeben.
Die Reihenfolge ist dabei **sehr wichtig** (das wird später bei Konflikten relevant!).

-----------------------------------------------------------
Was passiert bei multipler Vererbung?
-----------------------------------------------------------
• Die Unterklasse erbt ALLE Klassenvariablen der Superklassen
• Die Unterklasse erbt ALLE Methoden der Superklassen
• Ein Objekt der Unterklasse kann auf alles zugreifen,
  was in allen Superklassen definiert ist

-----------------------------------------------------------
Beispiel:
-----------------------------------------------------------
• SuperA liefert:
    - Klassenvariable var_a
    - Methode fun_a()

• SuperB liefert:
    - Klassenvariable var_b
    - Methode fun_b()

• Sub erbt von SuperA UND SuperB

-----------------------------------------------------------
Erwartete Ausgabe:
-----------------------------------------------------------
10 11
20 21
"""

# ---------------------------------------------------------
# Erste Superklasse
# ---------------------------------------------------------
class SuperA:
    var_a = 10                                      # Klassenvariable aus SuperA

    def fun_a(self):
        return 11                                  # Methode aus SuperA


# ---------------------------------------------------------
# Zweite Superklasse
# ---------------------------------------------------------
class SuperB:
    var_b = 20                                      # Klassenvariable aus SuperB

    def fun_b(self):
        return 21                                  # Methode aus SuperB


# ---------------------------------------------------------
# Unterklasse mit multipler Vererbung
# ---------------------------------------------------------
class Sub(SuperA, SuperB):
    pass                                            # erbt alles von SuperA und SuperB


objekt = Sub()                                      # Objekt der Unterklasse erzeugen

print(objekt.var_a, objekt.fun_a())                 # Zugriff auf SuperA → 10 11
print(objekt.var_b, objekt.fun_b())                 # Zugriff auf SuperB → 20 21


"""
-----------------------------------------------------------
Neuer Begriff: Überschreibung (Overriding)
-----------------------------------------------------------
Jetzt kommt die entscheidende Frage:

Was passiert, wenn MEHRERE Superklassen
eine Eigenschaft oder Methode mit DEMSELBEN Namen besitzen?

➡️ Genau das nennt man einen Namenskonflikt.
➡️ Python löst diesen Konflikt über die sogenannte
   Method Resolution Order (MRO).

• Die Reihenfolge der Superklassen entscheidet!
• Python sucht von links nach rechts.

Das schauen wir uns im nächsten Abschnitt ganz konkret an.
"""


