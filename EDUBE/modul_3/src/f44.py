"""
Single Inheritance vs. Multiple Inheritance
(Einfache Vererbung vs. Mehrfachvererbung)

-----------------------------------------------------------
Grundsätzliches
-----------------------------------------------------------
In Python ist Mehrfachvererbung technisch erlaubt.
Eine Klasse kann also von mehr als einer Superklasse erben.

WICHTIG:
Nur weil es möglich ist, heißt das nicht, dass es sinnvoll ist.

-----------------------------------------------------------
Single Inheritance (einfache Vererbung)
-----------------------------------------------------------
Bei einfacher Vererbung hat eine Klasse genau EINE Superklasse.

Vorteile:
- einfacher Aufbau
- leichter zu verstehen
- besser wartbar
- geringere Fehleranfälligkeit
- klares Verhalten beim Überschreiben von Methoden

Merksatz:
👉 Single Inheritance ist fast immer die bessere Wahl.

-----------------------------------------------------------
Multiple Inheritance (Mehrfachvererbung)
-----------------------------------------------------------
Bei Mehrfachvererbung erbt eine Klasse von ZWEI oder mehr Superklassen.

Nachteile:
- deutlich komplexer
- schwer nachvollziehbar, woher Methoden/Eigenschaften stammen
- hohes Risiko für Namenskonflikte
- Überschreiben von Methoden wird unübersichtlich
- super() kann mehrdeutig werden (MRO-Probleme)

-----------------------------------------------------------
Single Responsibility Principle (SRP)
-----------------------------------------------------------
Das SRP besagt:
👉 Eine Klasse sollte genau EINE Verantwortung haben.

Mehrfachvererbung verletzt dieses Prinzip häufig,
weil eine Klasse Verhalten aus mehreren, unabhängigen Klassen mischt,
die nichts voneinander wissen.

-----------------------------------------------------------
Empfehlung (prüfungsrelevant)
-----------------------------------------------------------
- Verwende Single Inheritance als Standard
- Nutze Multiple Inheritance nur im absoluten Ausnahmefall
- Wenn mehrere Fähigkeiten benötigt werden:
  👉 Komposition ist meist die bessere Lösung

Merksatz für Prüfung & Praxis:
👉 „Lieber Komposition statt Mehrfachvererbung“
"""
