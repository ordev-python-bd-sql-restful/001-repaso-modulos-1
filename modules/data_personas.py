from modules.formato import formatear_sexo,formatear_documento, formatear_nombre as fNombre

# Convención, las constantes van todo en mayúsculas
DB_PERSONA = [
    {'nombre': 'María Pérez', 'documento': 'D1234', "sexo": 'F'},
    {'nombre': 'Pedro González', 'documento': 'P9999', "sexo": 'M'},
    {'nombre': 'Ana González', 'documento': 'P9999', "sexo": 'F'}
]

# Realiza el formateo de una persona
# utilizando las funciones de formato
# del módulo formato	
# Debe revisarse si se puede mejorar
# pues en este caso se está acoplando   
# funciones de formato con un módulo 
# que se supone que es para manejar los datos.
def formatear_persona(persona):
    return {'nombre': fNombre(persona['nombre']), \
            'documento': formatear_documento(persona['documento']), \
             'sexo': formatear_sexo(persona['sexo'])}

def total_personas():
    return len(DB_PERSONA)

def get_persona(i):
    if i < 0 or i >= len(DB_PERSONA):
        return None
    
    return formatear_persona(DB_PERSONA[0])
