from enum import Enum

class Tipo_guerrero(Enum):
    BOXEADOR = 1
    GLADIADOR = 2
    UFC = 3
    MMA = 4

class Tipo_arma(Enum): 
    PUÑETAZO = 4
    PATADA = 6
    CODAZO = 8
    ESPADA = 10



class Warrior:

    __vida = 100

    def __init__(self, defensa, guerrero, arma):
        if type(guerrero) != Tipo_guerrero:
            raise TypeError("Invalid type for attribute guerrero")
        if type(guerrero) != Tipo_arma:
            raise TypeError("Invalid type for attribute arma")
        if type(defensa) != int:
            raise TypeError("Invalid type for attribute defensa")
        if defensa<1 or defensa>10:
            raise ValueError("Invalid value for defense")
        self.__defensa = defensa
        self.__guerrero = guerrero
        self.__arma = arma
    
    def get_vida(self): 
        return self.__vida

    def get_arma(self): 
        return self.__arma

    def get_guerrero(self): 
        return self.__guerrero

    def get_defensa(self): 
        return self.__defensa
    
    def set_arma(self, x):
        self.__arma = x 
    
    #No se ha hecho setter de guerrero ni de defensa porque es un atributo que no puede cambiar, y no se ha hecho setter de vida porque se modifica en fight_defense. Luego,
    #el resto tienen todos getter para poderlos consurtal en el programa. 
    
    def is_alive(self): 
        return self.__vida != 0

    def fight_attack(self, warrior_to_attack):
        return 0
        
    def fight_defense(self, points_of_damage):
        daño = points_of_damage - self.__defensa
        self.__vida = self.__vida - daño if (daño>0) else self.__vida
        return daño > 0 



warrior_1 = Warrior(0, "BOXEADOR", Tipo_arma.PATADA)