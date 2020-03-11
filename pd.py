import pandas as pd
import pprint

data_set = pd.read_csv(r'data/2019_nCoV_data.csv') # load the data set
print(data_set.head()) # prints the first few data set 
print(data_set.columns) # prints the column name values e.g. name, email, etc

countries = data_set['Country'].tolist() # convert the dataframe of Country into a list


# basically uses the list value, which hold redundancy, and makes a dict aka hash map. Hash
# maps only allow unique key values which means it'll get rid of all the redundant countries
# and we're left with unique countries. Now we just convert the dict back to a list since 
# that was our original goal
unique_countries = list(dict.fromkeys(countries)) 
pprint.pprint(unique_countries, indent = 4) #show the unique countries


# to find the total number of provinces to report corona virus in each country
for country in unique_countries:
    total = 0
    for curr_country in countries:
        if curr_country == country:
            total += 1
    print("{} province(s) reported to have corona virus in {}".format(total, country))
