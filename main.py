import numpy
import pandas as pd
import datetime
import os
from typing import Union
import autopep8


def formatted_file(input_file: str) -> pd.DataFrame:
    df = pd.read_csv(input_file)
    df["Day"] = pd.to_datetime(df.Day, format="%Y-%m-%d")
    df["Day"] = df["Day"].dt.date
    return df



def get_data(input_file: str, date: datetime.date) -> Union[numpy.float64, None]:
    if os.path.exists(input_file):
        df = formatted_file(input_file)
        for i in range(0, df.shape[0], 1):
            if str(df["Day"].iloc[i]).replace("-", "") == str(date).replace("-", ""):
                return df.iloc[i]["Exchange rate"]
        return None
    raise FileNotFoundError


def get_data_xy(input_file_x: str, input_file_y: str,
                date: datetime.date) -> Union[numpy.float64, None]:
    if os.path.exists(input_file_x) and os.path.exists(input_file_y):

        df_x = pd.read_csv(input_file_x)
        df_y = pd.read_csv(input_file_y)
        index = -1

        for i in range(0, df_x.shape[0], 1):
            if df_x["Day"].iloc[i].replace("-", "") == str(date).replace("-", ""):
                index = i
                break

        if index >= 0:
            return df_y.iloc[index]["Exchange rate"]
        return None

    raise FileNotFoundError