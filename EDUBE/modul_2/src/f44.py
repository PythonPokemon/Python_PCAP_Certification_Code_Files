"""
Ausnahmen: Fortsetzung
Dies ist der bevorzugte Python-Ansatz zur Fehlerbehandlung: try / except.

Funktionsweise:

1) Das Schlüsselwort try leitet einen Block ein, der riskanten Code enthält.
   → Python versucht, diesen Block vollständig auszuführen.

2) Wenn während der Ausführung eine Ausnahme entsteht,
   → springt Python sofort zum except-Block.

3) Der except-Block enthält den Code, der ausgeführt wird,
   wenn im try-Block etwas schiefgegangen ist.
   → Er bietet also eine angemessene Reaktion auf den Fehler.

4) Nach dem except-Block geht das Programm normal weiter.

Zusammengefasst:

try:
    # riskante Anweisungen
except:
    # Reaktion auf Fehler

Ablauf:
• Wenn im try-Block alles fehlerfrei läuft,
  → der except-Block wird übersprungen.

• Wenn im try-Block ein Fehler passiert,
  → der restliche try-Code wird übersprungen
  → und der except-Block wird ausgeführt.
"""
# Beispiel: bevorzugte Python-Methode (try/except)
erste_zahl = int(input("Geben Sie die erste Zahl ein: "))
zweite_zahl = int(input("Geben Sie die zweite Zahl ein: "))

try:
    print(erste_zahl / zweite_zahl)
except:
    print("Diese Operation kann nicht durchgeführt werden.")

print("ENDE.")
