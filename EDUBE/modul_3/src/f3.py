"""
Der Stapel – objektorientierter Ansatz: Fortsetzung
Alles, was im Konstruktor (__init__) dem Parameter self hinzugefügt wird,
wird automatisch Teil des neuen Objekts.

Das bedeutet:
• Du kannst beliebige Eigenschaften definieren.
• Diese Eigenschaften bleiben bestehen, solange das Objekt existiert.
• Eigenschaften können von außen gelesen/geschrieben werden,
  sofern man sie nicht „versteckt“.

Nun richten wir die interne Speicherstruktur des Stacks ein.
Wir nennen sie: stapel_liste

Beispiel:
---------------------------------
class Stapel:
    def __init__(self):
        self.stapel_liste = []
---------------------------------

Was passiert hier?

1) self.stapel_liste wird zum ersten Mal erzeugt.
   → Dadurch erhält jedes Objekt SEINE EIGENE Liste.

2) Die Punkt-Notation (object.eigenschaft) ermöglicht den Zugriff:
       objekt.stapel_liste
   Wichtig:
   • KEINE Klammern verwenden! (sonst wäre es ein Methodenaufruf)
   • Punkt-Notation = Standardzugriff auf Objektattribute

3) Der folgende Code erzeugt ein Stapel-Objekt
   und prüft die aktuelle Länge seiner internen Liste.
   Da der Stapel leer ist, lautet die Ausgabe: 0

Hinweis:
Obwohl es funktioniert, ist es **nicht erwünscht**, dass
stapel_liste von außen sichtbar ist.
Wir wollen diese interne Struktur eigentlich verbergen.
"""
# Objektorientierter Stack – interne Liste sichtbar
class Stapel:
    def __init__(self):
        self.stapel_liste = []   # interne Speicherliste für den Stack


# Objekt erzeugen
stapel_objekt = Stapel()

# Länge der internen Liste prüfen
print(len(stapel_objekt.stapel_liste))   # Ausgabe: 0
