"""
Ausnahmen: Fortsetzung
Wie geht man mit Ausnahmen um? Das Schlüsselwort lautet: try.

Der typische Ansatz vieler Anfänger ist:
1) Erst alle Bedingungen prüfen.
2) Nur dann den kritischen Code ausführen, wenn alles „sicher“ erscheint.

Das Beispiel unten zeigt diesen klassischen Ansatz:
• Es wird geprüft, ob der zweite Wert ungleich 0 ist.
• Nur wenn das stimmt, wird die Division ausgeführt.
• Andernfalls wird eine Fehlermeldung ausgegeben.

Nachteil dieser Methode:
Viele Prüfungen machen den Code schnell lang und unübersichtlich.

Python bevorzugt später eine andere, viel sauberere Methode:
„Easier to ask for forgiveness than permission“ (EAFP).
Diese wird mit try/except realisiert – dazu kommen wir anschließend.
"""
# Klassischer Ansatz: erst prüfen, dann ausführen
erste_zahl = int(input("Geben Sie die erste Zahl ein: "))
zweite_zahl = int(input("Geben Sie die zweite Zahl ein: "))

if zweite_zahl != 0:
    print(erste_zahl / zweite_zahl)
else:
    print("Diese Operation kann nicht durchgeführt werden.")

print("ENDE.")
