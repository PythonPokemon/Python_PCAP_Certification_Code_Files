"""
Sorting – Sortieren von Listen
Vergleiche hängen eng mit dem Sortieren zusammen. Sortieren bedeutet,
dass Elemente anhand ihrer Vergleichsregeln geordnet werden.

Python bietet zwei Hauptmöglichkeiten, um Listen zu sortieren.

1) Die Funktion sorted()
   • erstellt eine NEUE sortierte Liste
   • das Original bleibt unverändert

Beispiel:
"""
# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_sorted = sorted(first_greek)

print(first_greek)          # Original bleibt unverändert
print(first_greek_sorted)   # Neue sortierte Liste
print()


"""
2) Die Methode sort()
   • sortiert die Liste direkt (in-place)
   • es wird KEINE neue Liste erzeugt

Beispiel:
"""
# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)     # Original

second_greek.sort()
print(second_greek)     # Sortierte Version







"""

"""

