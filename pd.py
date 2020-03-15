import pandas as pd
import pprint

data_set = pd.read_csv(r'data/2019_nCoV_data.csv') # load the data set
countries = data_set['Country'].tolist() # convert the dataframe of Country into a list

# basically uses the list value, which hold redundancy, and makes a dict aka hash map. Hash
# maps only allow unique key values which means it'll get rid of all the redundant countries
# and we're left with unique countries. Now we just convert the dict back to a list since 
# that was our original goal
unique_countries = list(dict.fromkeys(countries))
df = pd.DataFrame()

print(df)
t_provinces = []
t_confirmed = []

# to find the total number of provinces to report corona virus in each country
for country in unique_countries:
	provinces = data_set.loc[data_set['Country'] == country]
	total = sum(provinces['Confirmed'].tolist())
	t_provinces.append(len(provinces))
	t_confirmed.append(total)

df['Country'] = unique_countries
df['Provinces'] = t_provinces
df['Confirmed'] = t_confirmed
print(df)
