import pandas as pd
import numpy as np

def function_1(doc):
    format_cols = ["cleaning_fee", "price"]
    dtype_dict = {"accommodates": np.int32, "minimum_nights": np.int32}
    df = pd.read_csv(doc, delimiter='\t', dtype=dtype_dict, na_filter=True)
    df = df[["id", "host_id", "listing_url", "room_type", "neighbourhood_group_cleansed", "price", "cleaning_fee",
             "accommodates", "minimum_nights", "review_scores_rating", "latitude", "longitude", "is_location_exact"]]
    df = df.dropna()
    for col in format_cols:
        df[col] = df[col].apply(lambda x: float(x.replace("$", "").replace(",", "")))
    df["minimum_cost"] = df["price"] * df["minimum_nights"] + df["cleaning_fee"]
    df["minimum_cost_per_person"] = df["minimum_cost"] / df["accommodates"]
    return df


def function_2(doc, districts):
    districts_info = {}
    dtype_dict = {"accommodates": np.int32, "minimum_nights": np.int32}
    df = pd.read_csv(doc, delimiter='\t', dtype=dtype_dict, na_filter=True)
    df = df[["neighbourhood", "property_type"]]
    df = df.dropna()
    for district in districts:
        df_aux = df.loc[df['neighbourhood'] == district]
        unique, unique_counts = np.unique(df_aux['property_type'], return_counts=True)
        districts_info[district] = {unique[i]: unique_counts[i]/sum(unique_counts) for i in range(0, len(unique))}
    return districts_info


def function_3(doc, districts):
    host_info = {}
    dtype_dict = {"accommodates": np.int32, "minimum_nights": np.int32}
    df = pd.read_csv(doc, delimiter='\t', dtype=dtype_dict, na_filter=True)
    df = df[["id", "host_id", "neighbourhood"]]
    df = df.dropna()
    df = df.loc[df["neighbourhood"].isin(districts)]
    df_agg = df.groupby(by=["neighbourhood", "host_id"], as_index=False, group_keys=False).agg({'id': ['count']})
    for host in np.unique(df_agg["host_id"]):
        df_aux = df_agg.loc[df_agg["host_id"] == host]
        array_count = [(row["neighbourhood"].values[0], row["id"].values[0]) for index, row in df_aux.iterrows()]
        array_count.sort(key=lambda y: y[1])
        host_info[host] = array_count
    print(host_info)


def main_pandas(doc):

    function_1(doc)
    function_2(doc, ["Embajadores", "Salamanca"])
    function_3(doc, ["Centro", "Salamanca"])