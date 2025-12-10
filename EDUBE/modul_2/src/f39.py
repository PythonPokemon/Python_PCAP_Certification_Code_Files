"""
Der IBAN-Validator
Dieses Programm implementiert den (vereinfacht dargestellten) Prüfalgorithmus,
der in Europa zur Validierung von IBAN-Kontonummern genutzt wird.

Eine IBAN besteht aus:
• einem zweibuchstabigen Ländercode (z.B. DE, FR, GB)
• zwei Prüfziffern
• der eigentlichen Kontonummer (bis zu 30 Zeichen)

Der vollständige Prüfprozess (vereinfacht):
1) Die IBAN darf nur aus Buchstaben und Ziffern bestehen (Leerzeichen vorher entfernen).
2) Länge prüfen: mindestens 15 Zeichen, maximal 31 Zeichen.
3) Die ersten vier Zeichen (Ländercode + Prüfziffern) ans Ende verschieben.
4) Alle Buchstaben in Großbuchstaben umwandeln.
5) Jeden Buchstaben durch zwei Ziffern ersetzen:
   A = 10, B = 11, ..., Z = 35
6) Die resultierende Zeichenkette als große Ganzzahl interpretieren.
7) Wenn diese Zahl modulo 97 den Rest 1 ergibt, ist die IBAN gültig.

Die folgenden Beispiele sind gültige IBANs:
• GB72HBZU70067212125300   (britisch)
• FR7630003036200002021690750   (französisch)
• DE02100100100152517108        (deutsch)
"""

# IBAN Validator – eingedeutschte Version
iban = input("Bitte geben Sie die IBAN ein: ")
iban = iban.replace(' ', '')  # Leerzeichen entfernen

# Schritt 1: Grundvalidierung
if not iban.isalnum():
    print("Sie haben ungültige Zeichen eingegeben.")
elif len(iban) < 15:
    print("Die eingegebene IBAN ist zu kurz.")
elif len(iban) > 31:
    print("Die eingegebene IBAN ist zu lang.")
else:
    # Schritt 2: Die ersten vier Zeichen ans Ende verschieben + Großbuchstaben erzwingen
    iban = (iban[4:] + iban[0:4]).upper()

    # Schritt 3: Buchstaben durch zweistellige Zahlen ersetzen
    iban_ersetzt = ""
    for zeichen in iban:
        if zeichen.isdigit():
            iban_ersetzt += zeichen
        else:
            iban_ersetzt += str(10 + ord(zeichen) - ord('A'))

    # Schritt 4: In Ganzzahl umwandeln und Modulo 97 prüfen
    iban_zahl = int(iban_ersetzt)

    if iban_zahl % 97 == 1:
        print("Die IBAN ist gültig.")
    else:
        print("Die IBAN ist ungültig.")
