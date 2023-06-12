import pandas as pd
from pathlib import Path
from Dependencies import corelation


# Function to drop irrelevant columns from the dataframe
def drop_irrelevant(columns_to_drop, df):
    for d in columns_to_drop:
        if d in df.columns:
            df = df.drop(d, axis=1)
    return df


if __name__ == "__main__":
    # Define the path to the data folder
    data_folder = Path("../Data_scraping")
    # Read the CSV file into a pandas dataframe
    df = pd.read_csv(data_folder / "2010-2016_prepared_data.csv")

    # List of columns to drop
    columns_to_drop = ['demography', 'suicides', 'landarea', 'demography', 'Country', 'Year']
    # Drop the irrelevant columns from the dataframe
    df = drop_irrelevant(columns_to_drop, df)
    # Call the corelation function to visualize the correlation matrix
    corelation(df)
    # Save the modified dataframe to a new CSV file
    df.to_csv("relevant_data.csv", index=False)

