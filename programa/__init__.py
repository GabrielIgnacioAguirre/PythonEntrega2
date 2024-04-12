def Goleador(nombres, tabla_goles):
    max_goles = max(tabla_goles)
    index_max_goles = tabla_goles.index(max_goles)
    max_goleador = nombres[index_max_goles]
    return max_goleador, max_goles

def GenerarJugadores(nombres,goles,goles_e,asistencias):
    jugadores = []
    for n,g,g_e,a in zip(nombres,goles,goles_e,asistencias):
        jugador = {
            'nombre':n,
            'goles':g,
            'goles evitados':g_e,
            'asistencias':a
        }
        jugadores.append(jugador)
    return jugadores

def mas_influyente(equipo):
    lista = []
    for jugador in equipo:
        aux = []
        influencia = jugador["goles"] * 1.5 + jugador["goles evitados"] * 1.25 + jugador["asistencias"]
        aux = [influencia,jugador['nombre']]
        lista.append(aux)
    return max(lista, key=lambda x: x[0])[1]

def promedio_goles_equipo(goles_temporada):
    return sum(goles_temporada) / 25

def promedio_goles_goleador(lista_nombres,lista_goles):
    indice_max_promedio = (max(range(0,len(lista_goles)), key =lambda x: lista_goles[x] / 25))
    return lista_nombres[indice_max_promedio],lista_goles[indice_max_promedio] / 25