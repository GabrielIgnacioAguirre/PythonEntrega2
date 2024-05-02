import csv
from pathlib import Path

def PoseeConectividad(lista, indice, fin):
   ret = True
   while ( indice < fin ):
       if "-" in lista[indice]:
            return False
       indice +=1
   return ret


file_route = Path("./datasets/Conectividad_Internet.csv")
new_file_route = Path("./custom_datasets/Conectividad_Internet.csv")

file = open(file_route, "r",encoding="utf-8")
new_file = open(new_file_route, "w",encoding="utf-8", newline="")

reader = csv.reader(file)
writer = csv.writer(new_file)

header = next(reader)
header.append("posee_conectividad")
writer.writerow(header)
4-13

for line in reader:
    if PoseeConectividad(line,4,14):
        line.append("SI")
    else:
        line.append("NO")
    for elem in line:
        if "-" in elem:
            i = line.index(elem)
            line[i] = "NO"
    writer.writerow(line)
    
file.close()
new_file.close()
            