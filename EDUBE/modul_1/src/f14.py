"""
Es gibt ein Modul, das dir eine Möglichkeit bietet, 
herauszufinden, wo du bist und welche Komponenten für dich funktionieren. 
Das Modul heißt Plattform. 

Selected functions from the platform module
The platform function
--------------------------------------------------------------------------------------------------------------------
Das Modul ermöglicht Ihnen den Zugriff auf die zugrunde liegenden Plattformdaten, also Hardware-, Betriebssystem- 
und Interpreter-Versionsinformationen.platform

Es gibt eine Funktion, die Ihnen alle zugrundeliegenden Schichten auf einen Blick zeigen kann, genannt , ebenfalls . 
Es gibt einfach eine Zeichenkette zurück, die die Umgebung beschreibt; 
daher richtet sich seine Ausgabe eher an Menschen als an automatisierte Verarbeitung (das werden Sie bald sehen).
--------------------------------------------------------------------------------------------------------------------
"""

from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))

platform(aliased = False, terse = False)
print(platform)
