from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os.path
import time

# Define the path to store the scraped CSV data
SCRAPED_PATH = 'Scraped_csv_data'


# Function to scrape suicides data
def suicides_data():
    years = ["2017"]
    url = 'https://ourworldindata.org/grapher/number-of-deaths-from-suicide-ghe?tab=table&time='
    csv_file = os.path.join(SCRAPED_PATH, 'suicides_data.csv')

    if not os.path.isfile(csv_file):
        # If the CSV file does not exist, start scraping
        driver = webdriver.Chrome()
        dfs = []
        for year in years:
            driver.get(url + year)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            table = soup.find('table')
            headers = [header.text.strip().replace("Deathsdeaths • ", "") for header in table.find_all('th')]
            headers = [header.replace("Country or region", "Country") for header in headers]
            rows = table.find_all('tr')
            data = []
            for row in rows:
                cols = row.find_all('td')
                cols = [float(ele.text.strip().replace(',', '')) if ele.text.strip().replace(',',
                                                                                             '').isdigit() else ele.text.strip()
                        for ele in cols]
                if cols:
                    data.append(cols)
            dfs.append(pd.DataFrame(data, columns=headers))
        driver.quit()
        combined_df = dfs[0]
        for i in range(1, len(dfs)):
            combined_df = pd.merge(combined_df, dfs[i], how="outer")

        combined_df.to_csv(csv_file, index=False)
    else:
        # If the CSV file already exists, print the information
        print("File already exists")


# Function to scrape population density data
def population_density_data():
    years = ["2017"]
    url = 'https://ourworldindata.org/grapher/population-density?tab=table&time='
    csv_file = os.path.join(SCRAPED_PATH, 'populationdensity_data.csv')

    if not os.path.isfile(csv_file):
        driver = webdriver.Chrome()
        dfs = []
        for year in years:
            driver.get(url + year)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            table = soup.find('table')
            headers = [header.text.strip().replace("Population densitypeople per km² • ", "") for header in
                       table.find_all('th')]
            headers = [header.replace("Country or region", "Country") for header in headers]
            rows = table.find_all('tr')
            data = []
            for row in rows:
                cols = row.find_all('td')
                new_cols = []
                for ele in cols:
                    try:
                        ele = float((ele.text.strip().replace(',', '')))
                    except:
                        ele = ele.text.strip()
                    new_cols.append(ele)
                cols = new_cols
                if cols:
                    data.append(cols)
            dfs.append(pd.DataFrame(data, columns=headers))

        driver.quit()

        combined_df = dfs[0]
        for i in range(1, len(dfs)):
            combined_df = pd.merge(combined_df, dfs[i], how="outer")
        combined_df.to_csv(csv_file, index=False)
    else:
        print("File already exists")


# Function to scrape pollution data
def pollution_data():
    years = ["latest"]
    url = 'https://ourworldindata.org/grapher/PM25-air-pollution?tab=table&time='
    csv_file = os.path.join(SCRAPED_PATH, 'pollution_data.csv')

    if not os.path.isfile(csv_file):
        driver = webdriver.Chrome()
        dfs = []
        for year in years:
            driver.get(url + year)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            table = soup.find('table')
            headers = [header.text.strip().replace(
                "PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)micrograms per cubic meter •",
                "") for header in table.find_all('th')]
            headers = [header.replace("Country or region", "Country") for header in headers]
            rows = table.find_all('tr')
            data = []
            for row in rows:
                cols = row.find_all('td')
                cols = [float(ele.text.strip().replace(',', '').replace('μg', '').replace('\xa0', '')) if ele.text.strip().replace(',',
                                                                                                               '').isdigit() else ele.text.strip().replace(
                    'μg', '').replace('\xa0', '') for ele in cols]
                cols = [ele.split()[1] if ele.split() != [] and ele.split()[0].isdigit() else ele for ele in cols]
                if cols:
                    data.append(cols)
            dfs.append(pd.DataFrame(data, columns=headers))
        driver.quit()
        combined_df = dfs[0]
        for i in range(1, len(dfs)):
            combined_df = pd.merge(combined_df, dfs[i], how="outer")

        combined_df.to_csv(csv_file, index=False)
    else:
        print("File already exists")


