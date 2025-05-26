from faker import Faker
from faker.providers import date_time as date_time_provider 

if __name__ == "__main__":
    
    # Iniciamos faker con el local de Español México
    # Genera cosas como nombres en español latino
    f = Faker('es_MX')

    # Provider para generar fakes de tiempo
    f.add_provider(date_time_provider)

    # Generamos 10 personas aleatorias
    # Faltaría generar email
    people = []
    for i in range(0,10):
        people.append({\
            
            # Nombre aleatorio
            "nombre": f.first_name(), \
            
            # Apellido aleatorio
            "apellido": f.last_name(), \
            
            # Fecha
            "fecha_nacimiento": f.date_between(start_date='-99y').strftime("%Y-%m-%d")})

    print(people)

