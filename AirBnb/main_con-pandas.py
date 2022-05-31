import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def procesador(arch):
    df = pd.read_csv(arch, delimiter='\t', na_filter=True)
    claves = ["id", "host_id", "listing_url", "room_type", "neighbourhood_group_cleansed", "price", "cleaning_fee",
              "accommodates", "minimum_nights", "review_scores_rating", "latitude", "longitude",
              "is_location_exact"]
    df_claves = df[claves].dropna(axis=0, how="any")
    lista_aux = ["price", "cleaning_fee"]
    df_claves[lista_aux] = df_claves[lista_aux].replace(to_replace={'\$': '', ',':''}, regex=True).astype(float)
    df_claves["minimum_cost"] = df_claves["price"] * df_claves["minimum_nights"] + df_claves["cleaning_fee"]
    df_claves["minimum_cost_xperson"] = (df_claves["minimum_cost"])/df_claves["accommodates"]

    return df_claves


def aloj_disct(list,arch):
    df = pd.read_csv(arch, delimiter='\t', na_filter=True)
    claves = ["neighbourhood", "property_type"]
    df_claves = df[claves].dropna(axis=0, how="any")

    dist_alojx= {}

    for elemento in list:
        df_aux = df_claves.loc[df_claves["neighbourhood"] == elemento]
        alojamiento, num = np.unique(df_aux["property_type"], return_counts= True)

        dic_x2 = {}
        total = sum(num)

        for i in range(0,len(alojamiento)):
            dic_x2[alojamiento[i]] = str((num[i]/total)*100) + "%"

        dist_alojx[elemento] = dic_x2

    return dist_alojx


def aloj_xanf(list, arch):
    df = pd.read_csv(arch, delimiter='\t', na_filter=True)
    claves = ["host_id", "neighbourhood"]
    df_claves = df[claves].dropna(axis=0, how="any")
    df_aux = df_claves.loc[df_claves["neighbourhood"].isin(list)]
    host, num = np.unique(df_aux["host_id"], return_counts=True)

    dic_hostxaloj = {}

    for i in range(0, len(host)):
        dic_hostxaloj[host[i]] = num[i]

    return sorted(dic_hostxaloj.items() , key = lambda x : x[1], reverse = False)


def aloj_media(arch):
    df = pd.read_csv(arch, delimiter='\t', na_filter=True)
    claves = ["neighbourhood", "host_id"]
    df_claves = df[claves].dropna(axis=0, how="any")
    df_aux = df_claves.groupby(["host_id", "neighbourhood"]).size().reset_index(name = "num_alojamiento_media")
    df_aux = df_aux.groupby(["host_id"], as_index = False).mean()

    return df_aux

def diagrama_sec(list,arch):
    df = pd.read_csv(arch, delimiter='\t', na_filter=True)
    claves = ["property_type", "neighbourhood"]
    df_claves = df[claves].dropna(axis=0, how="any")
    df_claves = df_claves.loc[df_claves["neighbourhood"].isin(list)]
    df_aux = df_claves.groupby(["property_type"]).size().reset_index(name = "num_alojamiento")
    plt.pie(df_aux["num_alojamiento"], labels=df_aux["property_type"])
    plt.show()

def diagraba_bar(arch):
    df = pd.read_csv(arch, delimiter='\t', na_filter=True)
    claves = ["neighbourhood"]
    df_claves = df[claves].dropna(axis=0, how="any")
    df_aux = df_claves.groupby(["neighbourhood"]).size().reset_index(name = "num_alojamiento")
    df_aux.set_index("neighbourhood", inplace=True)
    grafico = df_aux.plot.bar()
    plt.show()


def main():

    arch_procesado = procesador("madrid-airbnb-listings-small.csv")
    jkdjdj = aloj_xanf(["Aluche", "Centro"], "madrid-airbnb-listings-small.csv")

    jkgb =aloj_media("madrid-airbnb-listings-small.csv")

    afg = diagrama_sec(["Aluche", "Centro", "Moratalaz"], "madrid-airbnb-listings-small.csv")

    ghf = diagraba_bar("madrid-airbnb-listings-small.csv")

if __name__ == '__main__':
    main()