# Function to scrape mental disorders data
def mental_disorders_data():
    years = ["2017"]
    url = 'https://ourworldindata.org/grapher/share-with-mental-and-substance-disorders?tab=table&time='
    csv_file = os.path.join(SCRAPED_PATH, 'mentaldisorders_data.csv')

    if not os.path.isfile(csv_file):
        driver = webdriver.Chrome()
        dfs = []
        for year in years:
            driver.get(url + year)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            table = soup.find('table')
            headers = [header.text.strip().replace(
                "Current number of cases in the population per 100 people - Sex: Both - Age: Age-standardized - Cause: Mental disorderspercent • ",
                "") for header in table.find_all('th')]
            headers = [header.replace("Country or region", "Country") for header in headers]
            rows = table.find_all('tr')
            data = []
            for row in rows:
                cols = row.find_all('td')
                cols = [float(ele.text.strip().replace(',', '').replace('%', '')) if ele.text.strip().replace(',',
                                                                                                              '').isdigit() else ele.text.strip().replace(
                    '%', '') for ele in cols]
                cols = [ele.split()[1] if ele.split() != [] and ele.split()[0].isdigit() else ele for ele in cols]
                if cols:
                    data.append(cols)
            dfs.append(pd.DataFrame(data, columns=headers))
        driver.quit()
        combined_df = dfs[0]
        for i in range(1, len(dfs)):
            combined_df = pd.merge(combined_df, dfs[i], how="outer")

        combined_df.to_csv(csv_file, index=False)
    else:
        print("File already exists")


# Function to scrape median age data
def median_age_data():
    years = ["2017"]
    url = 'https://ourworldindata.org/grapher/median-age?tab=table&time='
    csv_file = os.path.join(SCRAPED_PATH, 'medianage_data.csv')

    if not os.path.isfile(csv_file):
        driver = webdriver.Chrome()
        dfs = []
        for year in years:
            driver.get(url + year)
            time.sleep(1)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            table = soup.find('table')
            headers = [header.text.strip().replace("Median ageyears • 2017", "").replace(
                "Median age - Sex: all - Age: all - Variant: estimatesyears •", "") for header in table.find_all('th')]
            headers = [header.replace("Country or region", "Country") for header in headers]
            rows = table.find_all('tr')
            data = []
            for row in rows:
                cols = row.find_all('td')
                cols = [float(ele.text.strip().replace(',', '')) if ele.text.strip().replace(',',
                                                                                             '').isdigit() else ele.text.strip()
                        for ele in cols]
                if cols:
                    data.append(cols)
            dfs.append(pd.DataFrame(data, columns=headers))
        driver.quit()

        combined_df = dfs[0]
        for i in range(1, len(dfs)):
            combined_df = pd.merge(combined_df, dfs[i], how="outer")

        combined_df = combined_df.iloc[:, :-1]

        combined_df.to_csv(csv_file, index=False)
    else:
        print("File already exists")


# Function to scrape life expectancy data
def life_expectancy_data():
    years = ["2017"]
    url = 'https://ourworldindata.org/grapher/life-expectancy?tab=table&time='
    csv_file = os.path.join(SCRAPED_PATH, 'lifeexpectancy_data.csv')

    if not os.path.isfile(csv_file):
        driver = webdriver.Chrome()
        dfs = []
        for year in years:
            driver.get(url + year)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            table = soup.find('table')
            headers = [header.text.strip().replace("Life expectancy at birth (historical)years •", "") for header in
                       table.find_all('th')]
            headers = [header.replace("Region", "Country") for header in headers]
            rows = table.find_all('tr')
            data = []
            for row in rows:
                cols = row.find_all('td')
                cols = [float(ele.text.strip().replace(',', '').replace('\xa0years', '')) if ele.text.strip().replace(',',
                                                                                                                   '').replace(
                    ' years', '').replace('.', '').isdigit() else ele.text.strip().replace('\xa0years', '') for ele in
                        cols]
                if cols:
                    data.append(cols)
            dfs.append(pd.DataFrame(data, columns=headers))

        driver.quit()

        combined_df = dfs[0]
        for i in range(1, len(dfs)):
            combined_df = pd.merge(combined_df, dfs[i], how="outer")
        combined_df.to_csv(csv_file, index=False)
    else:
        print("File already exists")


