"""
Eigene Ausnahmen erstellen – Fortsetzung
Custom-Exception-Hierarchie (PizzaError / TooMuchCheeseError)

-----------------------------------------------------------
Problem: Erweiterte Fehlerbehandlung in eigenen Modulen
-----------------------------------------------------------
Wir möchten eigene Ausnahmen definieren, um Fehler in einem
domänenspezifischen Kontext (z. B. Pizzeria-Simulation)
klarer zu unterscheiden.

Beispiel:
• Ungültige Pizza → PizzaError
• Zu viel Käse     → TooMuchCheeseError

Dadurch können Fehler gezielt abgefangen werden.

-----------------------------------------------------------
Schwäche der ursprünglichen Lösung
-----------------------------------------------------------
Wenn der Konstruktor der eigenen Ausnahme Pflichtargumente
verlangt (pizza, message, …), kann raise PizzaError ohne
Argumente NICHT funktionieren.

→ Lösung: Defaultwerte für alle Parameter setzen.

So bleiben beide Varianten gültig:
• raise PizzaError
• raise PizzaError("margherita", "Fehlerbeschreibung")

-----------------------------------------------------------
Was muss man bei try/except beachten?
-----------------------------------------------------------
Wenn except TooMuchCheeseError entfernt wird:
→ Jede dieser Ausnahmen wird als PizzaError behandelt  
  (weil TooMuchCheeseError eine Unterklasse IST).

Wenn except PizzaError entfernt wird:
→ TooMuchCheeseError wird korrekt abgefangen  
→ PizzaError NICHT → Programm bricht ab

-----------------------------------------------------------
⚠️ WICHTIG FÜR EDUBE / PCAP
-----------------------------------------------------------
• Eigene Exceptions IMMER von Exception ableiten  
• Reihenfolge der except-Zweige ist entscheidend:
  Unterklassen müssen VOR Oberklassen stehen
• Konstruktorparameter brauchen Defaults, sonst:
  raise MyError  führt zu TypeError

-----------------------------------------------------------
Typische Prüfungsfallen
-----------------------------------------------------------
• Ausnahme wird nicht gefangen, weil except-Reihenfolge falsch ist
• Ausnahme kann nicht erzeugt werden, weil Konstruktor-Args fehlen
• Unterklasse überschattet Oberklasse, wenn except falsch sortiert ist
"""

class PizzaFehler(Exception):
    def __init__(self, pizza='unbekannt', nachricht=''):
        Exception.__init__(self, nachricht)
        self.pizza = pizza                              # betroffene Pizza

class ZuVielKaeseFehler(PizzaFehler):
    def __init__(self, pizza='unbekannt', kaese='>100', nachricht=''):
        PizzaFehler.__init__(self, pizza, nachricht)    # Nachricht an Superklasse
        self.kaese = kaese                              # zu viel verwendeter Käse

def pizza_herstellen(pizza, kaese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaFehler                               # ungültige Pizza
    if kaese > 100:
        raise ZuVielKaeseFehler                         # zu viel Käse
    print("Pizza fertig!")

for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        pizza_herstellen(pz, ch)
    except ZuVielKaeseFehler as zkf:
        print(zkf, ':', zkf.kaese)
    except PizzaFehler as pf:
        print(pf, ':', pf.pizza)
