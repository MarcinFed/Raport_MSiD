import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import os


# Function to plot histograms for specified columns in a dataframe
def histogram(df, columns):
    for column in columns:
        column_name = column
        plt.figure(figsize=(10, 6))
        # Plot histogram using specified column
        plt.hist(df[column_name], bins=10, rwidth=0.8, edgecolor='black')
        plt.xticks(fontsize=17)
        plt.yticks(fontsize=17)
        # Save the histogram plot as an image
        plt.savefig(os.path.join("Histograms\\", column + "_histogram.jpg"))
        plt.show()


if __name__ == "__main__":
    # Define the path to the data folder
    data_folder = Path("../Data_scraping")
    # Read the CSV file into a pandas dataframe
    df = pd.read_csv(data_folder / "2010-2016_prepared_data.csv")
    # Drop the 'Country' column from the dataframe
    df = df.drop('Country', axis=1)

    # List of columns to plot histograms for
    columns = ["alcoholdrug", "demography", "gdp", "happiness", "internet", "landarea", "medianage", "mentaldisorders", "pollution", "populationdensity", "suicides", "lifeexpectancy"]
    # Call the histogram function to plot histograms for the specified columns
    histogram(df, columns)
