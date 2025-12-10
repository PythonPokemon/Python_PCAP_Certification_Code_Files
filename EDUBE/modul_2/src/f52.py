"""
Ausnahmen: Fortsetzung
Wenn mehrere Ausnahmen gleich behandelt werden sollen, kann man sie
in einem einzigen except-Zweig zusammenfassen:

    except (Fehler1, Fehler2):

Dabei stehen die Ausnahmen in einer Klammer, getrennt durch Kommas.

---------------------------------------------------------
Ausnahmen innerhalb von Funktionen
---------------------------------------------------------
Eine Ausnahme, die IN einer Funktion entsteht, kann auf zwei Arten
behandelt werden:

1) Die Funktion fängt die Ausnahme selbst ab.
2) Die Ausnahme wird „nach außen“ weitergereicht und muss vom Aufrufer
   behandelt werden.

---------------------------------------------------------
Variante 1: Ausnahme wird IN der Funktion abgefangen
---------------------------------------------------------
Im folgenden Beispiel entsteht ein ZeroDivisionError innerhalb
der Funktion bad_fun(), wird aber dort sofort behandelt.
Die Ausnahme verlässt die Funktion also NICHT.

Die Ausgabe lautet:
    Arithmetic Problem!
    ENDE.
"""
# Variante 1: Funktion behandelt die Ausnahme selbst
def boese_funktion(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None

boese_funktion(0)

print("ENDE.")


"""
---------------------------------------------------------
Variante 2: Ausnahme verlässt die Funktion und wird
            vom AUFRUFER behandelt
---------------------------------------------------------

Hier wird die Ausnahme NICHT in der Funktion abgefangen.
Sie propagiert (wandert) nach außen. Der try/except-Block des
Aufrufers muss sie behandeln.

Ausgabe:
    Was ist passiert? Eine Ausnahme wurde ausgelöst!
    ENDE.

Wichtig:
• Ausnahmen können Funktionen und sogar ganze Module durchlaufen.
• Sie „reisen“ die Aufrufkette nach oben, bis sie auf einen passenden
  except-Zweig treffen.
• Wenn nirgendwo ein passender except existiert, stürzt das Programm ab
  und Python zeigt eine Fehlermeldung an.
"""
# Variante 2: Ausnahme wird NICHT in der Funktion abgefangen
def boese_funktion(n):
    return 1 / n   # löst bei n=0 ZeroDivisionError aus

try:
    boese_funktion(0)
except ArithmeticError:
    print("Was ist passiert? Eine Ausnahme wurde ausgelöst!")

print("ENDE.")
