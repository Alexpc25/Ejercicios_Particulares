import pandas as pd
import numpy as np

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


def main():

    list = ["Aluche", "Centro"]
    df = pd.read_csv("madrid-airbnb-listings-small.csv", delimiter='\t', na_filter=True)
    claves = ["neighbourhood", "property_type"]
    df_claves = df[claves].dropna(axis=0, how="any")


    for elemento in list:
        df_aux = df_claves.loc[df_claves["neighbourhood"] == elemento]
        alojamiento, num = np.unique(df_aux["property_type"], return_counts= True)

        total = sum(num)



        print(alojamiento)

        print(num)

        break

    arch_procesado = procesador("madrid-airbnb-listings-small.csv")



if __name__ == '__main__':
    main()

