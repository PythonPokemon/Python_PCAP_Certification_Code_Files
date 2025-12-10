"""
Die Caesar-Chiffre: Verschlüsselung einer Nachricht

Die Caesar-Chiffre ist eine sehr einfache Verschlüsselungsmethode:
Jeder Buchstabe wird durch den nächsten Buchstaben im Alphabet ersetzt.
A → B, B → C, ..., Y → Z, Z → A

Vereinfachungen für dieses Programm:
• Es werden nur lateinische Buchstaben verarbeitet
• Alle Buchstaben werden automatisch in Großbuchstaben umgewandelt
• Nicht-Buchstaben (z.B. Zahlen, Leerzeichen, Satzzeichen) werden ignoriert

Ablauf des Algorithmus:
1) Eingabe der Nachricht
2) Vorbereitung eines leeren Ergebnis-Strings
3) Iteration über jedes Zeichen
4) Wenn das Zeichen kein Buchstabe ist → überspringen
5) Buchstabe in Großbuchstaben umwandeln
6) Unicode-Code um 1 erhöhen
7) Wenn der Code über 'Z' hinausgeht → wieder zu 'A' springen
8) Den verschlüsselten Buchstaben an das Ergebnis anhängen
9) Ergebnis ausgeben
"""
# Caesar cipher – Demonstration des Algorithmus:
text = input("Enter your message: ")
cipher = ''

for char in text:
    if not char.isalpha():      # Nicht-Buchstaben überspringen
        continue
    char = char.upper()         # Immer Großbuchstaben verwenden
    code = ord(char) + 1        # Nächster Buchstabe
    if code > ord('Z'):         # Falls wir hinter Z sind → zurück zu A
        code = ord('A')
    cipher += chr(code)         # Zeichen an die verschlüsselte Nachricht anhängen

print(cipher)
