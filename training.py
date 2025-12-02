liste = []  # leere Liste

while True:
    eingabe = input("Gib einen Wert ein (oder 'stop' zum Beenden): ")

    if eingabe == "stop":
        break

    liste.append(eingabe)  # Wert an Liste anhängen

print("Die gespeicherten Werte in der liste sind: ", liste, len(liste))
