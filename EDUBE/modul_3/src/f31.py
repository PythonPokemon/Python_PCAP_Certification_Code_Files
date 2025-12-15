"""
Vererbung / Objekte: der is-Operator
-----------------------------------------------------

Der Operator „is“ vergleicht **nicht den Inhalt**, sondern die **Identität**
von Objekten.

Syntax:
    objekt_1 is objekt_2

Bedeutung:
• True  → beide Variablen zeigen auf **dasselbe Objekt im Speicher**
• False → es sind **zwei verschiedene Objekte**, auch wenn der Inhalt gleich ist

-----------------------------------------------------------
Ganz wichtig (PCAP/PCPP-relevant):
-----------------------------------------------------------
• Variablen speichern **keine Objekte**, sondern nur REFERENZEN (Handles)
• Eine Zuweisung kopiert **nicht** das Objekt, sondern nur die Referenz
• ==  → vergleicht den INHALT
• is  → vergleicht die IDENTITÄT (Speicheradresse)

-----------------------------------------------------------
Beispiel 1: Eigene Klasse
-----------------------------------------------------------
Wir erzeugen:
• zwei unabhängige Objekte
• eine zweite Referenz auf dasselbe Objekt

Dann prüfen wir alle Kombinationen mit is.
"""

class BeispielKlasse:
    def __init__(self, wert):
        self.wert = wert                              # Instanzvariable speichern


objekt_1 = BeispielKlasse(0)                          # neues Objekt im Speicher
objekt_2 = BeispielKlasse(2)                          # anderes neues Objekt
objekt_3 = objekt_1                                   # KEIN neues Objekt → gleiche Referenz

objekt_3.wert += 1                                    # verändert objekt_1 UND objekt_3

print(objekt_1 is objekt_2)                            # False → verschiedene Objekte
print(objekt_2 is objekt_3)                            # False → verschiedene Objekte
print(objekt_3 is objekt_1)                            # True  → gleiche Referenz

print(objekt_1.wert, objekt_2.wert, objekt_3.wert)    # 1 2 1


"""
-----------------------------------------------------------
Beispiel 2: Strings
-----------------------------------------------------------
Auch wenn zwei Strings den gleichen Text enthalten,
müssen sie NICHT dasselbe Objekt sein.

• == vergleicht den Text
• is vergleicht das Objekt im Speicher

Erwartete Ausgabe:
True False

✅ Merksatz (sehr prüfungsrelevant):

== → „Sieht es gleich aus?“
is → „Ist es exakt dasselbe Objekt?“
"""

text_1 = "Mary had a little "
text_2 = "Mary had a little lamb"

text_1 += "lamb"                                      # neuer String wird erzeugt

print(text_1 == text_2, text_1 is text_2)             # Inhalt gleich, Objekt verschieden
