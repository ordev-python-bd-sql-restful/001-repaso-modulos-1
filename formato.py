from numbers import Number

db_persona = [
    {'nombre': 'María Pérez', 'documento': 'D1234', "sexo": 'F', "edad": 20},
    {'nombre': 'Pedro González', 'documento': 'P9999', "sexo": 'M', "edad" : 15},
    {'nombre': 'Ana González', 'documento': 'P9999', "sexo": 'F',  "edad": 28},
    {'nombre': 'Ana González', 'documento': 'P9999', "sexo": 'F',  "edad": 10},
    {'nombre': 'Ana González', 'documento': 'P9999', "sexo": 'F',  "edad": "x"},
    {'nombre': 'Ana González', 'documento': 'P9999', "sexo": 'F',  "edad": 21},
    {'nombre': 'Ana González', 'documento': 'P9999', "sexo": 'F',  "edad": 60},
]

# Devuelva la edad de un diccionario de persona
def get_edad(persona = {}):
    # return int(persona["edad"])
    # Programación defensiva
    # Ver que la clave "edad" está en el parámetro persona
    return 0 if ("edad" not in persona.keys() or not isinstance(persona["edad"], Number)) \
        else persona["edad"]
    
    # existe_edad = "edad" in persona.keys()
    # if existe_edad:
    #     return persona["edad"]
    # else:
    #     return 0

def grupo_etario(persona):
    edad = get_edad(persona)

    # Programación defensiva
    # valor a descartar
    if edad <= 0:
        return None

    if (edad <= 11):
       return "niño"
    elif (edad <= 18):
        return "adolescente"
    elif (edad <= 29):
        return "juventud" 
    elif (edad <= 59):
        return "adultez" 
    else: 
        return "vejez"

if __name__ == "__main__":
    # Map, aplicar una función a cada elemento de a lista
    # Devuelve lista
    lista_edades = list(map(get_edad, db_persona))
    
    # Sacar los grupos etarios
    lista_grupos_etarios = list(map(grupo_etario, db_persona))
    
    # Filtrar los None que corresponden a edades inválidas
    lista_grupos_etarios = list(filter(lambda x : x is not None, lista_grupos_etarios))
    print (f"grupos etarios = {lista_grupos_etarios}")