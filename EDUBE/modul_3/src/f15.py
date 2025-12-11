"""
Überprüfung der Existenz eines Attributs

In Python müssen Objekte derselben Klasse nicht zwingend die gleichen
Attribute besitzen. Welche Attribute ein Objekt wirklich hat, hängt
davon ab, wie der Konstruktor (oder andere Methoden) sie erzeugen.

-----------------------------------------------------------
Beispiel erklärt
-----------------------------------------------------------
Das Objekt erhält je nach Eingabewert unterschiedliche Attribute:

    • Bei ungeraden Zahlen → Attribut "a"
    • Bei geraden Zahlen   → Attribut "b"

Das bedeutet:
Ein Objekt kann "a" besitzen, aber kein "b" – oder umgekehrt.

-----------------------------------------------------------
Wichtig:
-----------------------------------------------------------
Wenn versucht wird, auf ein Attribut zuzugreifen, das nicht existiert,
löst Python eine **AttributeError**-Ausnahme aus.

Das Beispiel zeigt genau dieses Verhalten:

1) Wir erzeugen ein Objekt mit dem Wert 1 → ungerade → Attribut a wird erstellt.
2) Zugriff auf a funktioniert.
3) Zugriff auf b führt zu:

    AttributeError: 'BeispielKlasse' object has no attribute 'b'

-----------------------------------------------------------
Merksatz (PCAP-wichtig):
-----------------------------------------------------------
In Python entstehen Attribute erst, wenn sie ZUGEWIESEN werden.
Es gibt keine Garantie, dass jedes Objekt dieselben Attribute besitzt.
"""

class BeispielKlasse:
    def __init__(self, wert):
        if wert % 2 != 0:
            self.a = 1                                # Attribut a wird nur bei ungeraden Werten erzeugt
        else:
            self.b = 1                                # Attribut b wird nur bei geraden Werten erzeugt


objekt = BeispielKlasse(1)                            # ungerade → hat nur 'a'

print(objekt.a)                                       # OK
print(objekt.b)                                       # Fehler: Attribut existiert nicht
