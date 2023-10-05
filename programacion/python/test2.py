
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

#a = 1

#b = 2

c = a + b

f = open('yago.txt','w')

f.write(str(c))

