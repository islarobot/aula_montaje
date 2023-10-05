
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = 0

#control adicional

if(a<b):
  print('El dividendo no puede ser menor que el divisor')
  sys.exit()

fin = False

d = a

while(fin==False):

   d = d - b
   c = c + 1
   if(d<b):
     
     resto = d
     fin = True
     cociente = c
   

print('Cociente: '+str(cociente))
print('\n')
print('Resto: '+str(resto))


