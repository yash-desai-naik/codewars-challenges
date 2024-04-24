import pandas as pd


def create_df(data_: list[int]) -> None:
    df = pd.DataFrame(data=data_)
    print(df)
