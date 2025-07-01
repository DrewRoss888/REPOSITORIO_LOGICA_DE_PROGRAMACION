# REPOSITORIO_LOGICA_DE_PROGRAMACION
Trabajos de Aprendizaje Inicial de Programación

PROYECTO INTEGRADOR 


Elaboración del Juego de la Culebra

Autor:  William A. Dávila

Universidad Internacional del Ecuador 
Paralelo 1-ECC-1E: Lógica de Programación
Instructor: Mag. Estefanía V. Heredia Jiménez

Junio 29, 2025

Quito, Ecuador



JUEGO DE LA CULEBRA


Requisitos del Sistema

Python 3.7 o superior

No se requieren librerías externas (usa únicamente Turtle y Random de Python)


Contenido del Proyecto

C:\REPOSITORIO_LOGICA_DE_PROGRAMACION\proyecto_integrador_culebra.py
C:\REPOSITORIO_LOGICA_DE_PROGRAMACION\readme_proyecto_integrador_culebra.txt
C:\REPOSITORIO_LOGICA_DE_PROGRAMACION\DIAGRAMA_DE_FLUJO_CULEBRA_PROYECTO_INTEGRADOR.vsdx
C:\REPOSITORIO_LOGICA_DE_PROGRAMACION\DIAGRAMA_DE_FLUJO_CULEBRA.pdf


Descripción

El objetivo del juego es lograr comer la mayor cantidad de manzanas posibles sin chocarse.

El juego comienza mostrando un Menú Principal con cuatro opciones. El jugador debe seleccionar una usando el teclado:

1. Jugar – Inicia una nueva partida (Puedes escoger partidas o dejarlo libre).

2. Reglas del Juego – Muestra una pantalla con instrucciones básicas.

3. Estadísticas – Visualiza el resumen de las partidas anteriores.

4. Salir – Cierra el juego.


Detalles Adicionales.

El juego preguntará por el nombre y si quiere jugar en modo libre o con número fijo de partidas.

Cada partida tiene tres intentos.

Si elige ver reglas o estadísticas, se presentaran en pantalla con la opción de volver al Menú Principal presionando la barra espaciadora.

Las Estadísticas muestran por cada intento de cada partida cuantas manzanas se comieron, cuantas veces se chocó contra la pared y cuantas 
veces lo hizo contra el cuerpo.

La opción 4 finaliza el juego y sale de la pantalla





INICIO DE PROGRAMA

 1. Importación de Biblioteca Interna de Python.
    De la biblioteca traemos todo turtle para crear gráficos y controlar objetos en pantalla.
 	  De Random, traemos Randrange, que usaremos para generar posiciones aleatorias para la manzana.

2. Vector.
	  Asignar una posición en el plano (usada para la culebra, la manzana y la dirección). Esto va en coordenadas (x, y)

3. Lógica Principal del Juego. 
    Crear las variables de los objetos, se inician los componentes:  manzana, culebra, ruta.
	  Ubicar la posición inicial de la manzana, la culebra (como lista que sigue sumando segmentos), y la dirección de movimiento.
	  Crear datos del jugador, control de partidas, y partidas jugadas para asignar valores para usarlos en la configuración de las     	presentaciones de pantalla y estadísticas.
	  Crear Contadores y estado del juego, que sirvan para asignar valores para registrar y contabilizar: 
   	Estadísticas: (debe ser tipo diccionario por que se van a ingresar en ella claves y valores)
   	manzanas actual 
   	colisión pared 
   	colisión cuerpo 
   	velocidad 
   	modo libre  
   	intentos restantes 
   	juego activo 

4. Interfaz de la Pantalla.
 	  Configurar la ventana del juego: tamaño, color de fondo, título y activa controles de teclado, además para poder presentar en 	pantalla  el menú inicial.
 	  Dibujar un cuadrado de un cierto tamaño y color en la pantalla, para representar la culebra o la manzana.
	  Cambiar la dirección de movimiento de la culebra.
	  Verificar si la cabeza de la culebra sigue dentro del área visible del juego.

5. Visualizar Menú Principal.
     Despliega selecciones : 1. Jugar, 2. Ver Reglas, 3. Estadísticas y 4. Salir.

