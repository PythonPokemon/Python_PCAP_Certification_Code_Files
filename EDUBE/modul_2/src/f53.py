"""
Ausnahmen: Fortsetzung
Die raise-Anweisung löst eine Ausnahme KÜNSTLICH aus, so als wäre sie
ganz natürlich im Programm entstanden:

    raise AusnahmeTyp

Wichtig:
• raise ist ein Python-Schlüsselwort.
• Damit kannst du absichtlich eine bestimmte Ausnahme erzeugen.
• Das ist nützlich, um Fehlerbehandlungen zu testen oder um
  bestimmte Programmteile bewusst zu trennen („separation of concerns“).

Typische Einsatzgebiete von raise:
1) Testen deiner Fehlerbehandlung, ohne absichtlich falsche Eingaben
   oder gefährliche Operationen ausführen zu müssen.
2) Eine Ausnahme teilweise im aktuellen Code behandeln und dann
   bewusst weiterreichen, damit ein anderer Teil des Programms
   den Rest der Behandlung übernimmt.

Im folgenden Beispiel wird ZeroDivisionError absichtlich ausgelöst.
Das Verhalten ist identisch zu einer echten Division-durch-Null.

Die Ausgabe lautet:
    Was ist passiert? Ein Fehler?
    ENDE.
"""
# Beispiel: künstliches Auslösen einer Ausnahme
def boese_funktion(wert):
    raise ZeroDivisionError   # Ausnahme wird absichtlich erzeugt

try:
    boese_funktion(0)
except ArithmeticError:
    print("Was ist passiert? Ein Fehler?")

print("ENDE.")
