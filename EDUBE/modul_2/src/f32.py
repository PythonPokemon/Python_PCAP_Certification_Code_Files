"""
Comparing / Vergleich von strings
Die Python-Zeichenketten können mit denselben Operatoren verglichen werden, die auch in Bezug auf Zahlen verwendet werden.
--------------------------------------------------------------------------------------------------------------------------
Schau dir diese Operatoren an – sie können alle auch Strings vergleichen:

==
!=
>
>=
<
<=
--------------------------------------------------------------------------------------------------------------------------
Es gibt ein "aber" – die Ergebnisse solcher Vergleiche können manchmal etwas überraschend sein. 
Vergiss nicht, dass Python sich subtiler linguistischer Probleme nicht bewusst ist (das kann es in keiner Weise sein) – 
es vergleicht nur Codepunktwerte Zeichen für Zeichen.

Die Ergebnisse einer solchen Operation sind manchmal erstaunlich. Fangen wir mit den einfachsten Fällen an.

Zwei Strings sind gleich, wenn sie aus denselben Zeichen in derselben Reihenfolge bestehen. 
Auf dieselbe Weise sind zwei Strings nicht gleich, wenn sie nicht aus denselben Zeichen in derselben Reihenfolge bestehen.
--------------------------------------------------------------------------------------------------------------------------
"""
# gleichheits vergleich
print('alpha' == 'alpha')
print('alpha' != 'Alpha')
print()


"""
Wenn man zwei Zeichenketten unterschiedlicher Länge vergleicht und die kürzere identisch mit dem Anfang der längeren ist, 
gilt die längere Saite als größer.
"""
# längen vergleich mit <>
print('alpha' < 'alphabet')
print()


"""
Der String-Vergleich ist immer groß- und kleinschreibungssensitiv (Großbuchstaben werden als kleiner als kleiner als kleingeschrieben gewertet)
weil großund kleinbuchstaben dem ASCII-wert dezimal unterschiedlich sind:
"""
print('beta' > 'Beta') 

# kleines b == dezimal 98 
# großes  B == dezimal 66

"""
🧠 Was passiert bei print("beta" > "Beta")?

Python vergleicht Zeichenketten lexikografisch (wie im Wörterbuch), also:

1️⃣ erstes Zeichen mit erstem Zeichen
2️⃣ wenn gleich → nächstes Zeichen
3️⃣ Vergleich endet, sobald ein Unterschied gefunden wurde

UND:

🔑 Python vergleicht nicht die Summe aller Zeichen, sondern Zeichen für Zeichen.

Das ist der wichtigste Punkt
"""


"""
-------------------------------------------------------------------------
https://www.ascii-code.com/de
-------------------------------------------------------------------------
Großbuchstaben von dezimal 65 - 90 == A - Z
-------------------------------------------------------------------------
65	101	41	01000001	A	&#65;	 	Großbuchstabe A
66	102	42	01000010	B	&#66;	 	Großbuchstabe B
67	103	43	01000011	C	&#67;	 	Großbuchstabe C
68	104	44	01000100	D	&#68;	 	Großbuchstabe D
69	105	45	01000101	E	&#69;	 	Großbuchstabe E
70	106	46	01000110	F	&#70;	 	Großbuchstabe F
71	107	47	01000111	G	&#71;	 	Großbuchstabe G
72	110	48	01001000	H	&#72;	 	Großbuchstabe H
73	111	49	01001001	I	&#73;	 	Großbuchstabe I
74	112	4A	01001010	J	&#74;	 	Großbuchstabe J
75	113	4B	01001011	K	&#75;	 	Großbuchstabe K
76	114	4C	01001100	L	&#76;	 	Großbuchstabe L
77	115	4D	01001101	M	&#77;	 	Großbuchstabe M
78	116	4E	01001110	N	&#78;	 	Großbuchstabe N
79	117	4F	01001111	O	&#79;	 	Großbuchstabe O
80	120	50	01010000	P	&#80;	 	Großbuchstabe P
81	121	51	01010001	Q	&#81;	 	Großbuchstabe Q
82	122	52	01010010	R	&#82;	 	Großbuchstabe R
83	123	53	01010011	S	&#83;	 	Großbuchstabe S
84	124	54	01010100	T	&#84;	 	Großbuchstabe T
85	125	55	01010101	U	&#85;	 	Großbuchstabe U
86	126	56	01010110	V	&#86;	 	Großbuchstabe V
87	127	57	01010111	W	&#87;	 	Großbuchstabe W
88	130	58	01011000	X	&#88;	 	Großbuchstabe X
89	131	59	01011001	Y	&#89;	 	Großbuchstabe Y
90	132	5A	01011010	Z	&#90;	 	Großbuchstabe Z
-------------------------------------------------------------------------
Großbuchstaben von dezimal 65 - 90 == A - Z
-------------------------------------------------------------------------
97	141	61	01100001	a	&#97;	 	Kleinbuchstaben a
98	142	62	01100010	b	&#98;	 	Kleinbuchstaben b
99	143	63	01100011	c	&#99;	 	Kleinbuchstaben c
100	144	64	01100100	d	&#100;	 	Kleinbuchstaben d
101	145	65	01100101	e	&#101;	 	Kleinbuchstaben e
102	146	66	01100110	f	&#102;	 	Kleinbuchstaben f
103	147	67	01100111	g	&#103;	 	Kleinbuchstaben g
104	150	68	01101000	h	&#104;	 	Kleinbuchstaben h
105	151	69	01101001	i	&#105;	 	Kleinbuchstaben i
106	152	6A	01101010	j	&#106;	 	Kleinbuchstaben j
107	153	6B	01101011	k	&#107;	 	Kleinbuchstaben k
108	154	6C	01101100	l	&#108;	 	Kleinbuchstaben l
109	155	6D	01101101	m	&#109;	 	Kleinbuchstaben m
110	156	6E	01101110	n	&#110;	 	Kleinbuchstaben n
111	157	6F	01101111	o	&#111;	 	Kleinbuchstaben o
112	160	70	01110000	p	&#112;	 	Kleinbuchstaben p
113	161	71	01110001	q	&#113;	 	Kleinbuchstaben q
114	162	72	01110010	r	&#114;	 	Kleinbuchstaben r
115	163	73	01110011	s	&#115;	 	Kleinbuchstaben s
116	164	74	01110100	t	&#116;	 	Kleinbuchstaben t
117	165	75	01110101	u	&#117;	 	Kleinbuchstaben u
118	166	76	01110110	v	&#118;	 	Kleinbuchstaben v
119	167	77	01110111	w	&#119;	 	Kleinbuchstaben w
120	170	78	01111000	x	&#120;	 	Kleinbuchstaben x
121	171	79	01111001	y	&#121;	 	Kleinbuchstaben y
122	172	7A	01111010	z	&#122;	 	Kleinbuchstaben z
-------------------------------------------------------------------------
"""
