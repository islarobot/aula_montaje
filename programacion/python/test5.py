


def resta(a,b)

	c = 0

	if(a<b):
  		print('El dividendo no puede ser menor que el divisor')
  		return -1

	fin = False

	d = a

	while(fin==False):

   		d = d - b
   		c = c + 1
   	if(d<b):

     		resto = d
     		fin = True
     		cociente = c
		resultado = [cociente,resto]

	return resultado



