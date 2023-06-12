import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns


# Function to plot the relationship between population density and life expectancy
def populationdensity_lifeexpectancy(df):
    sns.regplot(x=df['populationdensity'], y=df['lifeexpectancy'])
    plt.xlabel('Gęstość zaludnienia')
    plt.ylabel('Przewidywana długość życia')
    plt.title('Zależność przeiwdywanej długości życia od gęstości zaludnienia')
    plt.show()


# Function to plot the relationship between happiness and life expectancy
def happiness_lifeexpectancy(df):
    sns.regplot(x=df['happiness'], y=df['lifeexpectancy'])
    plt.xlabel('Deklarowane szczęście')
    plt.ylabel('Przewidywana długość życia')
    plt.title('Zależność przewidywanej długości życia od średniego deklarowanego szczęścia')
    plt.show()


# Function to plot the relationship between land area and life expectancy
def landarea_lifeexpectancy(df):
    sns.regplot(x=df['landarea'], y=df['lifeexpectancy'])
    plt.xlabel('Powierzchnia kraju')
    plt.ylabel('Przewidywana długość życia')
    plt.title('Zależność przeiwdywanej długości życia od powierzchni kraju')
    plt.show()


# Function to plot the relationship between demography and life expectancy
def demography_lifeexpectancy(df):
    sns.regplot(x=df['demography'], y=df['lifeexpectancy'])
    plt.xlabel('Liczba ludności')
    plt.ylabel('Przewidywana długość życia')
    plt.title('Zależność przewidywanej długości życia od liczby ludności')
    plt.show()


# Function to plot the relationship between internet access and life expectancy
def internet_lifeexpectancy(df):
    sns.regplot(x=df['internet'], y=df['lifeexpectancy'])
    plt.xlabel('% społeczeństwa z dostępem do internetu')
    plt.ylabel('Przewidywana długość życia')
    plt.title('Zależność przewidywanej długości życia od % społeczeństwa z dostępem do internetu')
    plt.show()


# Function to plot the relationship between median age and life expectancy
def medianage_lifeexpectancy(df):
    sns.regplot(x=df['medianage'], y=df['lifeexpectancy'])
    plt.xlabel('mediana wieku')
    plt.ylabel('Przewidywana długość życia')
    plt.title('Zależność przewidywanej długości życia od mediany wieku')
    plt.show()


# Function to plot the relationship between mental disorders and life expectancy
def mentaldisorders_lifeexpectancy(df):
    sns.regplot(x=df['mentaldisorders'], y=df['lifeexpectancy'])
    plt.xlabel('% społeczeństwa z chorobami psychicznymi')
    plt.ylabel('Przewidywana długość życia')
    plt.title('Zależność przewidywanej długości życia od % społeczeństwa z chorobami psychicznymi')
    plt.show()


# Function to plot the relationship between alcohol/drug issues and life expectancy
def alcoholdrug_lifeexpectancy(df):
    sns.regplot(x=df['alcoholdrug'], y=df['lifeexpectancy'])
    plt.xlabel('% społeczeństwa z problemami z używkami')
    plt.ylabel('Przewidywana długość życia')
    plt.title('Zależność przewidywanej długości życia od % społeczeństwa z problemami z używkami')
    plt.show()


# Function to plot the relationship between GDP and life expectancy
def gdp_lifeexpectancy(df):
    sns.regplot(x=df['gdp'], y=df['lifeexpectancy'])
    plt.xlabel('GDP per capita ($)')
    plt.ylabel('Przewidywana długość życia')
    plt.title('Zależność przewidywanej długości życia od GDP per capita ($)')
    plt.show()


# Function to plot the relationship between pollution and life expectancy
def pollution_lifeexpectancy(df):
    sns.regplot(x=df['pollution'], y=df['lifeexpectancy'])
    plt.xlabel('zanieczyszczenie powietrza w μg')
    plt.ylabel('Przewidywana długość życia')
    plt.title('Zależność przewidywanej długości życia od zanieczyszczenia powietrza w μg')
    plt.show()


# Function to plot the correlation matrix of the DataFrame
def corelation(df):
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Macierz korelacji')
    plt.subplots_adjust(bottom=0.30)
    plt.show()


if __name__ == "__main__":
    data_folder = Path("../Data_scraping")
    df = pd.read_csv(data_folder / "prepared_data.csv")
    df = df.drop('Country', axis=1)
    df = df.drop('Year', axis=1)

    #gdp_lifeexpectancy(df)
    #alcoholdrug_lifeexpectancy(df)
    #mentaldisorders_lifeexpectancy(df)
    #medianage_lifeexpectancy(df)
    #internet_lifeexpectancy(df)
    #demography_lifeexpectancy(df)
    #happiness_lifeexpectancy(df)
    #landarea_lifeexpectancy(df)
    #populationdensity_lifeexpectancy(df)
    #pollution_lifeexpectancy(df)
    corelation(df)



