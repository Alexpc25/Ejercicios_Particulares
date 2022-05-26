from csv import DictReader

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



def main():
    lista_alojamientos = lis_alojamientos("madrid-airbnb-listings-small.csv")

    n_alojamientoxdisc = alojamientos_dis(lista_alojamientos)

    print(n_alojamientoxdisc)

if __name__ == '__main__':
    main()


