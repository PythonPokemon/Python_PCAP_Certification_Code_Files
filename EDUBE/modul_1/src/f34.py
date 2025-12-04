"""
✅ KURZ & KLAR: Was zeigt das Bild?

Du hast ein externes Paket („packages“-Ordner), das nicht im selben Verzeichnis liegt wie deine main2.py.

➡ Deshalb musst du Python erst sagen:
„Bitte suche auch in ..\packages nach Modulen!“

Das passiert mit:
path.append('..\\packages')

"""

"""
🧪 Wenn du es trotzdem global starten willst

(Du bist oft in OneDrive → macht Probleme)

Dann nutze den absoluten Pfad:
"""

from sys import path
path.append(r"C:\Users\Jakob.Derzapf\OneDrive - Amadeus Fire AG\Dokumente\Python_PCAP_Certification_Code_Files\EDUBE\modul_1\src\f32_gruppierte_module")

import extra.iota
print(extra.iota.funI())
