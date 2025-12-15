"""
Wie Python Eigenschaften und Methoden findet – Fortsetzung
Klassenvariablen und Vererbung
-----------------------------------------------------

Jetzt betrachten wir, wie Python mit **Klassenvariablen** in
Vererbungsstrukturen umgeht.

-----------------------------------------------------------
Wichtige Regel:
-----------------------------------------------------------
• Klassenvariablen werden von Unterklassen **geerbt**
• Ein Objekt kann auf Klassenvariablen zugreifen:
, auch wenn:
    – sie in der Superklasse definiert wurden
• Python sucht Klassenvariablen in derselben Reihenfolge
  wie Methoden (MRO):

    1) Klasse des Objekts
    2) Superklasse
    3) weitere Vorfahren
    4) object

-----------------------------------------------------------
Beispiel:
-----------------------------------------------------------
• Superklasse besitzt:  super_variable
• Unterklasse besitzt: sub_variable
• Objekt der Unterklasse kann auf BEIDE zugreifen

-----------------------------------------------------------
Erwartete Ausgabe:
-----------------------------------------------------------
2
1

✅ Merksatz (PCAP/PCPP-wichtig):
Objekte können geerbte Klassenvariablen genauso nutzen
wie eigene Klassenvariablen der Unterklasse.
"""

# ---------------------------------------------------------
# Klassenvariablen in Vererbung
# ---------------------------------------------------------
class Super:
    super_variable = 1                               # Klassenvariable der Superklasse


class Sub(Super):
    sub_variable = 2                                 # Klassenvariable der Unterklasse


objekt = Sub()                                       # Objekt der Unterklasse erzeugen

print(objekt.sub_variable)                           # zuerst in Sub gefunden → 2
print(objekt.super_variable)                         # nicht in Sub → aus Super geerbt → 1
