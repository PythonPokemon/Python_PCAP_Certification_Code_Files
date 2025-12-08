"""
Die In- und Nicht-In-Operatoren
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Der In-Operator

Der Operator sollte dich nicht überraschen, wenn er auf Strings angewendet wird – er prüft einfach, 
ob sein linkes Argument (eine String) irgendwo im rechten Argument (einem anderen String) zu finden ist.in

Das Ergebnis der Prüfung ist einfach oder .TrueFalse
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Schauen Sie sich das Beispielprogramm unten an. So funktioniert der Operator:in
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)



"""
Der Nicht-in-Operator
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Wie du wahrscheinlich vermutest, ist auch der Betreiber hier relevant.not in
---------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
print("---")

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)