# Function to scrape land area data
def land_area_data():
    url = 'https://ourworldindata.org/grapher/land-area-km?tab=table'
    csv_file = os.path.join(SCRAPED_PATH, 'landarea_data.csv')

    if not os.path.isfile(csv_file):
        driver = webdriver.Chrome()
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = soup.find('table')
        headers = [header.text.strip().replace("square kilometres • 2021", "") for header in table.find_all('th')]
        headers = [header.replace("Country or region", "Country") for header in headers]
        rows = table.find_all('tr')
        data = []
        for row in rows:
            cols = row.find_all('td')
            cols = [float(ele.text.strip().replace(',', '').replace('\xa0km²', '')) if ele.text.strip().replace(',',
                                                                                                             '').replace(
                '\xa0km²', '').replace('.', '').isdigit() else ele.text.strip().replace('\xa0km²', '') for ele in cols]
            if cols:
                data.append(cols)

        driver.quit()
        df = pd.DataFrame(data, columns=headers)
        df.to_csv(csv_file, index=False)
    else:
        print("File already exists")


#Function to scrape internet data
def internet_data():
    years = ["2017"]
    url = 'https://ourworldindata.org/grapher/share-of-individuals-using-the-internet?tab=table&time='
    csv_file = os.path.join(SCRAPED_PATH, 'internet_data.csv')

    if not os.path.isfile(csv_file):
        driver = webdriver.Chrome()
        dfs = []
        for year in years:
            driver.get(url + year)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            table = soup.find('table')
            headers = [
                header.text.strip().replace("Individuals using the Internet (% of population)% of population •", "") for
                header in table.find_all('th')]
            headers = [header.replace("Country or region", "Country") for header in headers]
            rows = table.find_all('tr')
            data = []
            for row in rows:
                cols = row.find_all('td')
                cols = [float(ele.text.strip().replace(',', '').replace('%', '')) if ele.text.strip().replace(',',
                                                                                                              '').isdigit() else ele.text.strip().replace(
                    '%', '') for ele in cols]
                cols = [ele.split()[1] if ele.split() != [] and ele.split()[0].isdigit() else ele for ele in cols]
                if cols:
                    data.append(cols)
            dfs.append(pd.DataFrame(data, columns=headers))
        driver.quit()
        combined_df = dfs[0]
        for i in range(1, len(dfs)):
            combined_df = pd.merge(combined_df, dfs[i], how="outer")

        combined_df.to_csv(csv_file, index=False)
    else:
        print("File already exists")


# Function to scrape happiness data
def happiness_data():
    years = ["2017"]
    url = 'https://ourworldindata.org/grapher/happiness-cantril-ladder?tab=table&time='
    csv_file = os.path.join(SCRAPED_PATH, 'happiness_data.csv')

    if not os.path.isfile(csv_file):
        driver = webdriver.Chrome()
        dfs = []
        for year in years:
            driver.get(url + year)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            table = soup.find('table')
            headers = [
                header.text.strip().replace("World Happiness Report 2016Cantril Ladder (0=worst; 10=best) • ", "") for
                header in table.find_all('th')]
            headers = [header.replace("Country or region", "Country") for header in headers]
            rows = table.find_all('tr')
            data = []
            for row in rows:
                cols = row.find_all('td')
                cols = [float(ele.text.strip().replace(',', '')) if ele.text.strip().replace(',',
                                                                                             '').isdigit() else ele.text.strip()
                        for ele in cols]
                cols = [ele.split()[1] if ele.split() != [] and ele.split()[0].isdigit() else ele for ele in cols]
                if cols:
                    data.append(cols)
            dfs.append(pd.DataFrame(data, columns=headers))
        driver.quit()
        combined_df = dfs[0]
        for i in range(1, len(dfs)):
            combined_df = pd.merge(combined_df, dfs[i], how="outer")

        combined_df.to_csv(csv_file, index=False)
    else:
        print("File already exists")


