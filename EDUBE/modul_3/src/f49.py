"""
Ausnahmen sind Klassen

Bisher haben wir Ausnahmen nur erkannt und darauf reagiert.
Jetzt schauen wir uns die Ausnahme selbst genauer an.

Wichtige Punkte:
- Ausnahmen sind Klassen
- Beim Auftreten einer Ausnahme wird ein Objekt dieser Klasse erzeugt
- Dieses Ausnahmeobjekt wandert durch den Programmablauf, bis ein passender except-Zweig gefunden wird
- Mit „except … as …“ kann dieses Ausnahmeobjekt abgefangen werden
- Das abgefangene Objekt enthält Informationen über den Fehler
- Die Textdarstellung der Ausnahme stammt aus der __str__()-Methode
- Der Bezeichner hinter „as“ ist nur innerhalb des except-Zweigs gültig
"""

try:
    zahl = int("Hello!")                              # Ungültige Umwandlung: String → int
except Exception as ausnahme:                         # Ausnahmeobjekt abfangen
    print(ausnahme)                                  # Ausgabe der Fehlermeldung
    print(ausnahme.__str__())                         # expliziter Aufruf der __str__()-Methode
