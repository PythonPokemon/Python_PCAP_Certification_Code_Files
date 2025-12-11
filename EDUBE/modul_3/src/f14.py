"""
Klassenvariablen: Fortsetzung

Klassenvariablen existieren bereits, bevor auch nur ein einziges Objekt
der Klasse erzeugt wurde. Das macht sie grundlegend anders als
Instanzvariablen.

In diesem Abschnitt vergleichen wir das __dict__ der Klasse und das
__dict__ eines Objekts.

-----------------------------------------------------------
Was zeigt das Beispiel?
-----------------------------------------------------------

1) Die Klasse BeispielKlasse besitzt eine Klassenvariable „wert“.
2) Im Konstruktor wird die Klassenvariable auf einen neuen Wert gesetzt.
3) Vor der Objekterzeugung geben wir bereits ExampleClass.wert aus –
   das funktioniert, weil Klassenvariablen OHNE Objekt existieren.

-----------------------------------------------------------
Wichtige Hinweise
-----------------------------------------------------------

• „BeispielKlasse.__dict__“ zeigt ALLE Klasseneigenschaften,
  inklusive Methoden und interner Python-Strukturen.

• „objekt.__dict__“ enthält NUR Instanzvariablen.

• Wenn der Konstruktor Folgendes schreiben würde:

      self.wert = val

  → dann entstünde eine INSTANZvariable, die die Klassenvariable NICHT überschreibt.

• Wenn der Konstruktor einfach „wert = val“ schreiben würde:

      wert = val

  → dann wäre dies nur eine lokale Variable der Methode und hätte
    keinerlei Einfluss auf Klassen- oder Instanzvariablen.

Wir empfehlen, beide Varianten auszuprobieren, um den Unterschied
wirklich zu verstehen.

-----------------------------------------------------------
Erwartetes Verhalten
-----------------------------------------------------------

1) Vor der Objekterzeugung zeigt BeispielKlasse.__dict__ die
   Klassenvariable „wert“ mit dem Startwert 1.

2) Nach Erzeugung eines Objekts hat die Klasse einen neuen Wert
   für „wert“, da der Konstruktor BeispielKlasse.wert = val setzt.

3) Das Objekt hat weiterhin KEINE Instanzvariablen, daher ist
   objekt.__dict__ leer {}.
"""

class BeispielKlasse:
    wert = 1                                          # Klassenvariable

    def __init__(self, neuer_wert):
        BeispielKlasse.wert = neuer_wert              # Klassenvariable ändern


# Ausgabe VOR dem ersten Objekt
print(BeispielKlasse.__dict__)                        # zeigt alle Klassendaten
print("-----------------------")
# erstes Objekt erzeugen → ändert Klassenvariable
objekt = BeispielKlasse(2)

print(BeispielKlasse.__dict__)                        # zeigt aktualisierten Wert der Klassenvariable
print(objekt.__dict__)                                # leer, keine Instanzvariablen
