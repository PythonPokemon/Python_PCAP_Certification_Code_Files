"""
Ausnahmen: Fortsetzung
Die raise-Anweisung kann auch OHNE Angabe eines Ausnahme-Typs verwendet werden:

    raise

Wichtig:
• Diese Form darf NUR innerhalb eines except-Blocks benutzt werden.
• Wird sie außerhalb eines except-Blocks verwendet → Fehler.
• Sie löst dieselbe Ausnahme erneut aus, die gerade behandelt wird.
  (man nennt das „Weiterreichen“ oder „Re-raise“.)

Warum ist das nützlich?
Damit kann man die Fehlerbehandlung aufteilen:
• Ein Teil der Behandlung passiert im aktuellen except-Block,
• der Rest wird an einen äußeren try/except-Block weitergegeben.

Im folgenden Beispiel passiert Folgendes:

1) ZeroDivisionError entsteht in bad_fun() durch n / 0.
2) Der except-Block von bad_fun() fängt ihn ab und gibt:
       "Ich habe es schon wieder getan!"
3) Der raise-Befehl OHNE Typ löst denselben ZeroDivisionError erneut aus.
4) Der äußere except ArithmeticError erkennt diese Ausnahme und gibt:
       "Ich verstehe!"
5) Danach läuft das Programm normal weiter.

Ausgabe:
    Ich habe es schon wieder getan!
    Ich verstehe!
    ENDE.
"""
# Beispiel: raise ohne Ausnahme-Typ – Re-raise derselben Ausnahme
def boese_funktion(n):
    try:
        return n / 0            # Fehler entsteht hier
    except:
        print("Ich habe es schon wieder getan!")
        raise                   # dieselbe Ausnahme erneut auslösen

try:
    boese_funktion(0)
except ArithmeticError:
    print("Ich verstehe!")

print("ENDE.")