# Function to scrape GDP data
def gdp_data():
    years = ["2017"]
    url = 'https://ourworldindata.org/grapher/gdp-per-capita-maddison-2020?tab=table&time='
    csv_file = os.path.join(SCRAPED_PATH, 'gdp_data.csv')

    if not os.path.isfile(csv_file):
        driver = webdriver.Chrome()
        dfs = []
        for year in years:
            driver.get(url + year)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            table = soup.find('table')
            headers = [header.text.strip().replace("GDP per capitainternational-$ in 2011 prices •", "") for
                       header in table.find_all('th')]
            headers = [header.replace("Country or region", "Country") for header in headers]
            rows = table.find_all('tr')
            data = []
            for row in rows:
                cols = row.find_all('td')
                cols = [float(ele.text.strip().replace(',', '').replace('$', '')) if ele.text.strip().replace(',',
                                                                                                              '').replace(
                    '$', '').isdigit() else ele.text.strip().replace('$', '') for ele in cols]
                if cols:
                    data.append(cols)
            dfs.append(pd.DataFrame(data, columns=headers))
        driver.quit()
        combined_df = dfs[0]
        for i in range(1, len(dfs)):
            combined_df = pd.merge(combined_df, dfs[i], how="outer")

        combined_df.to_csv(csv_file, index=False)
    else:
        print("File already exists")


# Function to scrape demography data
def demography_data():
    years = ["2017"]
    url_p1 = 'https://ourworldindata.org/explorers/population-and-demography?tab=table&time='
    url_p2 = '&facet=none&hideControls=false&Metric=Population&Sex=Both+sexes&Age+group=Total&Projection+Scenario=None'
    csv_file = os.path.join(SCRAPED_PATH, 'demography_data.csv')

    if not os.path.isfile(csv_file):
        driver = webdriver.Chrome()
        dfs = []
        for year in years:
            driver.get(url_p1 + year + url_p2)
            time.sleep(1)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            table = soup.find('table')
            headers = [header.text.strip().replace("Populationpeople • ", "") for header in table.find_all('th')]
            headers = [header.replace("Country or region", "Country") for header in headers]
            rows = table.find_all('tr')
            data = []
            for row in rows:
                cols = row.find_all('td')
                cols = [float(ele.text.strip().replace(',', '')) if ele.text.strip().replace(',',
                                                                                             '').isdigit() else ele.text.strip()
                        for ele in cols]
                if cols:
                    data.append(cols)
            dfs.append(pd.DataFrame(data, columns=headers))
        driver.quit()

        combined_df = dfs[0]
        for i in range(1, len(dfs)):
            combined_df = pd.merge(combined_df, dfs[i], how="outer")

        combined_df.to_csv(csv_file, index=False)
    else:
        print("File already exists")


# Function to scrape alcohol and drug data
def alcohol_drug_data():
    years = ["2017"]
    url = 'https://ourworldindata.org/grapher/share-with-alcohol-or-drug-use-disorders?tab=table&time='
    csv_file = os.path.join(SCRAPED_PATH, 'alcoholdrug_data.csv')

    if not os.path.isfile(csv_file):
        driver = webdriver.Chrome()
        dfs = []
        for year in years:
            driver.get(url + year)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            table = soup.find('table')
            headers = [header.text.strip().replace(
                "Prevalence - Substance use disorders - Sex: Both - Age: Age-standardized (Percent)percent • ", "") for
                       header in table.find_all('th')]
            headers = [header.replace("Country or region", "Country") for header in headers]
            rows = table.find_all('tr')
            data = []
            for row in rows:
                cols = row.find_all('td')
                cols = [float(ele.text.strip().replace(',', '').replace('%', '')) if ele.text.strip().replace(',',
                                                                                                              '').isdigit() else ele.text.strip().replace(
                    '%', '') for ele in cols]
                cols = [ele.split()[1] if ele.split() != [] and ele.split()[0].isdigit() else ele for ele in cols]
                if cols:
                    data.append(cols)
            dfs.append(pd.DataFrame(data, columns=headers))
        driver.quit()
        combined_df = dfs[0]
        for i in range(1, len(dfs)):
            combined_df = pd.merge(combined_df, dfs[i], how="outer")

        combined_df.to_csv(csv_file, index=False)
    else:
        print("File already exists")

if __name__ == "__main__":
    # Scraping all necessary data
    suicides_data()
    population_density_data()
    pollution_data()
    mental_disorders_data()
    median_age_data()
    life_expectancy_data()
    land_area_data()
    internet_data()
    happiness_data()
    gdp_data()
    demography_data()
    alcohol_drug_data()