6. Solicitar Datos.
    Esta recopila la información del jugador y define el modo de juego antes de iniciar las partidas. También reinicia todas las     	estadísticas para evitar conflictos con datos antiguos.
	  Limpia las estadísticas acumuladas. 
	  Resetea contadores de partidas, intentos, manzanas y colisiones.
	  Solicita el nombre del jugador mediante una ventana emergente (textinput).
	  Pregunta si el jugador desea jugar un número fijo de partidas o en modo libre.
	  Si elige "sí", se solicita la cantidad de partidas.
	  Si elige "no", se activa el modo libre con intentos ilimitados.
	  Finalmente, llama a iniciar juego.

7. Iniciar Juego.
	  Controla el arranque de cada partida. Decide si es una nueva partida o un nuevo intento.
	  Aumenta el contador de partidas jugadas.
	  Establece 3 intentos para esa partida.
	  Muestra un mensaje en pantalla con el número de la partida.
	  Después de unos segundos, vuelve a llamar a iniciar juego.
	  Si hay intentos restantes:
	  Llama directamente a iniciar nivel para iniciar el juego.

8. Iniciar Nivel.
	  Inicia una nueva ronda dentro de cada partida. 
	  Reestablece las condiciones para comenzar un nuevo intento en: ruta, manzana, culebra, contadores, velocidad.
	  Coloca la serpiente en su posición inicial.
	  Fija la dirección inicial de movimiento.
	  Coloca una manzana en una posición aleatoria del tablero.
	  Reinicia los contadores de manzanas, colisiones y velocidad.
	  Activa el juego y llama para empezar a moverse dependiendo si hay o no intentos.

9.  Lógica Principal de Movimiento del Juego.
    Copia la última posición de la culebra a la cabeza y juntas se mueven en la ruta actual.
    Verifica que la culebra si no esta dentro de las paredes o se choca con el cuerpo, detenga el juego
    Realiza la suma en los contadores: colisión en cuerpo y colisión en pared según donde choque para sumar a las estadísticas.
    Para estadísticas, si aún no hay datos para la partida crea la lista.
    Si no se han registrado los 3 intentos permitidos guardamos los resultados actuales.
	  Muestra en consola un resumen de los que pasa en cada intento para control.
    Se coloca contador de intentos que se van restando.
	  Marca con un cuadrado el lugar donde la culebra chocó.
	  Muestra con texto en la pantalla que se perdió y cuantos intentos le quedan
	  Si aun hay intentos sigue. (En Modo libre despliega la pantalla si desea seguir o no)
	  Si no perdió continua el juego, agrega la nueva cabeza.
	  Si la manzana es comida se suma la nueva manzana al conteo y se genera una nueva manzana en un posición aleatoria y se aumenta la 	velocidad (reduciendo el tiempo de espera entre los ciclos).
	  Si no comió se  elimina el primer segmento para mantener la longitud actual, y dibuja el cuerpo y la manzana.
	  Se programa la siguiente ejecución de movimiento.

10. Mostrar Reglas.
	  Muestra en pantalla las reglas básicas del juego para que el jugador sepa cómo jugar.		
	  Extra:
	  Al final muestra un mensaje indicando que puede presionar la tecla ESPACIO para volver al menú principal.

11. Mostrar Estadísticas
	  Muestra un resumen estadístico de las últimas 3 partidas jugadas.
	  Incluye:
	  El número de manzanas comidas, colisiones con la pared, y colisiones con el cuerpo, por intento.
	  Si no hay partidas registradas, se muestra un mensaje que informa que aún no hay registro. 
	  Extra:
	  Al final muestra un mensaje indicando que puede presionar la tecla ESPACIO para volver al menú principal.

12. Salir del Juego. 
	  Cierra la ventana del Juego y programa.

13. Asignar Controles
	  Asocia teclas con acciones:
	  Flechas para mover la culebra.
	  Teclas numéricas para elegir opciones del Menú
	  Barra espaciadora para regresar al Menú.

14. Ejecutar el Juego.
	  Lanza todo el sistema del programa.

