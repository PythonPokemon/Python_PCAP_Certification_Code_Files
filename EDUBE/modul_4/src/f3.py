"""
Generatoren – wo man sie findet (Fortsetzung)
Iterator in einer anderen Klasse „eingebaut“ (PCAP-relevant)

-----------------------------------------------------------
Was passiert in diesem Beispiel?
-----------------------------------------------------------
Diesmal ist der Iterator NICHT die Klasse selbst.
Stattdessen:

• Die Klasse Fib implementiert das vollständige Iterator-Protokoll:
  - __iter__()
  - __next__()

• Die Klasse Class besitzt KEIN eigenes Iterationsverhalten,
  sondern enthält ein Fib-Objekt als internes Attribut.

-----------------------------------------------------------
Warum funktioniert die for-Schleife trotzdem?
-----------------------------------------------------------
Eine for-Schleife fragt IMMER zuerst:

1) „Hast du eine __iter__()-Methode?“  
   → Ja, Class hat __iter__().

2) Class.__iter__() gibt NICHT sich selbst zurück,  
   sondern das eingebaute Fib-Objekt.

3) Fib ist ein vollständiger Iterator (hat __next__()).

Ergebnis:
• Die for-Schleife iteriert über das Fib-Objekt,
  obwohl sie ursprünglich über ein Class-Objekt gestartet wurde.

-----------------------------------------------------------
Wofür ist das nützlich?
-----------------------------------------------------------
Diese Technik erlaubt:

• Eine Klasse kann andere Objekte „iterierbar machen“  
  (Komposition statt Vererbung)

• Du kannst entscheiden, WELCHEN Iterator eine Klasse zurückgibt  
  (z. B. verschiedene View-Modi, Filter, Pagination)

• Eine Klasse muss nicht selbst __next__() besitzen,
  solange sie einen Iterator bereitstellt.

-----------------------------------------------------------
Ablauf im Beispiel:
-----------------------------------------------------------
1. object = Class(8) erzeugt intern Fib(8)
2. for i in object:
       → ruft Class.__iter__() auf
       → gibt das Fib-Objekt zurück
3. Python ruft wiederholt Fib.__next__() auf
4. Ausgabe entspricht derselben Fibonacci-Reihe wie im vorherigen Beispiel

-----------------------------------------------------------
Typische PCAP-Prüfungsfalle:
-----------------------------------------------------------
• Eine Klasse IST NICHT automatisch ein Iterator,
  nur weil sie __iter__() implementiert hat.

• Ein Iterator MUSS __next__() besitzen.

• Eine Klasse ohne __next__() kann trotzdem in for verwendet werden,
  WENN __iter__() ein objekt MIT __next__() zurückgibt.
"""

class Fib:
    def __init__(self, nn):
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("Fib iter")                # zeigt, dass der Iterator aus Fib stammt
        return self

    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in (1, 2):
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


class Class:
    def __init__(self, n):
        self.__iter = Fib(n)             # eingebauter Iterator

    def __iter__(self):
        print("Class iter")              # zeigt, dass FOR zuerst Class iteriert
        return self.__iter               # gibt den echten Iterator zurück!


object = Class(8)

for i in object:
    print(i)
