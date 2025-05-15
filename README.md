# 💡Idea del proyecto

Este proyecto se hizo como base durante la sesión para revisar una estructura de creación de nuevo proyecto, organización y uso de la documentación. Algunos puntos que vimos son los siguientes.

## ⚙️Instalación de dependencias

CAda uno debe investigar y buscar información para instalar las siguientes dependencias. 

- Visual Studio Code
- Git
- Python

Aunque la instalación por lo general es sencilla, básicamente descargar el instalador y seleccionar opciones por defecto, ss importante que hagan todo el trabajo por sí mismos para afianzar el aprendizaje.


## 📂 Un proyecto por directorio

Los proyectos, por lo general, deben ser autocontenidos y estar en una única carpeta. ¿Por qué? ¡Te cuento!

- Orden y claridad: Tener todo en un solo lugar facilita encontrar y entender los archivos del proyecto. ¡Adiós a la búsqueda interminable!
- Dependencias controladas: Puedes gestionar las dependencias específicas de ese proyecto sin afectar a otros. Usa un entorno virtual (`venv`) dentro de la carpeta para aislar las dependencias.
- Fácil de compartir: Si quieres compartir tu proyecto con alguien más, solo tienes que comprimir la carpeta. ¡Listo para colaborar!
- Control de versiones: Git funciona mejor cuando cada proyecto tiene su propio directorio. Así, puedes rastrear los cambios de manera eficiente.
- Despliegue sencillo: Al tener todo autocontenido, el despliegue a un servidor o plataforma en la nube se vuelve mucho más sencillo y predecible.

## 💻 Crear workspace y seleccionar perfil Python en VS Code

Configurar tu workspace de VS Code correctamente es crucial para un desarrollo eficiente. Aquí te mostramos cómo hacerlo paso a paso:

### 👣 Pasos

- Crea una nueva carpeta para tu proyecto directamente desde el explorador de Windows. Desde la consola puedes escribir el comando 
``` 
mkdir nombre_directorio
```
-  Haz clic derecho dentro de la carpeta y selecciona "Abrir con Visual Studio Code". Desde la consola puedes hace. Desde la consola puedes escribir el comando

``` 
cd nombre_directorio
code .
```

- Si VS Code te pregunta si confías en el contenido de la carpeta, confirma para habilitar todas las funcionalidades.
- Guarda el workspace en la misma carpeta del proyecto para mantener todo organizado. Menú _Archivo_ opción "Guardar espacio de trabajo como".
- Crear un nuevo Perfil de Python _Archivo -> Preferencias -> Perfil_  
- Dentro de la ventana crear un perfil _Python Dev_ (o cualquier otro nombre) basado en la plantilla _Python_
  
Estos pasos te permitirán tener un entorno de desarrollo limpio y listo para comenzar a programar. Recuerda tomar el esfuerzo de hacerlo por ti mismo para que realmente aprendas.

## 📝 Crear un README.md en la raíz del proyecto

Los archivos Markdown (extensión `.md`)  facilitan escribir documentación de una manera portable (es texto plano, así que lo podés editar con cualquier programa como vim, Notepad, etc.). Además, plataformas como GitHub te muestran automáticamente el archivo `README.md` que esté en cualquier directorio. 

Otra ventaja de aprender Markdown es que la mayoría de las IAs generativas te dan los resultados en este formato para que los copies y pegues. Si escribís tus *prompts* en Markdown, ¡la IA te va a entender mejor y te dará mejores respuestas!

Además, los archivos `.md` te permiten (algunas de estas cosas requieren extensiones):

- Ver links a páginas web.
- Mostrar imágenes.
- Integrar herramientas como Mermaid o PlantUML (para hacer gráficos con código).
- Usar MathJax para escribir fórmulas matemáticas con LaTeX.
- Verlos bien en un montón de IDEs con un "visor" de Markdown.

También hay herramientas para convertir Markdown a otros formatos, como Word o PowerPoint. ¡Pandoc es una de ellas y es gratis!

Por todo esto, recomiendo que busques tutoriales y la especificación de Markdown en la web. Acá te dejo algunos links que te pueden servir:

