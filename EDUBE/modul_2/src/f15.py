"""
Operations on strings: the list() function
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Die Funktion nimmt ihr Argument (eine Zeichenkette) und erstellt eine neue Liste, die alle Zeichen der Zeichenkette enthält, jeweils eines pro Listenelement.list()

Hinweis: 
Es handelt sich nicht strikt um eine Zeichenkettenfunktion – sie kann eine neue Liste aus vielen anderen Entitäten erstellen 
(z. B. aus Tupeln und Wörterbüchern).list()
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
# Demonstrating the list() function:
print(list("abcabc"))


"""
Operations on strings: the count() method
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Die Methode zählt alle Vorkommen des Elements innerhalb der Sequenz. Das Fehlen solcher Elemente verursacht keine Probleme.count()
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))
