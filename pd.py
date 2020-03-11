import pandas as pd
import pprint

data_set = pd.read_csv(r'data/2019_nCoV_data.csv')
print(data_set.head())
print(data_set.columns)

countries = data_set['Country'].tolist()


unique_countries = list(dict.fromkeys(countries))
pprint.pprint(unique_countries, indent = 4)


for country in unique_countries:
    total = 0
    for curr_country in countries:
        if curr_country == country:
            total += 1
    print("{} cases in {}".format(total, country))
