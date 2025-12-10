"""
Ausnahmen: Fortsetzung
Dieses Beispiel zeigt einen weiteren sehr häufigen Fehler:
Der Zugriff auf ein Listenelement, das nicht existiert.

Wenn eine Liste leer ist und man versucht, auf ein Element wie my_list[0]
zuzugreifen, erzeugt Python die Ausnahme:

IndexError: list index out of range

Dies bedeutet:
• Der angeforderte Index existiert nicht in der Liste.
• Der gültige Indexbereich wird überschritten.
"""
# Beispielcode, der einen IndexError auslöst:
meine_liste = []
x = meine_liste[0]   # Versuch, auf ein nicht vorhandenes Element zuzugreifen
