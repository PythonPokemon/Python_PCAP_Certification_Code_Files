"""
Method Resolution Order (MRO) – was ist das und warum ergibt nicht jede Vererbung Sinn?

-----------------------------------------------------------
Was ist MRO?
-----------------------------------------------------------
MRO (Method Resolution Order) beschreibt die feste Reihenfolge,
in der Python bei Vererbung nach Methoden und Attributen sucht.

Kurz gesagt:
👉 MRO bestimmt, WELCHE Methode aufgerufen wird,
   wenn mehrere Klassen dieselben Namen definieren.

Wichtig:
- Jede Programmiersprache hat ihre eigene MRO-Strategie
- Python verwendet eine feste, mathematisch definierte Ordnung
- Diese Ordnung DARF NICHT verletzt werden

-----------------------------------------------------------
Beispiel 1: Saubere einfache Vererbung
-----------------------------------------------------------
Hier gibt es nur einen klaren Vererbungsweg:
Unten → Mitte → Oben

Die Auflösung ist eindeutig und problemlos.
"""

class Oben:
    def methode_oben(self):
        print("oben")                      # Methode der Oberklasse


class Mitte(Oben):
    def methode_mitte(self):
        print("mitte")                     # Methode der Mittelklasse


class Unten(Mitte):
    def methode_unten(self):
        print("unten")                     # Methode der Unterklasse


objekt = Unten()

objekt.methode_oben()     # Oberklasse
objekt.methode_mitte()    # Mittelklasse
objekt.methode_unten()    # Unterklasse



"""
-----------------------------------------------------------
Beispiel 2: Mehrfachvererbung – formal korrekt, aber sinnlos
-----------------------------------------------------------
Hier wird Mehrfachvererbung genutzt, obwohl sie keinen Mehrwert bringt.

Die Reihenfolge (Mitte, Oben) entspricht dem echten Vererbungsweg:
Mitte IST bereits eine Unterklasse von Oben.

➡️ Das Programm funktioniert,
➡️ bringt aber KEINE neue Funktionalität.
"""

class UntenExotisch(Mitte, Oben):
    def methode_unten(self):
        print("unten")


objekt = UntenExotisch()

objekt.methode_oben()     # Oberklasse
objekt.methode_mitte()    # Mittelklasse
objekt.methode_unten()    # Unterklasse



"""
-----------------------------------------------------------
Beispiel 3: Ungültige MRO – Python verweigert die Ausführung
-----------------------------------------------------------
Jetzt wird die Reihenfolge absichtlich zerstört.

Problem:
- Mitte erbt von Oben
- Unten behauptet aber: erst Oben, dann Mitte

❌ Das widerspricht der echten Vererbungsstruktur
❌ Python kann keine konsistente MRO berechnen
"""

class UntenFehlerhaft(Oben, Mitte):
    def methode_unten(self):
        print("unten")


"""
Beim Erstellen der Klasse entsteht folgender Fehler:

TypeError:
Cannot create a consistent method resolution order (MRO)
for bases Oben, Mitte
"""

"""
-----------------------------------------------------------
Merksätze (PRÜFUNGSRELEVANT)
-----------------------------------------------------------

✅ Python sucht Methoden:
1) im Objekt selbst
2) dann entlang der MRO
3) von links nach rechts
4) von unten nach oben

❌ Mehrfachvererbung darf die echte Vererbungsstruktur NICHT verletzen
❌ Die Reihenfolge der Superklassen ist entscheidend
❌ Eine ungültige MRO führt zu einem TypeError

👉 Fazit:
Nicht jede Vererbung macht Sinn.
Nicht jede erlaubte Syntax ist gute Architektur.
"""
