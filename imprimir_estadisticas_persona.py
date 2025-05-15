# importar dependencias

from modules.estadisticas import calcular_estadisticas
from modules.data_personas import get_persona, total_personas

# Programa principal
cantidad_personas = total_personas()
personas_formateadas = []
for i in range(0, cantidad_personas):
    personas_formateadas.append(get_persona(i))

estadisticas = calcular_estadisticas(personas_formateadas)

print("Lista de personas formateada")
print(personas_formateadas)

print("")
print("Estadísticas")
print(estadisticas)
