import re


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
        for linea in f.read().splitlines():
            obj_par = re.findall(r'(\w+)\s*=?\s*"?(.*)"?', linea)
            dict_objt[obj_par[0][0]] = obj_par[0][1]
            if "Mostrar" in obj_par[0][1]:
                linea_par = re.findall(r'\s*Mostrar\(\'(.+)\'\)', obj_par[0][1])
                dict_objt[obj_par[0][0]] = "print(" + linea_par[0] + ")"

            elif "MientrasQue" in obj_par[0][1]:
                print()
                #obj_par = re.findall(r'(\w+)\s*=\s*Mostrar\(\'(.+)\'\)', linea)
                #dict_objt[obj_par[0][0]] = "print(" + obj_par[0][1] + ")"

            elif "Si" in obj_par[0][1]:
                linea_par = re.findall(r'\s*Si\(\s*(.+)\s*,\s*(.+)\s*,\s*(.+)\s*\)', linea)
                objetos = []
                for objeto in linea_par[0]:
                    objeto = re.match(r'"(.+)"', objeto).group(1) if "\"" in objeto else dict_objt[objeto].strip("\"")
                    objetos.append(objeto)

                dict_objt[obj_par[0][0]] = "if " + objetos[0] + ": \n\t" + objetos[1] + "\nelse: \n\t" + objetos[2]

            elif "Bloque" in obj_par[0][1]:
                dict_objt[obj_par[0][0]] = ""

            elif "agregarInstruction(" in obj_par[0][1]:
                linea_par = re.findall(r'\(\s*(.+)\s*\)', linea)
                linea_par[0] = re.match(r'"(.+)"', linea_par[0]).group(1) if "\"" in linea_par[0] else dict_objt[linea_par[0]].strip("\"")


        print(dict_objt)







if __name__ == '__main__':
    main()

