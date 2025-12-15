"""
Detaillierte Anatomie der Ausnahmen

Jede Ausnahme ist ein Objekt einer Ausnahmeklasse.
Diese Objekte besitzen die Eigenschaft args.

Eigenschaft args:
- args ist ein Tupel
- es enthält alle Argumente, die beim Erzeugen der Ausnahme übergeben wurden
- keine Argumente  → args ist leer ()
- ein Argument     → args enthält ein Element
- mehrere Argumente → args enthält mehrere Elemente

Die Textausgabe der Ausnahme (__str__()) basiert auf dem Inhalt von args.
"""

def args_ausgeben(argumente):
    anzahl = len(argumente)                           # Anzahl der übergebenen Argumente
    if anzahl == 0:
        print("")                                     # Keine Argumente
    elif anzahl == 1:
        print(argumente[0])                           # Ein einzelnes Argument
    else:
        print(str(argumente))                         # Mehrere Argumente als Tupel


try:
    raise Exception                                  # Ausnahme ohne Argumente erzeugen
except Exception as ausnahme:
    print(ausnahme, ausnahme.__str__(), sep=' : ', end=' : ')
    args_ausgeben(ausnahme.args)                      # args-Tupel auswerten


try:
    raise Exception("meine ausnahme")                 # Ausnahme mit einem Argument
except Exception as ausnahme:
    print(ausnahme, ausnahme.__str__(), sep=' : ', end=' : ')
    args_ausgeben(ausnahme.args)                      # args enthält ein Element


try:
    raise Exception("meine", "ausnahme")              # Ausnahme mit zwei Argumenten
except Exception as ausnahme:
    print(ausnahme, ausnahme.__str__(), sep=' : ', end=' : ')
    args_ausgeben(ausnahme.args)                      # args enthält zwei Elemente
