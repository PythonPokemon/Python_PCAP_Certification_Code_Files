"""
Listenverständnisse (List Comprehensions)

-----------------------------------------------------------
Was ist eine Listenverständnis?
-----------------------------------------------------------
• Kurzschreibweise zum Erzeugen von Listen
• Spart Schleifen-Code
• Erzeugt Listen „in einem Zug“
• Wird häufig in EDUBE/PCAP genutzt

-----------------------------------------------------------
Vergleich:
1. Normale Schleife
2. Listenverständnis
-----------------------------------------------------------
Beide Varianten erzeugen dieselben Werte.
"""

liste_1 = []                                  # Leere Liste erzeugen

for exponent in range(6):                     # Exponenten 0..5 durchlaufen
    liste_1.append(10 ** exponent)            # 10^exponent anhängen

liste_2 = [10 ** exponent for exponent in range(6)]   # gleiche Liste per Comprehension

print(liste_1)                                # Ausgabe: [1,10,100,1000,10000,100000]
print(liste_2)                                # identische Ausgabe


"""
-----------------------------------------------------------
⚠️ WICHTIG (EDUBE / PCAP)
-----------------------------------------------------------
• Listenverständnisse ersetzen NICHT die for-Schleife – sie verkürzen nur den Code.
• Beide Varianten erzeugen dieselbe Liste.
• Die Comprehension ist kompakter, aber nicht magisch – Python führt intern trotzdem eine Schleife aus.

-----------------------------------------------------------
Typische Prüfungsfalle:
-----------------------------------------------------------
Frage: „Sind list_1 und list_2 gleich?“ → JA  
Beide enthalten IDENTISCHE Werte und sind echte Listen.

Frage: „Warum ist die zweite Variante besser?“  
→ Kürzer, lesbarer, pythonischer.
"""
