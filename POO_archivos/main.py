import csv


def funcion1(fichero):
    reader = csv.DictReader(fichero, delimiter = ';')
    list_datos = []
    examenes = ["Parcial1","Parcial2", "Ordinario1", "Ordinario2", "Practicas" , "OrdinarioPracticas"]
    for row in reader:
        list_datos.append(row)
        for a in row:
            if a=="Asistencia":
                row[a] = int(row[a].replace("%",""))


            elif a in examenes:
                if row[a] == "":
                    row[a] = 0

                else:
                    row[a] = float(row[a].replace(",", "."))


    return sorted(list_datos, key=lambda x: x["Apellidos"])

def funcion2(dic_list):
    for elemento in dic_list:
        a = elemento["Ordinario1"] if elemento["Ordinario1"] > elemento["Parcial1"] else elemento["Parcial1"]
        b = elemento["Ordinario2"] if elemento["Ordinario2"] > elemento["Parcial2"] else elemento["Parcial2"]
        c = elemento["OrdinarioPracticas"] if elemento["OrdinarioPracticas"] > elemento["Practicas"] else elemento["Practicas"]
        nota_fin = (a + b)*0.3 + c*0.4
        elemento["Nota Final"] = nota_fin

    return dic_list

def funcion3(dic_list):
    aprobados = []
    suspensos = []

    for elemento in dic_list:
        if elemento["Nota Final"] >= 5 and elemento["Asistencia"] >= 75 and elemento["Parcial1"] >= 4 and elemento["Parcial2"] >= 4 and elemento["Practicas"] >= 4:
            aprobados.append(elemento["Nombre"]+ " " + elemento["Apellidos"])

        elif elemento["Nota Final"] < 5:
            suspensos.append(elemento["Nombre"]+ " " + elemento["Apellidos"])

        else:
            aprobados.append(elemento["Nombre"] + " " + elemento["Apellidos"])

    return aprobados, suspensos


def main():
    with open('calificaciones.csv','r') as f:

        a = funcion1(f)

        funcion2(a)

        print(a)

        aprobados, suspensos = funcion3(a)

        print(aprobados, suspensos)







if __name__ == '__main__':
    main()


