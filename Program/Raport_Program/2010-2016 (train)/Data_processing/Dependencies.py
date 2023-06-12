import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Function to plot the relationship between population density and life expectancy
def populationdensity_lifeexpectancy(df):
    plt.figure(figsize=(10, 8))
    sns.regplot(x=df['populationdensity'], y=df['lifeexpectancy'], line_kws={'color': 'red'})
    plt.xlabel('Gęstość zaludnienia (na km^2)', fontsize=14)
    plt.ylabel('Przewidywana długość życia (w latach)', fontsize=14)
    plt.title('Zależność przewidywanej długości życia od gęstości zaludnienia')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.savefig(os.path.join("Dependencies\\", "populationdensity_dependency.jpg"))
    plt.show()


# Function to plot the relationship between happiness and life expectancy
def happiness_lifeexpectancy(df):
    plt.figure(figsize=(10, 8))
    sns.regplot(x=df['happiness'], y=df['lifeexpectancy'], line_kws={'color': 'red'})
    plt.xlabel('Deklarowane szczęście (0-najgorzej, 10-najlepiej)', fontsize=14)
    plt.ylabel('Przewidywana długość życia (w latach)', fontsize=14)
    plt.title('Zależność przewidywanej długości życia od średniego deklarowanego szczęścia')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.savefig(os.path.join("Dependencies\\", "happiness_dependency.jpg"))
    plt.show()


# Function to plot the relationship between land area and life expectancy
def landarea_lifeexpectancy(df):
    plt.figure(figsize=(10, 8))
    sns.regplot(x=df['landarea'], y=df['lifeexpectancy'], line_kws={'color': 'red'})
    plt.xlabel('Powierzchnia kraju (w km^2)', fontsize=14)
    plt.ylabel('Przewidywana długość życia (w latach)', fontsize=14)
    plt.title('Zależność przewidywanej długości życia od powierzchni kraju')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.savefig(os.path.join("Dependencies\\", "landarea_dependency.jpg"))
    plt.show()


# Function to plot the relationship between demography and life expectancy
def demography_lifeexpectancy(df):
    plt.figure(figsize=(10, 8))
    sns.regplot(x=df['demography'], y=df['lifeexpectancy'], line_kws={'color': 'red'})
    plt.xlabel('Liczba ludności', fontsize=14)
    plt.ylabel('Przewidywana długość życia (w latach)', fontsize=14)
    plt.title('Zależność przewidywanej długości życia od liczby ludności')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.savefig(os.path.join("Dependencies\\", "demography_dependency.jpg"))
    plt.show()


# Function to plot the relationship between internet usage and life expectancy
def internet_lifeexpectancy(df):
    plt.figure(figsize=(10, 8))
    sns.regplot(x=df['internet'], y=df['lifeexpectancy'], line_kws={'color': 'red'})
    plt.xlabel('% społeczeństwa używającego internetu', fontsize=14)
    plt.ylabel('Przewidywana długość życia (w latach)', fontsize=14)
    plt.title('Zależność przewidywanej długości życia od % społeczeństwa używającego internetu')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.savefig(os.path.join("Dependencies\\", "internet_dependency.jpg"))
    plt.show()


# Function to plot the relationship between median age and life expectancy
def medianage_lifeexpectancy(df):
    plt.figure(figsize=(10, 8))
    sns.regplot(x=df['medianage'], y=df['lifeexpectancy'], line_kws={'color': 'red'})
    plt.xlabel('mediana wieku (w latach)', fontsize=14)
    plt.ylabel('Przewidywana długość życia (w latach)', fontsize=14)
    plt.title('Zależność przewidywanej długości życia od mediany wieku')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.savefig(os.path.join("Dependencies\\", "medianage_dependency.jpg"))
    plt.show()


# Function to plot the relationship between mental disorders and life expectancy
def mentaldisorders_lifeexpectancy(df):
    plt.figure(figsize=(10, 8))
    sns.regplot(x=df['mentaldisorders'], y=df['lifeexpectancy'], line_kws={'color': 'red'})
    plt.xlabel('Liczba przypadków na 100 osób (w %)', fontsize=14)
    plt.ylabel('Przewidywana długość życia (w latach)', fontsize=14)
    plt.title('Zależność przewidywanej długości życia od aktualnej liczby przypadków zaburzeń psychicznych')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.savefig(os.path.join("Dependencies\\", "mentaldisorders_dependency.jpg"))
    plt.show()


