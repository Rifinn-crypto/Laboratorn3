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