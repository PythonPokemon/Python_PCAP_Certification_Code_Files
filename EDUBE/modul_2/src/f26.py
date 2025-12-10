"""
Die replace()-Methode
Die Zwei-Parameter-Methode liefert eine Kopie des ursprünglichen Strings, 
in der alle Vorkommen des ersten Arguments durch das zweite Argument ersetzt wurden.
"""
# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))   # achtung es werden die exacten strint literale getauscht!
print("Apple juice".replace("juice", ""))




"""
Wenn das zweite Argument eine leere Zeichenkette ist, bedeutet das Ersetzen tatsächlich das Entfernen der Zeichenkette des ersten Arguments. 
Welche Art von Magie entsteht, wenn das erste Argument eine leere Saite ist?
"""
# bsp. 2
text = "ABC"
print(text.replace("", "-"))



"""
Die Drei-Parameter-Variante verwendet das dritte Argument (eine Zahl), um die Anzahl der Ersetzungen zu begrenzen.
"""
# bsp. 3
print("This is it!".replace("is", "are", 1))    # bedeutet das 'is' vorkommen  'einmal' vertauscht wird
print("This is it!".replace("is", "are", 2))    # bedeutet das 'is' vorkommen  'zweimal' vertauscht wird

