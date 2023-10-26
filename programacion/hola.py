import csv
import sys

parametro = sys.argv[1]

with open('aerolineas.csv') as csvfile:

	reader = csv.reader(csvfile)
	for row in reader:
        	iata = row[0]
		nombre = row[2]
		if(iata == parametro):
			print(row[2])
		
		if(parametro.lower() in nombre.lower()):
			print(row[0]+' '+row[2])