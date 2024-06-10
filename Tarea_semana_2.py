class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        self.nivel = 1

    def atributos(self):
        print(f"{self.nombre} (Nivel {self.nivel}):")
        print(f"· Fuerza: {self.fuerza}")
        print(f"· Inteligencia: {self.inteligencia}")
        print(f"· Defensa: {self.defensa}")
        print(f"· Vida: {self.vida}")

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa
        self.nivel += 1

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(f"{self.nombre} ha muerto")

    def recibir_daño(self, daño):
        daño_real = max(daño - self.defensa, 0)
        self.vida -= daño_real
        print(f"{self.nombre} ha recibido {daño_real} puntos de daño")
        if not self.esta_vivo():
            self.morir()

    def atacar(self, enemigo):
        daño = self.calcular_daño()
        enemigo.recibir_daño(daño)

    def calcular_daño(self):
        return self.fuerza

class Guerrero(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self, daño_espada):
        self.espada = daño_espada

    def atributos(self):
        super().atributos()
        print(f"· Espada: {self.espada}")

    def calcular_daño(self):
        return self.fuerza + self.espada

class Mago(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def cambiar_libro(self, poder_libro):
        self.libro = poder_libro

    def atributos(self):
        super().atributos()
        print(f"· Libro: {self.libro}")

    def calcular_daño(self):
        return self.inteligencia + self.libro

def combate(jugador_1, jugador_2):
    turno = 1
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print(f"\nTurno {turno}")
        if jugador_1.esta_vivo():
            print(f">>> Acción de {jugador_1.nombre}:")
            jugador_1.atacar(jugador_2)
            jugador_1.atributos()
        if jugador_2.esta_vivo():
            print(f">>> Acción de {jugador_2.nombre}:")
            jugador_2.atacar(jugador_1)
            jugador_2.atributos()
        turno += 1
    if jugador_1.esta_vivo():
        print(f"\nHa ganado {jugador_1.nombre}")
    elif jugador_2.esta_vivo():
        print(f"\nHa ganado {jugador_2.nombre}")
    else:
        print("\nEmpate")

# Ejemplo de uso
personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 5)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 8)

personaje_1.atributos()
personaje_2.atributos()

combate(personaje_1, personaje_2)
