import pandas as pd
from pathlib import Path
from Dependencies import corelation


# Function to drop irrelevant columns from the DataFrame
def drop_irrelevant(columns_to_drop, df):
    for d in columns_to_drop:
        if d in df.columns:
            df = df.drop(d, axis=1)
    return df


if __name__ == "__main__":
    data_folder = Path("../Data_scraping")
    df = pd.read_csv(data_folder / "prepared_data.csv")

    columns_to_drop = ['demography', 'suicides', 'landarea', 'demography', 'Country', 'Year']
    df = drop_irrelevant(columns_to_drop, df)
    corelation(df)
    df.to_csv("relevant_data.csv", index=False)

