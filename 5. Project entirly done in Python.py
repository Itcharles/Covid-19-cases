import pandas as pd
import matplotlib.pyplot as plt


# Load data
data_path = 'https://github.com/Itcharles/Data-Analyst-Project---Covid-cases/blob/099eceed7a11db3d2444ddffeabf3c834968416c/1.%20Covid%20cases.xlsx'
covid_data = pd.read_url(data_path)


# Query 1: Total number of cases and deaths and the mortality rate

# Filter rows to include only those with a non-empty value in the 'continent' column
filtered_data = covid_data[covid_data['continent'].notna()]

# Aggregate data, calculating the sum of new cases and deaths
aggregated_data = {
    'total_cases': filtered_data['new_cases'].sum(),
    'total_deaths': filtered_data['new_deaths'].sum()
}

# Calculate the mortality rate
aggregated_data['death_percentage'] = (aggregated_data['total_deaths'] / aggregated_data['total_cases']) * 100

#Our first data to visualize:
print(aggregated_data) 


#Query 2:  Total Death by continent:

aggregated_data2 = filtered_data.groupby('continent')['new_deaths'].sum()\
    .reset_index(name='Total Deaths').sort_values(by='Total Deaths',\
                                                      ascending=False).reset_index(drop=True)
# We need start indexing from 1:
aggregated_data2.index += 1

#Our second data to visualize:
print(aggregated_data2)


