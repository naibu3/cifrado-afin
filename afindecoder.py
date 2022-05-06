#!/usr/bin/python3
#_*_utf-8_*_

from math import gcd
from sys import argv



def ayuda():
	print("Uso: ./afindecoder.py <codigo_cifrado> <abecedario>")

#codigo a descifrar, abcedario, num_elementos del abecedario
def descifrar(code, abc, elem, a, b):

	code_descif=[]

	for i in code:

		ind = int(abc.index(i))

		ind_orig=int( (ind-b)*pow(a, -1, elem) % elem )

		code_descif.append(abc[ind_orig])
	
	return "".join(code_descif)


#BUCLE PPAL____________________________________________________________________

if __name__=="__main__":

	abcedario=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
			'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

	try:

		codigo=argv[1]
	
	except:
		ayuda()
		exit(-1)


	n_elem=len(abcedario)

	for a in range(0, n_elem+1):

		if (gcd(a, n_elem)==1):

			for b in range(0,n_elem+1):

				print(descifrar(codigo, abcedario, n_elem, a, b) + " -> a=" + str(a) + ", b=" + str(b))
				print("")
	
	