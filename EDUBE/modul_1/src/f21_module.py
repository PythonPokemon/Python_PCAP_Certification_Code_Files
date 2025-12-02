"""
Das ist eine module datei zum importieren
"""

print("I like to be a module.")

"""
Kannst du Unterschiede zwischen einem Modul und einem gewöhnlichen Skript bemerken? Bisher gibt es keine.
Es ist möglich, diese Datei wie jedes andere Skript auszuführen. 
Probier es selbst aus.
"""

print(__name__) # wenn man __name__ in der datei ausführt, dann wird der name der datei auf __main__ gesetzt vom konstruktor
                # bedeutet wenn das modul dann von einer extenen datei aufgerufen wird, dann wird der name dieser datei angezeigt!

"""
Wir können sagen:

Wenn du eine Datei direkt ausführst, wird ihre Variable auf gesetzt __name____main__;
Wenn eine Datei als Modul importiert wird, wird ihre Variable auf den Dateinamen gesetzt (ausgenommen .py__name__)
"""

counter = 0
# bsp.
if __name__ == "__main__":
    print("Ich werde 'innerhalb der Datei' als modul aufgerufen")
else:
    print("Ich werde 'außerhalb der datei' als modul aufgerufen")

"""
Dies geschieht, indem man dem Namen der Variablen mit (einem Unterstrich) oder (zwei Unterstrichen) (zwei Unterstrichen) voranstellt, 
aber denken Sie daran, dass es nur eine Konvention ist. Die Nutzer deines Moduls könnten es befolgen oder auch nicht.___
"""