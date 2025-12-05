"""
dasselbe wie f35.py, aber mit Aliasing == spitzname

💬 Smart-Kommentare:

    as sig → sigma-Modul bekommt Kurzbezeichnung
    as alp → alpha-Modul bekommt Kurzbezeichnung
    Aufruf über Modulnamen (sig.funS())
"""

import os, sys

# 📌 Absoluten Modulpfad aktivieren
BASE = os.path.dirname(os.path.abspath(__file__))
MODULE_PATH = os.path.join(BASE, "f32_gruppierte_module")
sys.path.append(MODULE_PATH)

# 📌 Aliasing wie im Beispiel
import extra.good.best.sigma as sig
import extra.good.alpha as alp

# 📌 Funktionen aufrufen
print(sig.funS())
print(alp.funA())
