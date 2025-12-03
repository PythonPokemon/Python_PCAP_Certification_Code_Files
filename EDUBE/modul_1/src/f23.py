"""
wie Python nach Modulen sucht. 
Es gibt eine spezielle Variable (eigentlich eine Liste), die alle Orte (Ordner/Verzeichnisse) speichert, die durchsucht werden, 
um ein Modul zu finden, das von der Importinstruktion angefordert wurde.

Python durchsucht diese Ordner in der Reihenfolge, in der sie in der Liste aufgeführt sind 
– wenn das Modul in keinem dieser Verzeichnisse gefunden werden kann, schlägt der Import fehl.

Andernfalls wird der erste Ordner mit einem Modul mit dem gewünschten Namen berücksichtigt 
(wenn einer der verbleibenden Ordner ein Modul mit diesem Namen enthält, wird er ignoriert).
---------------------------------------------------------------------------------------------------------------------------------
Die Variable heißt , und sie ist über das Modul mit dem Namen zugänglich. So können Sie seinen regulären Wert überprüfen: pathsys

C:\Users\user
C:\Users\user\AppData\Local\Programs\Python\Python36-32\python36.zip
C:\Users\user\AppData\Local\Programs\Python\Python36-32\DLLs
C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib
C:\Users\user\AppData\Local\Programs\Python\Python36-32
C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages
---------------------------------------------------------------------------------------------------------------------------------
"""

import sys

for p in sys.path:
    print(p)

