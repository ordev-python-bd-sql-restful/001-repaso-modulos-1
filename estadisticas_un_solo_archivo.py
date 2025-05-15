# Programa en un solo archivo

# Problemas
# Se mezclan funciones de varios temas
# Se complica el mantenimiento y agregar cosas nuevas a medida que el archivo crece

# BD de personas

db_persona = [
    {'nombre': 'María Pérez', 'documento': 'D1234', "sexo": 'F'},
    {'nombre': 'Pedro González', 'documento': 'P9999', "sexo": 'M'},
    {'nombre': 'Ana González', 'documento': 'P9999', "sexo": 'F'}
]

# Convertir todo a mayusculas
def formatear_registro_persona(registro_persona):
    nombre = registro_persona['nombre']
    documento = registro_persona['documento']
    nombre_formateado = nombre.upper()
    documento_formateado = (documento[0] + '-' + documento[1:]).upper()
    sexo_formateado = registro_persona['sexo'].upper()
    return {'nombre': nombre_formateado, 'documento': documento_formateado, "sexo": sexo_formateado}

# calcula estadisticas
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

# Programa principal

db_personas_formateada = []
for p in db_persona:
    db_personas_formateada.append(formatear_registro_persona(p))

estadisticas = calcular_estadisticas(db_personas_formateada)

print("Lista persona formateada")
print(db_personas_formateada)

print("Estadisticas")
print(estadisticas)