# Function to plot the relationship between alcohol and drug problems and life expectancy
def alcoholdrug_lifeexpectancy(df):
    plt.figure(figsize=(10, 8))
    sns.regplot(x=df['alcoholdrug'], y=df['lifeexpectancy'], line_kws={'color': 'red'})
    plt.xlabel('Problemy z używkami (w %)', fontsize=14)
    plt.ylabel('Przewidywana długość życia (w latach)', fontsize=14)
    plt.title('Zależność przewidywanej długości życia od % społeczeństwa z problemami z używkami')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.savefig(os.path.join("Dependencies\\", "alcoholdrug_dependency.jpg"))
    plt.show()


# Function to plot the relationship between GDP and life expectancy
def gdp_lifeexpectancy(df):
    plt.figure(figsize=(10, 8))
    sns.regplot(x=df['gdp'], y=df['lifeexpectancy'], line_kws={'color': 'red'})
    plt.xlabel('GDP per capita ($)', fontsize=14)
    plt.ylabel('Przewidywana długość życia (w latach)', fontsize=14)
    plt.title('Zależność przewidywanej długości życia od GDP per capita')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.savefig(os.path.join("Dependencies\\", "gdp_dependency.jpg"))
    plt.show()


# Function to plot the relationship between air pollution and life expectancy
def pollution_lifeexpectancy(df):
    plt.figure(figsize=(10, 8))
    sns.regplot(x=df['pollution'], y=df['lifeexpectancy'], line_kws={'color': 'red'})
    plt.xlabel('zanieczyszczenie powietrza (w μg)', fontsize=14)
    plt.ylabel('Przewidywana długość życia (w latach)', fontsize=14)
    plt.title('Zależność przewidywanej długości życia od zanieczyszczenia powietrza')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.savefig(os.path.join("Dependencies\\", "pollution_dependency.jpg"))
    plt.show()


# Function to plot the relationship between year and life expectancy
def year_lifeexpectancy(df):
    plt.figure(figsize=(10, 8))
    sns.regplot(x=df['Year'], y=df['lifeexpectancy'], line_kws={'color': 'red'})
    plt.xlabel('Rok', fontsize=14)
    plt.ylabel('Przewidywana długość życia (w latach)', fontsize=14)
    plt.title('Zależność przewidywanej długości życia od roku')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.savefig(os.path.join("Dependencies\\", "year_dependency.jpg"))
    plt.show()



# Function to plot the relationship between suicides and life expectancy
def suicides_lifeexpectancy(df):
    plt.figure(figsize=(10, 8))
    sns.regplot(x=df['suicides'], y=df['lifeexpectancy'], line_kws={'color': 'red'})
    plt.xlabel('Liczba samobójstw', fontsize=14)
    plt.ylabel('Przewidywana długość życia (w latach)', fontsize=14)
    plt.title('Zależność przewidywanej długości życia od liczby samobójstw')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.savefig(os.path.join("Dependencies\\", "suicides_dependency.jpg"))
    plt.show()


# Function to plot the correlation matrix
def corelation(df):
    correlation_matrix = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Macierz korelacji')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.subplots_adjust(bottom=0.30, left=0.17, right=1)
    plt.savefig(os.path.join("Dependencies\\", "corelation.jpg"))
    plt.show()


if __name__ == "__main__":
    data_folder = Path("../Data_scraping")
    df = pd.read_csv(data_folder / "2010-2016_prepared_data.csv")
    df = df.drop('Country', axis=1)

    #populationdensity_lifeexpectancy(df)
    #gdp_lifeexpectancy(df)
    #alcoholdrug_lifeexpectancy(df)
    #mentaldisorders_lifeexpectancy(df)
    #medianage_lifeexpectancy(df)
    #internet_lifeexpectancy(df)
    #demography_lifeexpectancy(df)
    #happiness_lifeexpectancy(df)
    #landarea_lifeexpectancy(df)
    #pollution_lifeexpectancy(df)
    #year_lifeexpectancy(df)
    #suicides_lifeexpectancy(df)
    corelation(df)



