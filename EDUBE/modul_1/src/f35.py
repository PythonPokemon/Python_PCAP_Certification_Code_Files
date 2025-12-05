"""
Wir bauen uns erst eine sichere Pfad-Basis:
-----------------------------------------------------------------
import os, sys

BASE = os.path.dirname(os.path.abspath(__file__))  
MODULE_PATH = os.path.join(BASE, "f32_gruppierte_module")
sys.path.append(MODULE_PATH)
-----------------------------------------------------------------
Damit funktionieren alle Imports immer, egal von wo du startest.
"""

import os, sys

# 📌 Absoluten Pfad zum Modulordner setzen
BASE = os.path.dirname(os.path.abspath(__file__))                   # Ordner von f35.py
MODULE_PATH = os.path.join(BASE, "f32_gruppierte_module")           # Paketordner
sys.path.append(MODULE_PATH)                                        # Zu sys.path hinzufügen

# 📌 Jetzt absolut importieren
import extra.good.best.sigma
from extra.good.best.tau import funT

# 📌 Funktionen ausgeben
print(extra.good.best.sigma.funS())
print(funT())

"""
💬 Smart-Kommentar:

    extra.good.best.sigma ist der vollständige Paketpfad
    funT wird direkt importiert
    Absoluter Pfad garantiert keine Importfehler
"""