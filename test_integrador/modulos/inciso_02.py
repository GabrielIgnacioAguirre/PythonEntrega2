def ReturnAiportElevationX (elevacion):
    from pathlib import Path
    import csv
    
    route = Path(__file__).parent
    route = route.parent
    route = Path("./") / "custom_datasets" / "ar-airports.csv"
    
    file = open(route, encoding="utf-8", newline="")
    reader = csv.reader(file)
    next(reader)
    
    lista = []
    for elem in reader:
        if elem[23] == elevacion:
            lista.append(elem[3])
    return lista