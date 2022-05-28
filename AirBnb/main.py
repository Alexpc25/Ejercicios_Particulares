from csv import DictReader
import pandas as pd
import numpy as np


def lis_alojamientos(doc):
    with open(doc, "r", encoding="utf-8") as f:
        #columnas: id, host_id, neighbourhood, weekly_price, monthly_price, accommodates
        datos_arb = DictReader(f, delimiter='\t')
        datos_selec = []
        claves = ["id", "host_id", "neighbourhood", "weekly_price", "monthly_price", "accommodates"]

        for row in datos_arb:
            dict_aux = {clave: row[clave] for clave in claves}
            for i in range(3,6):
                dict_aux[claves[i]] = float(dict_aux[claves[i]].replace("$", "").replace(",", "")) if dict_aux[claves[i]] else 0
            datos_selec.append(dict_aux)

    return datos_selec

def alojamientos_dis(list):
    dict_dist = {}

    for elemento in list:
        if elemento["neighbourhood"] in dict_dist:
            dict_dist[elemento["neighbourhood"]] += 1

        else:
            dict_dist[ elemento["neighbourhood"]] = 1

    return dict_dist

def op_ocupantes(list, n):
    oc_list = []

    for elemento in list:
        if elemento["accommodates"] >= n:
            oc_list.append(elemento)

    return oc_list

def precio_busc(list, dist):
    precio_list = []
    lista = sorted(list, key = lambda x: x["weekly_price"])

    for elemento in lista:
        if elemento["neighbourhood"] == dist and elemento["weekly_price"] != 0:
            precio_list.append(elemento)

    return precio_list[:9]

def aloj_anf(list):
    list_anf = {}

    for elemento in list:
        if elemento["host_id"] in list_anf:
            list_anf[elemento["host_id"]] += 1

        else:
            list_anf[elemento["host_id"]] = 1

    return list_anf



def main():
    lista_alojamientos = lis_alojamientos("madrid-airbnb-listings-small.csv")

    n_alojamientoxdisc = alojamientos_dis(lista_alojamientos)

    num_ocup = op_ocupantes(lista_alojamientos, 2)

    alojamiento_barato = precio_busc(lista_alojamientos,"La Latina")

    aloj_x_anf = aloj_anf(lista_alojamientos)

    print(aloj_x_anf)



if __name__ == '__main__':
    main()

