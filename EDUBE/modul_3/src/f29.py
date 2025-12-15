"""
Erbschaft – warum und wie?
Grundlagen der Vererbung in Python
-----------------------------------------------------

Der Begriff „Vererbung“ stammt ursprünglich nicht aus der Informatik,
sondern beschreibt das Weitergeben von Eigenschaften.

In der Objektorientierung bedeutet Vererbung etwas anderes:

-----------------------------------------------------------
Definition: Vererbung
-----------------------------------------------------------
Vererbung ist ein zentrales Konzept der objektorientierten Programmierung.

Dabei gilt:
• Eine UNTERKLASSE übernimmt (erbt) Attribute und Methoden
  von einer bereits existierenden Klasse, der SUPERKLASSE.
• Die Unterklasse kann:
    – alles Geerbte verwenden
    – zusätzlich neue Eigenschaften und Methoden hinzufügen
    – bestehende Methoden überschreiben (später wichtig!)

Ziel:
→ Code-Wiederverwendung
→ klare Hierarchien
→ spezialisierte Klassen statt doppeltem Code

-----------------------------------------------------------
Transitive Eigenschaft der Vererbung
-----------------------------------------------------------
Vererbung ist transitiv:

Wenn:
• Klasse B von Klasse A erbt
• Klasse C von Klasse B erbt

Dann gilt automatisch:
→ Klasse C erbt auch von Klasse A

-----------------------------------------------------------
Beispiel: Mehrstufige Vererbung
-----------------------------------------------------------
Wir definieren drei Klassen:

• Vehicle           → allgemeine Oberklasse
• LandVehicle       → spezialisiert Vehicle
• TrackedVehicle    → spezialisiert LandVehicle

Alle Klassen sind noch leer, es geht hier nur um die Beziehung.
"""

class Vehicle:
    pass                                            # Oberklasse (Superklasse)


class LandVehicle(Vehicle):
    pass                                            # Unterklasse von Vehicle


class TrackedVehicle(LandVehicle):
    pass                                            # Unterklasse von LandVehicle


"""
-----------------------------------------------------------
Beziehungen der Klassen (logisch erklärt)
-----------------------------------------------------------

1) Vehicle ist Superklasse von:
   • LandVehicle
   • TrackedVehicle

2) LandVehicle ist:
   • Unterklasse von Vehicle
   • Superklasse von TrackedVehicle

3) TrackedVehicle ist Unterklasse von:
   • LandVehicle
   • Vehicle

Diese Beziehungen erkennen wir als Leser sofort am Code.

-----------------------------------------------------------
Wichtige Frage:
-----------------------------------------------------------
Weiß Python das auch?

Antwort:
JA.

Python speichert diese Informationen intern und stellt sie über
eingebaute Mechanismen zur Verfügung (z. B. __bases__, issubclass()).

➡️ Genau DAS schauen wir uns im nächsten Schritt an.
✅ issubclass()
✅ isinstance()
✅ Vererbungsprüfung in Prüfungsaufgaben (PCAP/PCPP-Style)
"""