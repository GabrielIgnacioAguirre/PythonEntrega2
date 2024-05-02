def returnTypes():
    from pathlib import Path
    import csv
    route_act = Path(__file__).parent
    route_padre = route_act.parent
    route = route_padre / "datasets" / "ar-airports.csv"
    
    file = open(route,encoding="utf-8",newline="")
    reader = csv.reader(file)
    lista = []
    for line in reader:
        if line[2] not in lista:
            lista.append(line[2])
    return lista