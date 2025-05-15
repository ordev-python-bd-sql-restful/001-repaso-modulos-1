# funciones de formato

# Da formato al nombre de la persona
def formatear_nombre(nombre=""):
    return nombre.upper()

# Da formato al número de documento
# Separa el número de documento en dos partes
# y lo devuelve en el formato "X-XXXXXXX"
# Ejemplo: "12345678" -> "1-2345678"s
def formatear_documento(documento="0-0"):
    return (documento[0] + "-" + documento[1]).upper 

# Da formato al sexo de la persona
def formatear_sexo(sexo=""):
    return sexo.upper()