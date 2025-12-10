"""
Ausnahmen: Fortsetzung
------------------------------------------------------
Im folgenden Beispiel tritt ein klarer Fehler auf:
Eine Zahl wird durch 0 geteilt.

Python reagiert darauf mit einer Ausnahme (Exception),
genauer mit einem ZeroDivisionError.

Ausgaben eines solchen Programms sehen etwa so aus:

Traceback (most recent call last):
  File "div.py", line 2, in <module>
    value /= 0
ZeroDivisionError: division by zero

Der Fehlername lautet also: ZeroDivisionError.
"""
# Beispielcode, der einen ZeroDivisionError erzeugt:
wert = 1
wert /= 0   # Division durch Null → löst Ausnahme aus
