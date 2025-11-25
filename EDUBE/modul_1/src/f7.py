"""
Working with standard modules
Die Funktion liefert eine alphabetisch sortierte Liste zurück, die alle Namen aller Entitäten enthält, 
die im Modul verfügbar sind, identifiziert durch einen Namen, der als Argument an die Funktion übergeben wird:

dir(module)
"""

import math

for name in dir(math):
    print(name, end="\t")


# ausgabe:
"""
__doc__	__loader__	__name__	__package__	__spec__	acos	acosh	asin	asinh	atan	
atan2	atanh	ceil    copysign	cos	cosh	degrees	e	erf	erfc	exp	expm1	fabs	
factorial	floor	fmod	frexp	fsum	gamma	hypot	isfinite	isinf	isnan	ldexp	
lgamma	log	log10	log1p	log2	modf	pi	pow	radians	sin	sinh	sqrt	tan	tanh	trunc	
"""