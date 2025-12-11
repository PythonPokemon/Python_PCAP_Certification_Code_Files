"""
Das Innenleben von Klassen und Objekten – Fortsetzung
-----------------------------------------------------

Neben __dict__ besitzt jede Klasse auch das eingebaute Attribut:

    __name__

Dieses Attribut existiert NUR auf Klassenebene und enthält den
Klassennamen als Zeichenkette.

Wichtig:
• obj.__name__    → FEHLER! (Objekte haben kein __name__)
• Klassenname.__name__ → funktioniert

-----------------------------------------------------------
Wie findet man die Klasse eines OBJEKTS?
-----------------------------------------------------------

Dafür gibt es die eingebaute Funktion:

    type(obj)

Sie liefert u.a. die Klasse zurück, aus der das Objekt erzeugt wurde.
Daher funktioniert:

    type(obj).__name__

→ liefert ebenfalls den Klassennamen.

-----------------------------------------------------------
Erwartete Ausgabe dieses Beispiels:
-----------------------------------------------------------
Classy
Classy
"""

class Classy:
    pass                                            # leere Beispielklasse


print(Classy.__name__)                              # Name der Klasse → "Classy"

obj = Classy()                                      # Objekt instanziieren

print(type(obj).__name__)                           # über type() erneut "Classy"
