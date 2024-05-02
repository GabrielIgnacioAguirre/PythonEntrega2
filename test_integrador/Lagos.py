import csv
from pathlib import Path
from string import digits

def ConversionAGD(lat, long, coor):
    lista = coor.split(" ")
    lat_list = []
    aux = ""
    for elem in lista[0]:
        if (elem in digits):
            aux += elem
        else:
            if aux:
                lat_list.append(int(aux))
            aux = ""
    print(lat_list)
    lat = -1* lat_list[0] + (lat_list[1] / 60 ) + (lat_list[2] / 3600)
    
    long_list = []
    aux = ""
    for elem in lista[1]:
        if (elem in digits):
            aux += elem
        else:
            if aux:
                long_list.append(int(aux))
            aux = ""
    print(long_list)
    long =-1 * long_list[0] + (long_list[1] / 60) + (long_list[2] / 3600)
    return lat, long


def TamañoSuperficie(sup):
    sup = int(sup)
    if sup < 17:
        return "chico"
    elif 17 < sup < 59:
        return "medio"
    else:
        return "grande"

file_route = Path("./datasets/lagos_arg.csv")
new_file_route = Path("./custom_datasets/lagos_arg.csv")

file = open(file_route, "r",encoding="utf-8")
new_file = open(new_file_route, "w",encoding="utf-8", newline="")

reader = csv.reader(file)
writer = csv.writer(new_file)

header = next(reader)
header.append("Sup tamaño")
header.append("latitud en GD")
header.append("Longitud en GD")
writer.writerow(header)

for line in reader:
    line.append(TamañoSuperficie(line[2]))
    latitud,longitud = 0.0,0.0
    latitud,longitud = ConversionAGD(latitud,longitud,line[5])
    line.append(latitud)
    line.append(longitud)
    writer.writerow(line)