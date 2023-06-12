import os
import pandas as pd
import glob

FOLDER_PATH = "Scraped_csv_data\\"
FILE_PATHS = glob.glob(FOLDER_PATH + "/*.csv")


# Function to merge the CSV files into a single DataFrame
def merge():
    merged_data = pd.DataFrame()

    # Iterate over each file in the folder
    for filename in os.listdir(FOLDER_PATH):
        if filename.endswith('.csv'):
            file_path = os.path.join(FOLDER_PATH, filename)
            df = pd.read_csv(file_path)
            # Extract the column name from the filename
            column = filename.split('.')[0][:-5]
            # Rename the column to the extracted name
            df = df.rename(columns={'2017': column})
            df = df.rename(columns={'Land area (sq. km)': column})
            df = df.rename(columns={' 2017': column})

            if merged_data.empty:
                # If the merged_data DataFrame is empty, assign it the current DataFrame
                merged_data = df
            else:
                # Merge the current DataFrame with the merged_data DataFrame
                merged_data = merged_data.merge(df, on='Country', how='outer')

    # Insert a "Year" column with a constant value of 2017
    merged_data.insert(0, "Year", 2017)
    # Save the merged data to a CSV file
    merged_data.to_csv("merged_data.csv", index=False)
    return merged_data


# Function to show missing values in the DataFrame
def show_missing_values(df):
    nulls = df.isnull()
    # Count the number of missing values in each column and calculate the percentage
    null_values = nulls.sum().sort_values(ascending=False)
    percentage = nulls.sum() / nulls.count()*100
    missing_values = pd.concat([null_values, percentage], axis=1, keys=['Number', 'Percentage'], sort=False)
    return missing_values[missing_values['Percentage'] != 0]


# Function to drop rows with missing data from the DataFrame
def drop_missing_data(df):
    # Function to drop rows with missing data from the DataFrame
    df.dropna(inplace=True)
    # Function to drop rows with missing data from the DataFrame
    df.to_csv("prepared_data.csv", index=False)


if __name__ == "__main__":
    # Merge the CSV files
    df = merge()
    # Show missing values in the merged DataFrame
    print(show_missing_values(df))
    # Drop rows with missing data from the DataFrame
    drop_missing_data(df)
    # Show missing values after dropping missing data
    print(show_missing_values(df))


