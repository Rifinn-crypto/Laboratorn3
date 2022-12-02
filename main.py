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


