from enum import Enum

class Ataque(Enum):
    PUÑETAZO = 1
    CABEZAZO = 2
    CODAZO = 3
    PATADA = 4


class Pokemon:
    lista_de_ID = set()

    def __init__(self, nombre, ataque, salud, indice_ataque, indice_defensa, ID):
        if type(nombre) != str:
            raise TypeError("Error en el tipo de nombre")

        if type(ataque) != Ataque:
            raise TypeError("Error en el tipo de ataque")

        if type(salud) != int:
            raise TypeError("Error en el tipo de salud")

        if type(indice_ataque) != int:
            raise TypeError("Error en el tipo de indice de ataque")

        if type(indice_defensa) != int:
            raise TypeError("Error en el tipo de indice de defensa")

        if type(ID) != int:
            raise TypeError("Error en el tipo de ID")

        self.__nombre = nombre
        self.__ataque = ataque
        self.__salud = salud
        self.__indice_ataque = indice_ataque
        self.__indice_defensa = indice_defensa
        self.__ID = ID
        Pokemon.lista_de_ID.add(ID)

    def destroy(self):
        Pokemon.lista_de_ID.remove(self.__ID)

    def __str__(self):
        return "Pokemon ID " + str(self.__ID) + " con nombre " + self.__nombre + " con un ataque " + str(self.__ataque.name) + " y salud " + str(self.__salud)

    def get_nombre(self):
        return self.__nombre

    def get_ataque(self):
        return self.__ataque

    def get_salud(self):
        return self.__salud

    def get_indice_ataque(self):
        return self.__indice_ataque

    def get_indice_defensa(self):
        return self.__indice_defensa

    def get_ID(self):
        return self.__ID

    def set_salud(self, salud):
        self.__salud = salud

    def is_vivo(self):
        return self.__salud != 0

    def fight_defense(self, daño):
        x = True

        if self.__salud - (daño-self.__indice_defensa) >= 0 and daño > self.__indice_defensa:
            self.__salud -= (daño-self.__indice_defensa)

        elif self.__salud - (daño-self.__indice_defensa) < 0 and daño > self.__indice_defensa:
            self.__salud = 0

        else:
            x = False

        return x

    def fight_attack(self, atacado):
        return atacado.fight_defense(self.__indice_ataque)






















