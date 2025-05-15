# Calcula las estadísticas de una BD de personas
# La cual es una lista de diccionarios
# Cada diccionario representa una persona
# y tiene los siguientes campos:
# - nombre
# - documento
# - sexo
def calcular_estadisticas(db_persona): 
    total = len(db_persona)
    total_f = 0
    total_m = 0

    for p in db_persona:
        if (p['sexo'] == 'F'):
            total_f += 1
        else:
            total_m += 1
    
    return {"total_personas" : total, "total_femenino": total_f, "total_masculino" : total_m}