*   [Guía básica de Markdown](https://www.markdownguide.org/basic-syntax/)
*   [Tutorial de Markdown en español](https://www.youtube.com/watch?v=J-ookj96KIQ)

¡Animate a usar Markdown y hacé tu documentación más copada!

##🔂Usar Git Siempre

Incluso si planeas mantener tu proyecto solo en local y no subirlo a un repositorio remoto como GitHub, usar Git sigue siendo una excelente idea. ¿Por qué? Porque te ayuda a tener un historial claro de todos los cambios que has realizado. Si en algún momento "metes la pata" y quieres volver a una versión anterior de tu código, Git te permite hacerlo de manera sencilla.

Para iniciar un repositorio Git en tu proyecto, simplemente abre la terminal en la carpeta de tu proyecto y ejecuta el siguiente comando:

```bash
git init
```



# 🚀 Hola mundo

Creamos un hola mundo para probar todo.

Para ejecutar el hola mundo deben escribir en la consola

```bash
python hello.py
```

# 🧩 Por qué se requieren módulos

Se intentó hacer una idea de programa para ver por qué se requieren módulos cuando se quieren hacer en la práctica programas más grandes. ¡Mira este problema!

## Descripción del problema a resolver

Tenemos una lista de personas con sus datos: "nombre", "documento", "sexo". Cada persona está representada en un objeto diccionario. Necesitamos hacer lo siguiente:

- Leer la data del diccionario.
- Transformar los valores de la siguiente forma:
    - Nombre: todo en mayúsculas.
    - Documento: el primer caracter tipo, luego guión, luego el número.
- Sacar una estadística que tenga el total de personas y el total por sexo en un diccionario.
- Imprimir el listado de personas con las transformaciones.
- Imprimir el diccionario con las estadísticas.

## Implementación de todo en un archivo

Implementamos la solución a este problema en un solo archivo de código 📄 y dejamos la solución e el archivo `estadisticas_un_solo_archivo.py`. Para ejecutarlo puedes usar el siguiente comando

```bash
python estadisticas_un_solo_archivo.py
```

Puedes intentar guiarte por los comentarios para entender el funcionamiento del código. Recuerda que el programa no es perfecto 😲 pues se hizo de forma improvisada sobre la marcha  y sin un análisis completo de la situación 💀.

## Problemas de esta solución monolítica

Ahora pensemos...

¿Por qué no es buena idea hacer todo esto en un solo archivo? 🤔 ¡Aquí te van algunas razones!

- 🧱 Acoplamiento alto: Imagina que cada parte del código está pegada a las demás. Si cambias algo en un lugar, ¡puede romper todo lo demás!
- 🧹 Mantenibilidad difícil: Encontrar y arreglar errores se vuelve un caos. Es como buscar una aguja en un pajar.
- 🔄 Reutilización limitada: Es difícil tomar partes del código y usarlas en otros proyectos. ¡Hay que copiar y pegar, lo cual es un desastre!
- 🧑‍💻 Colaboración complicada: Si varias personas trabajan en el mismo archivo, ¡los conflictos están garantizados!
- 🧪 Pruebas difíciles: Probar cada parte del código por separado se vuelve un dolor de cabeza.

Por eso, ¡la modularización es necesaria! 🤙 Dividir el código en módulos hace que todo sea más fácil de entender, mantener y reutilizar.

## 📦 Módulos de Python

En Python, un módulo es simplemente un archivo que contiene código reutilizable: funciones, clases, variables, etc. La idea es dividir un programa grande en partes más pequeñas y manejables. En este proyecto, hemos creado una carpeta llamada `modules` (#modules) para organizar nuestro código en módulos.

¿Cuál es el objetivo de dividir el código en módulos en este caso? 🤔 Queremos separar las responsabilidades y hacer que el código sea más fácil de entender y mantener.

## ✍️ Reescritura del programa usando módulos

Aquí te mostramos cómo dividimos el código en módulos y cuáles son las ventajas:

- 📁 `modules/data_personas.py`: Se encarga de manejar la información de las personas. Define la estructura de la base de datos y las funciones para acceder a ella.
    - ✅ Ventaja: Permite modificar la estructura de la base de datos sin afectar otras partes del código.
- 🧮 `modules/estadisticas.py`: Contiene las funciones para calcular estadísticas sobre la base de datos de personas.
    - ✅ Ventaja: Facilita la creación de nuevas estadísticas sin modificar el código de otras partes del programa.
- 🎨 `modules/formato.py`: Define las funciones para formatear los datos de las personas (nombre, documento, sexo).
    - ✅ Ventaja: Permite cambiar el formato de los datos sin afectar la lógica principal del programa.

Al dividir el código en módulos, logramos un código más organizado, fácil de mantener y reutilizable. ¡La modularización es la clave para construir programas grandes y complejos! 🚀

Para ejecutar este código debes usar el comando

```bash
python estadisticas_un_solo_archivo.py
```

## 🛠️ Posibles mejoras en la modularización

Si bien hemos modularizado el código, siempre hay espacio para mejorar. Aquí te presentamos algunas ideas para refinar aún más la estructura de nuestro proyecto:

- 🔒 Ocultamiento de la base de datos de personas: La base de datos de personas es una variable global que puede ser modificada directamente desde cualquier parte del código. Esto no es ideal, ya que podríamos modificar accidentalmente la base de datos y romper el programa.
    - 💡 Solución: Encapsular la base de datos dentro del módulo `data_personas.py` y proporcionar funciones para acceder y modificar la base de datos de forma controlada. Por ejemplo, en lugar de acceder directamente a `DB_PERSONA`, podríamos tener funciones como `get_persona(documento)` o `update_persona(documento, nuevos_datos)`. Estas funciones actuarían como intermediarios, controlando cómo se accede y modifica la base de datos. Esto se conoce como "ocultamiento de información" y ayuda a proteger la integridad de los datos.
- 🧩 Desacoplamiento de los módulos (sin POO): Los módulos `estadisticas.py` y `formato.py` dependen directamente del módulo `data_personas.py` para acceder a la base de datos de personas. Esto crea un acoplamiento entre los módulos, lo que dificulta la reutilización y el mantenimiento del código.
    - 💡 Solución: En lugar de que `estadisticas.py` y `formato.py` accedan directamente a `DB_PERSONA`, el módulo `data_personas.py` podría proporcionar funciones que devuelvan los datos necesarios en un formato específico. Por ejemplo, `data_personas.py` podría tener una función `get_nombres_y_sexos()` que devuelva una lista de tuplas con los nombres y sexos de las personas. De esta manera, `estadisticas.py` y `formato.py` no necesitan conocer la estructura interna de `DB_PERSONA` y solo dependen de la interfaz proporcionada por `data_personas.py`.

Al implementar estas mejoras, lograremos un código aún más modular, fácil de mantener y reutilizable, ¡sin necesidad de usar POO! 


# 🏋️ Ejercicios propuestos

## ✏️ Ejercicio 1

En el programa `hello.py`, pide al usuario que ingrese un valor por teclado y genera una salida formateada usando `f-strings` o el operador `%`. 

## 🧠 Ejercicio 2

Modifica el programa `hello.py` para que reciba un parámetro como argumento desde la línea de comandos. ¿Qué función usarías para lograr esto?

## 🏆 Ejercicio 3

Piensa en las mejoras que propusimos antes, y otras alternativas para reducir el acoplamiento del programa modular de estadísticas. ¿Cómo implementarías estas mejoras?

## 👴 Ejercicio 4

Los grupos etarios son categorías que agrupan a personas en función de su edad. Por ejemplo:

| Grupo Etario   | Rango de Edad | Descripción                                                                                                |
| :------------- | :------------ | :--------------------------------------------------------------------------------------------------------- |
| Niñez          | 0 - 11 años   | Etapa de desarrollo físico y cognitivo fundamental, caracterizada por el aprendizaje y la exploración.      |
| Adolescencia   | 12 - 18 años  | Período de cambios hormonales y emocionales, búsqueda de identidad y desarrollo de la autonomía.           |
| Juventud       | 19 - 29 años  | Etapa de consolidación de la identidad, desarrollo profesional y establecimiento de relaciones duraderas. |
| Adultez        | 30 - 59 años  | Período de madurez, desarrollo profesional y familiar, y contribución a la sociedad.                      |
| Adulto Mayor  | 60+ años      | Etapa de sabiduría y experiencia, disfrute de la vida y legado a las nuevas generaciones.                 |

Extiende el programa de estadísticas para que también muestre:

- La cantidad de personas por cada grupo etario. 📊
- El grupo etario con mayor y menor cantidad de personas. 🏆
- La edad promedio de todas las personas (redondeada a 2 decimales). ➗

¿Qué modificaciones tienes que implementar para lograr esto?

## 🔨 Ejercicio 4

En un sistema de movimientos de inventario de una ferretería 🧰, se tiene la siguiente información de cada producto:

- Código SKU de 8 caracteres alfanuméricos. 🔑
- Categoría del producto (ej: Tornillos y Tuercas, Herramientas eléctricas, etc.). 🔩
- Nombre (hasta 50 caracteres). 📝
- Descripción (hasta 100 caracteres). ℹ️
- Precio Unitario. 💰
- Cantidad en bodega. 📦

El sistema debe registrar entradas y salidas de inventario con fecha de la operación y cantidad de productos. 📅

Se requiere un MVP (Producto Mínimo Viable) de este sistema. Desarrolla un programa en consola que presente un menú y gestione las siguientes opciones:

1.  Mostrar el catálogo de todos los productos. 📚
2.  Mostrar un producto por SKU. 🔍
3.  Registrar una entrada/salida de inventario de un producto por SKU y número de unidades. ➕/➖
4.  Mostrar el listado de todos los movimientos de entrada y salida del producto por SKU. 📜
5.  En todos los casos en donde aplique, si el SKU no existe, mostrar mensaje de error. ❌
6.  Los menús deben tener una opción para salir del sistema. 🚪

Para simplificar el programa, todos los datos se pueden modelar como diccionarios "quemados" o "cableados" en constantes que van a representar la Base de Datos, tal como se hizo en el ejemplo de estadísticas. 🔥

El ejercicio debe realizarse en dos partes:

### 🧱 Programa en un solo archivo `.py`

Implementa el sistema en un solo archivo `.py`. Analiza las ventajas y posibles problemas que tiene esta solución. 🤔

### 🧩 Programa modular

Divide el programa en funcionalidades (por ejemplo, menús, catálogo de productos, movimientos de inventario) separando en varios módulos `.py`, con un programa principal que utilice los módulos para el sistema. Analiza las ventajas y desventajas de esta aproximación. ¿En qué mejora el código? 🚀
