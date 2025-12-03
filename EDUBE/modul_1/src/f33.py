"""
Dein erstes Paket: Schritt 4
Es gibt zwei Fragen zu beantworten:

Wie verwandelt man einen solchen Baum (eigentlich einen Unterbaum) in ein echtes Python-Paket (mit anderen Worten, wie überzeugt man Python davon, dass ein solcher Baum nicht nur ein Haufen Junk-Dateien, sondern eine Sammlung von Modulen ist)?
Wo platziert man den Unterbaum, um ihn für Python zugänglich zu machen?
Die erste Frage hat eine überraschende Antwort: Pakete, ähnlich wie Module, benötigen möglicherweise eine Initialisierung.

Die Initialisierung eines Moduls erfolgt durch einen ungebundenen Code (kein Teil einer Funktion), der sich in der Datei des Moduls befindet. Da ein Paket keine Datei ist, ist diese Technik für die Initialisierung von Paketen nutzlos.

Du musst stattdessen einen anderen Trick verwenden – Python erwartet, dass sich eine Datei mit einem sehr einzigartigen Namen im Paketordner befindet: __init__.py.

Der Inhalt der Datei wird ausgeführt, wenn eines der Module des Pakets importiert wird. Wenn du keine speziellen Initialisierungen möchtest, kannst du die Datei leer lassen, aber du darfst sie nicht weglassen.


"""
"""
Projektstruktur (Paket- und Modul-Architektur)
-----------------------------------------------------------------------------
EDUBE/
│
└── modul_1/
    │
    ├── img/
    │     └── (Bilder, Ressourcen …)
    │
    └── src/
          ├── __pycache__/          (automatisch generierte Dateien)
          │
          └── f32_gruppierte_module/
                │
                ├── extra/
                └── iota.py
                │      ├── good/
                |      |     ├── alpha.py
                │      │     ├── beta.py
                │      │     └── best/
                │      │           ├── sigma.py
                │      │           ├── tau.py
                │      │
                │      └── ugly/
                │             ├── omega.py
                │             └── psi.py
                │
                └── (weitere Module falls benötigt)

-----------------------------------------------------------------------------
Hinweis:
- Um auf ein Modul außerhalb seines Pakets zuzugreifen, muss der vollständige
  Paketpfad angegeben werden.

  Beispiel:
      import EDUBE.modul_1.src.f32_gruppierte_module.extra.good.best.sigma
-----------------------------------------------------------------------------
"""


import f32_gruppierte_module.extra.good.best.sigma
