import os
import pandas as pd
import glob

SOURCE_FOLDER_PATH = "Scraped_csv_data\\"
FILE_PATHS = glob.glob(SOURCE_FOLDER_PATH + "/*.csv")
OUTPUT_FOLDER_PATH = "Merged_by_year_data\\"


# Function to merge data for a specific year
def merge_by_year(year):
    merged_data = pd.DataFrame()

    # Iterate over files in the source folder
    for filename in os.listdir(SOURCE_FOLDER_PATH):
        # Check if the file is a CSV and starts with the specified year
        if filename.endswith('.csv') and filename.startswith(year):
            file_path = os.path.join(SOURCE_FOLDER_PATH, filename)
            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)
            # Extract the column name from the filename
            column = filename.split('.')[0][:-5]
            column = column[5:]
            # Rename the columns in the DataFrame
            df = df.rename(columns={year: column})
            df = df.rename(columns={'Land area (sq. km)': column})
            df = df.rename(columns={' '+year: column})

            # Merge the DataFrame with the merged_data DataFrame
            if merged_data.empty:
                merged_data = df
            else:
                merged_data = merged_data.merge(df, on='Country', how='outer')

    # Add a "Year" column to the merged_data DataFrame
    merged_data.insert(0, "Year", int(year))
    # Save the merged_data DataFrame to a CSV file
    merged_data.to_csv(os.path.join(OUTPUT_FOLDER_PATH, year + "_merged_data.csv"), index=False)
    return merged_data


# Function to show missing values in a DataFrame
def show_missing_values(df):
    nulls = df.isnull()
    null_values = nulls.sum().sort_values(ascending=False)
    percentage = nulls.sum() / nulls.count()*100
    missing_values = pd.concat([null_values, percentage], axis=1, keys=['Number', 'Percentage'], sort=False)
    return missing_values[missing_values['Percentage'] != 0]


# Function to drop rows with missing data in a DataFrame
def drop_missing_data(df):
    df.dropna(inplace=True)
    df.to_csv(os.path.join(OUTPUT_FOLDER_PATH, year + "_prepared_data.csv"), index=False)


# Function to merge all prepared data files
def merge_all():
    merged_data = pd.DataFrame()

    # Iterate over files in the output folder
    for filename in os.listdir(OUTPUT_FOLDER_PATH):
        # Check if the file is a prepared data CSV
        if filename.endswith('.csv') and 'prepared' in filename:
            file_path = os.path.join(OUTPUT_FOLDER_PATH, filename)
            # Read the prepared data CSV into a DataFrame
            df = pd.read_csv(file_path)
            # Concatenate the DataFrame with the merged_data DataFrame
            merged_data = pd.concat([merged_data, df])

    # Save the merged_data DataFrame to a CSV file
    merged_data.to_csv("2010-2016_prepared_data.csv", index=False)
    return merged_data


if __name__ == "__main__":
    # Specify the years to process
    years = ["2010", "2011", "2012", "2013", "2014", "2015",
             "2016"]
    # Iterate over the years
    for year in years:
        # Merge data for the current year
        df = merge_by_year(year)
        # Show missing values in the merged DataFrame
        print(show_missing_values(df))
        # Drop rows with missing data in the merged DataFrame
        drop_missing_data(df)
        # Show missing values in the prepared DataFrame
        print(show_missing_values(df))

    # Merge all prepared data files
    merged_df = merge_all()
    # Show missing values in the final merged DataFrame
    print(show_missing_values(merged_df))


