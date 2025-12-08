"""

Operationen an strings: fortgesetzt
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Denk nicht, dass die Unveränderlichkeit einer Saite deine Fähigkeit, mit Saiten zu arbeiten, einschränkt.

Die einzige Folge ist, dass du dich daran erinnern und deinen Code etwas anders implementieren musst – schau dir den Beispielcode im Editor an.

Diese Codeform ist völlig akzeptabel, funktioniert ohne die Regeln von Python zu biegen und bringt das vollständige lateinische Alphabet auf deinen Bildschirm:

abcdefghijklmnopqrstuvwxyz
Ausgabe

Du solltest dich fragen, ob das Erstellen einer neuen Kopie eines Strings bei jeder Änderung des Inhalts die Effektivität des Codes verschlechtert.

Ja, das tut es. Ein wenig. Das ist aber überhaupt kein Problem.
"""

alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)
