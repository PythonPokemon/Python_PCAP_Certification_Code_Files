"""
📘 Vergleichen von Strings – Fortsetzung

Auch wenn ein String nur Ziffern enthält, ist er nicht automatisch eine Zahl.
Er wird wie jeder normale String behandelt – sein numerischer Wert spielt keine Rolle.

"""

# 🔍 Beispiel 1 – Strings sind keine Zahlen
print('10' == '010')
print('10' > '010')
print('10' > '8')
print('20' < '8')
print('20' < '80')





"""
📌 Erklärung: Wie Python Strings vergleicht

Python vergleicht Strings:
    von links nach rechts
    Zeichen für Zeichen
    nach Unicode-/ASCII-Werten
⚠️ Python vergleicht NICHT die Zahlenwerte der Strings.
------------------------------------------------------------------------------------
✅ Warum wird bei '20' < '8' wirklich '2' mit '8' verglichen?

Weil Python IMMER nur das erste Zeichen vergleicht, so lange es unterschiedlich ist.

Es wird NICHT die Zahl 20 mit der Zahl 8 verglichen.
Es wird rein zeichenweise verglichen:

🔍 Vergleich: '20' < '8'

String 1: "20"
String 2: "8"

Python vergleicht:

Erstes Zeichen links: '2'
Erstes Zeichen rechts: '8'
"""
# 🔍 Beispiel 2 – Zeichenweiser Vergleich

# '1' wird mit '0' verglichen → '1' hat höheren Unicode-Wert
print('10' > '010')   # True

# '2' wird mit '8' verglichen → '2' < '8'
print('20' < '8')     # True





"""
⚠️ Vergleiche zwischen Strings und Zahlen

Du kannst Strings und Zahlen nicht sinnvoll vergleichen.
----------------------------------------------------------------------------
Erlaubt sind nur:

    ==
    !=
----------------------------------------------------------------------------
Alle anderen Vergleichsoperatoren (>, <, >=, <=) führen zu einem TypeError.
"""

# 🔍 Beispiel 3 – erlaubte Vergleiche
print('10' == 10)   # False
print('10' != 10)   # True
print('10' == 1)    # False
print('10' != 1)    # True



# 🔥 Beispiel 4 – verbotener Vergleich (führt zu Fehler)
# Dieser Vergleich führt zu einem TypeError, weil String und Zahl nicht mit > verglichen werden dürfen.
print('10' > 10)
