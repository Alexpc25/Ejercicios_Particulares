class Bloque:
    # Un bloque es un conjunto de instrucciones ejecutadas
    # unas detrás de otras.
    def __init__(self):
        # Por defecto, un bloque no contiene ninguna instrucción.
        self.instrucciones = []

    def agregarInstruction(self, instruccion):
        self.instrucciones.append(instruccion)


class Si:
    # Representa una instrucción 'if'. 'condicion' es una cadena
    # de caracteres que contiene la evaluación de la condición,
    # 'entonces' es el bloque de instrucciones ejecutadas si la condición
    # se verifica, 'si_no' es el bloque de instrucciones ejecutadas
    # si no se verifica.

    def __init__(self, condicion, entonces, si_no):
        self.condicion = condicion
        self.entonces = entonces
        self.si_no = si_no


class MientrasQue:
    # Representa una instrucción 'while'.
    # 'condicion' es una cadena que contiene el valor evaluado
    # para decidir si el bucle continúa o no,
    # 'bloque' es la secuencia de instrucciones ejecutadas en bucle.
    def __init__(self, condicion, bloque):
        self.condicion = condicion
        self.bloque = bloque


class Mostrar:
    # Una instrucción para mostrar un mensaje
    # en salida estándar.
    def __init__(self, mensaje):
        self.mensaje = mensaje

def main():
    with open("programa.txt", "r") as f:
        dict_objt = {}
        for linea in f.readlines():
            linea = f.readline()
            linea.replace(" ", "")
            if "Mostrar" in linea:
                valores = linea.split("=")
                parametro = valores[1]

            elif "MientrasQue" in linea:
                a = linea.split("=")[0]

            elif "Si" in linea:
                a = linea.split("=")[0]

            elif "Bloque" in linea:
                a = linea.split("=")[0]

            else:







if __name__ == '__main__':
    main()

