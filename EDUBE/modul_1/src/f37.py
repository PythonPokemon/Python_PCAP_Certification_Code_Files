

import os, sys

# 📌 Absoluter Pfad zum Modulpaket
BASE = os.path.dirname(os.path.abspath(__file__))
MODULE_PATH = os.path.join(BASE, "f32_gruppierte_module")
sys.path.append(MODULE_PATH)

# 📌 Importieren wie in Edube Schritt 9
import extra.good.best.sigma as sig
import extra.good.alpha as alp
# from extra.ugly.omega import funO
# from extra.ugly.psi import funP

# 📌 Ausgabe
print(sig.funS())
print(alp.funA())
# print(funO())
# print(funP())
