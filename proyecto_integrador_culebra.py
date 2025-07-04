from turtle import *
from random import randrange

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def copy(self):
        return Vector(self.x, self.y)

    def move(self, other):
        self.x += other.x
        self.y += other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

class Juego:
    def __init__(self):
        self.manzana = Vector(0, 0)
        self.culebra = [Vector(10, 0)]
        self.ruta = Vector(0, -10)

        self.jugador = ""
        self.partidas_por_jugar = 0
        self.partidas_jugadas = 0

        self.estadisticas = {}
        self.manzanas_actual = 0
        self.colision_pared = 0
        self.colision_cuerpo = 0
        self.velocidad = 100
        self.modo_libre = False
        self.intentos_restantes = 0
        self.juego_activo = False

        self.iniciar_interfaz()

    def iniciar_interfaz(self):
        setup(420, 420, 370, 0)
        bgcolor("yellow")
        title("Culebreando Ando 🐍")
        hideturtle()
        tracer(False)
        self.asignar_controles()
        listen()
        self.visualizar_menu()
        done()

    def square(self, x, y, size, color_name):
        up()
        goto(x, y)
        down()
        color(color_name)
        begin_fill()
        for _ in range(4):
            forward(size)
            left(90)
        end_fill()

    def change(self, x, y):
        self.ruta.x = x
        self.ruta.y = y

    def inside(self, cabeza):
        return -200 < cabeza.x < 190 and -200 < cabeza.y < 190

    def visualizar_menu(self):
        clear()
        up()
        goto(0, 50)
        color("lime")
        write("MENU PRINCIPAL", align="center", font=("Tahoma", 30, "bold"))
        goto(0, 10)
        color("gray")
        write("1. Jugar", align="center", font=("Tahoma", 18, "bold"))
        goto(0, -30)
        write("2. Reglas del Juego", align="center", font=("Tahoma", 18, "bold"))
        goto(0, -70)
        write("3. Estadísticas", align="center", font=("Tahoma", 18, "bold"))
        goto(0, -110)
        write("4. Salir", align="center", font=("Tahoma", 18, "bold"))
        update()
        self.asignar_controles()

    def solicitar_datos(self):
        
        self.estadisticas = {}
        self.partidas_jugadas = 0
        self.partidas_por_jugar = 0
        self.intentos_restantes = 0
        self.manzanas_actual = 0
        self.colision_pared = 0
        self.colision_cuerpo = 0
        
        self.jugador = textinput("Nombre del Jugador", "Ingresa tu Nombre:")
        if self.jugador is None:
            return
        while True:
            modo = textinput("Opción de Juego", "¿Deseas un número de partidas? si / no ")
            if modo is None:
                return
            modo = modo.strip().lower()
            if modo == "si":
                while True:
                    try:
                        entrada = textinput("Número de Partidas", "¿Cuántas Partidas deseas Jugar?")
                        if entrada is None:
                            return
                        self.partidas_por_jugar = int(entrada)
                        if self.partidas_por_jugar > 0:
                            self.modo_libre = False
                            break
                    except:
                        pass
                break
            elif modo == "no":
                self.modo_libre = True
                self.partidas_por_jugar = 0
                break
            else:
                textinput("Respuesta Inválida", "Responde si o no y presiona ENTER.")
        self.partidas_jugadas = 0
        self.iniciar_juego()

    def iniciar_juego(self):
        if self.intentos_restantes == 0:
            if self.modo_libre: 
                self.partidas_jugadas += 1
            elif not self.modo_libre:
                self.partidas_jugadas += 1
                    
            self.intentos_restantes = 3
            clear()
            up()
            goto(0, 0)
            color("black")
            write(f"Inicio de Partida {self.partidas_jugadas}", align="center", font=("Tahoma", 20, "bold"))
            update()
            ontimer(self.iniciar_juego, 1500)
        else:
            self.iniciar_nivel()

    def iniciar_nivel(self):
        self.culebra = [Vector(10, 0)]
        self.ruta = Vector(0, -10)
        self.manzana.x = randrange(-15, 15) * 10
        self.manzana.y = randrange(-15, 15) * 10
        self.manzanas_actual = 0
        self.colision_pared = 0
        self.colision_cuerpo = 0
        self.velocidad = 100
        self.juego_activo = True
        self.asignar_controles()
        self.move()

    def move(self):
        if not self.juego_activo:
            return

        cabeza = self.culebra[-1].copy()
        cabeza.move(self.ruta)

        if not self.inside(cabeza) or cabeza in self.culebra:
            self.juego_activo = False

            if not self.inside(cabeza):
                self.colision_pared += 1
            if cabeza in self.culebra:
                self.colision_cuerpo += 1

            if self.partidas_jugadas not in self.estadisticas:
                self.estadisticas[self.partidas_jugadas] = []

            if len(self.estadisticas[self.partidas_jugadas]) < 3:
                self.estadisticas[self.partidas_jugadas].append({
                    "manzanas": self.manzanas_actual,
                    "colisiones_pared": self.colision_pared,
                    "colisiones_cuerpo": self.colision_cuerpo,})
                
                print(f"Intento registrado: Partida {self.partidas_jugadas}, 🍎 {self.manzanas_actual}, 🧱 {self.colision_pared}, 🐍 {self.colision_cuerpo}")

            self.intentos_restantes -= 1

            self.square(cabeza.x, cabeza.y, 11, "violet")
            up()
            goto(0, 0)
            color("black")
            write(f"Perdiste!!! Intentos Restantes: {self.intentos_restantes}", align="center", font=("Tahoma", 18, "bold"))
            update()

            if self.intentos_restantes > 0:
                ontimer(self.iniciar_juego, 1500)
            else:
                if self.modo_libre:
                    while True:
                        decision = textinput("Estas Muerto !!!!", "¿Quieres Intentarlo de Nuevo?  (si / no)")
                        if decision is None:
                            return
                        decision = decision.strip().lower()
                        if decision == "si":
                            ontimer(self.iniciar_juego, 1000)
                            break
                        elif decision == "no":
                            ontimer(self.mostrar_estadisticas, 1000)
                            break
                        else:
                            textinput("Respuesta Inválida", "Recuerda responder solo con si o no. Señala el recuadro y Presiona ENTER para volver.")
                else:
                    if self.partidas_jugadas < self.partidas_por_jugar:
                        ontimer(self.iniciar_juego, 1000)
                    else:
                        ontimer(self.mostrar_estadisticas, 1000)
            return

        self.culebra.append(cabeza)

        if cabeza == self.manzana:
            self.manzanas_actual += 1
            self.manzana.x = randrange(-15, 15) * 10
            self.manzana.y = randrange(-15, 15) * 10
            self.velocidad = max(30, self.velocidad - 5)
        else:
            self.culebra.pop(0)

        clear()
        for cuerpo in self.culebra:
            self.square(cuerpo.x, cuerpo.y, 11, 'black')
        self.square(self.manzana.x, self.manzana.y, 11, 'red')
        update()
        ontimer(self.move, self.velocidad)

    def mostrar_reglas(self):
        clear()
        up()
        goto(0, 80)
        color("lime")
        write("Reglas del Juego", align="center", font=("Tahoma", 24, "bold"))
        goto(0, 30)
        color("gray")
        write("Come manzanas y evita chocar.", align="center", font=("Comic Sans MS", 13, "bold"))
        goto(0, 0)
        write("Usa las flechas para moverte.", align="center", font=("Comic Sans MS", 13, "bold"))
        goto(0, -30)
        write("Cada partida tiene 3 intentos.", align="center", font=("Comic Sans MS", 13, "bold"))
        goto(0, -60)
        write("Mouse para menús y teclado para jugar.", align="center", font=("Comic Sans MS", 13, "bold"))
        goto(0, -120)
        color("magenta")
        write("Presiona ESPACIO para volver", align="center", font=("Courier", 14, "bold"))
        update()
        self.asignar_controles()

    def mostrar_estadisticas(self):
        clear()
        up()
        goto(0, 170)
        color("lime")
        write("Estadísticas de las Partidas", align="center", font=("Tahoma", 22, "bold"))

        y = 150
        total_manzanas = total_pared = total_cuerpo = 0

        partidas_validas = [p for p, intentos in self.estadisticas.items() if intentos]
        
        if not partidas_validas:
            goto(0, y - 30)
            color("red")
            write("No hay estadísticas aún", align="center", font=("Courier", 14, "bold"))
        else:
            ultimas_partidas = sorted(partidas_validas)[-3:]  
            
            for partida in ultimas_partidas:
                intentos = self.estadisticas[partida]
                suma_m = suma_p = suma_c = 0

                goto(0, y)
                color("blue")
                write(f"Partida {partida}", align="center", font=("Courier", 13, "bold"))
                y -= 22

                for i, intento in enumerate(intentos, 1):
                    linea = f"   Intento {i} -🍎 {intento['manzanas']} | 🧱 {intento['colisiones_pared']} | 🐍 {intento['colisiones_cuerpo']}"
                    goto(0, y)
                    color("black")
                    write(linea, align="center", font=("Courier", 11, "bold"))
                    y -= 18
                    
                    suma_m += intento["manzanas"]
                    suma_p += intento["colisiones_pared"]
                    suma_c += intento["colisiones_cuerpo"]

                total_manzanas += suma_m
                total_pared += suma_p
                total_cuerpo += suma_c

                goto(0, y)
                color("brown")
                write(f"  Total Partida {partida}  🍎 {suma_m} |🧱 {suma_p} |🐍 {suma_c}", align="center", font=("Courier", 12, "bold"))
                y -= 25

            goto(0, y)
            color("red")
            write(f" TOTAL GENERAL 🍎 {total_manzanas} |🧱 {total_pared} |🐍 {total_cuerpo}", align="center", font=("Courier", 13, "bold"))
            y -= 30

        goto(0, y)
        color("magenta")
        write("Presiona ESPACIO para volver al Menú", align="center", font=("Courier", 12, "bold"))
        update()
        self.asignar_controles()

    def salir(self):
        bye()

    def asignar_controles(self):
        listen()
        onkey(lambda: self.change(10, 0), 'Right')
        onkey(lambda: self.change(-10, 0), 'Left')
        onkey(lambda: self.change(0, 10), 'Up')
        onkey(lambda: self.change(0, -10), 'Down')
        onkey(self.solicitar_datos, '1')
        onkey(self.mostrar_reglas, '2')
        onkey(self.mostrar_estadisticas, '3')
        onkey(self.salir, '4')
        onkey(self.visualizar_menu, 'space')

Juego()


