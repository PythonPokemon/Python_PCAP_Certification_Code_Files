"""
Die join()-Methode
Die Methode ist ziemlich kompliziert, also lassen Sie uns Sie Schritt für Schritt durch sie führen:join()

Wie der Name schon sagt, führt die Methode einen Join durch – sie erwartet ein Argument als Liste; 
es muss sichergestellt werden, dass alle Elemente der Liste Strings sind – sonst löst die Methode eine TypeError-Ausnahme aus;

Alle Elemente der Liste werden zu einem String zusammengeführt, aber...
... die Zeichenkette, von der aus die Methode aufgerufen wurde, wird als Separator verwendet, der unter die Zeichenketten gelegt wird;

die neu erstellte Zeichenkette wird als Ergebnis zurückgegeben.
"""

# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))


