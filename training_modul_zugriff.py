"""
Projektstruktur (Paket- und Modul-Architektur)
-----------------------------------------------------------------------------
EDUBE/
│
└── modul_1/
    │
    ├── img/
    │     └── (Bilder, Ressourcen …)
    │
    └── src/
          ├── __pycache__/          (automatisch generierte Dateien)
          │
          └── f32_gruppierte_module/
                │
                ├── extra/
                └── iota.py
                │      ├── good/
                |      |     ├── alpha.py
                │      │     ├── beta.py
                │      │     └── best/
                │      │           ├── sigma.py
                │      │           ├── tau.py
                │      │
                │      └── ugly/
                │             ├── omega.py
                │             └── psi.py
                │
                └── (weitere Module falls benötigt)

-----------------------------------------------------------------------------
Hinweis:
- Um auf ein Modul außerhalb seines Pakets zuzugreifen, muss der vollständige
  Paketpfad angegeben werden.

  Beispiel:
      import EDUBE.modul_1.src.f32_gruppierte_module.extra.good.best.sigma
-----------------------------------------------------------------------------
"""

# hier muss man den kompletten pfad angeben, da die testdatei außerhalb der modul ordnern ist!
#import EDUBE.modul_1.src.f32_gruppierte_module.extra.good.best.sigma

# normaler import
from EDUBE.modul_1.src.f32_gruppierte_module.extra.good.best import sigma

sigma.funS()

