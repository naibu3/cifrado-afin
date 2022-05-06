#!/usr/bin/python3
#_*_utf-8_*_

from math import gcd


n_elem=26

abcedario=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
	 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

frase="ESPEROQUELEHAYAGUSTADO"


#codigo a descifrar, abcedario, num_elementos del abecedario
def cifrar(sentence, abc, elem, a, b):

	code_cif=[]

	for i in sentence:

		ind = int(abc.index(i))

		ind_cif=int( (a*ind+b) % elem )

		code_cif.append(abc[ind_cif])
	
	return "".join(code_cif)


#BUCLE PPAL____________________________________________________________________

if __name__=="__main__":

	print(cifrar(frase, abcedario, n_elem, 19, 25))
	
	