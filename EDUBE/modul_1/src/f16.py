"""
Selected functions from the platform module: continued
The processor function

The processor() function returns a string filled with the real processor name (if possible).

Once again, we ran the sample program on three different platforms:
"""

from platform import processor

print(processor())  # gibt den prozessor aus
