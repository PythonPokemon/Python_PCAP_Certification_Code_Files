"""
Aufbau einer Klassenhierarchie (Fortsetzung)
Komposition statt Vererbung

-----------------------------------------------------------
Grundidee: Komposition
-----------------------------------------------------------
Neben der Vererbung gibt es eine zweite, sehr wichtige Technik,
um flexible und erweiterbare Klassen zu bauen: die Komposition.

Dabei gilt:

• Vererbung:
  - Eine Klasse ERBT Eigenschaften und Methoden von einer Superklasse
  - Verhalten ist fest in der Klassenhierarchie verdrahtet

• Komposition:
  - Eine Klasse BESITZT andere Objekte
  - Diese Objekte liefern Teilverhalten
  - Verhalten kann zur Laufzeit ausgetauscht werden

Merksatz (prüfungsrelevant):
👉 „Vererbung ist ein *ist-ein*, Komposition ist ein *hat-ein*“

-----------------------------------------------------------
Beispiel: Fahrzeug mit austauschbarer Lenkung
-----------------------------------------------------------
• Fahrzeug weiß, WIE man abbiegt (Ablauf)
• Fahrzeug weiß NICHT, WODURCH abgebogen wird
• Die konkrete Steuerung übernimmt ein externes Objekt
  (Controller), z. B. Räder oder Ketten
"""

import time


class Ketten:
    def richtung_aendern(self, links, aktiv):
        print("ketten:", links, aktiv)           # Steuerung über Ketten


class Raeder:
    def richtung_aendern(self, links, aktiv):
        print("räder:", links, aktiv)             # Steuerung über Vorderräder


class Fahrzeug:
    def __init__(self, steuerung):
        self.steuerung = steuerung                # Zusammengesetztes Objekt (Komposition)

    def abbiegen(self, links):
        self.steuerung.richtung_aendern(links, True)   # Richtungsänderung starten
        time.sleep(0.25)                               # kurze Pause
        self.steuerung.richtung_aendern(links, False)  # Richtungsänderung beenden


# ---------------------------------------------------------
# Test der Komposition
# ---------------------------------------------------------
radfahrzeug = Fahrzeug(Raeder())                  # Fahrzeug mit Rädern
kettenfahrzeug = Fahrzeug(Ketten())               # Fahrzeug mit Ketten

radfahrzeug.abbiegen(True)
kettenfahrzeug.abbiegen(False)
