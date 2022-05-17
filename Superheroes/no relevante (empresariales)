#ej nº 8

from pydoc import doc


def obt_precio():
    prec = float(input("Introduzca un precio"))
    IVA = int(input("Introduzca un IVA"))
    x = (prec/100)*IVA
    prec = x + prec
    print("Este es el precio:" , prec)
    if input("Quiere continuar?[Y/N]: !" ) == "Y":
        obt_precio()


