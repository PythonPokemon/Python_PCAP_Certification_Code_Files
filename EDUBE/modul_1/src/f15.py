"""
Selected functions from the platform module: continued
The machine function

Sometimes, you may just want to know the generic name of the processor which runs your OS together with Python and your code - a function named machine() will tell you that. 
As previously, the function returns a string.
"""

from platform import machine

print(machine())    # gibt das OS aus
