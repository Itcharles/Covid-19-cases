import pandas as pd



# Load data
data_path = 'https://github.com/Itcharles/Data-Analyst-Project---Covid-cases/blob/099eceed7a11db3d2444ddffeabf3c834968416c/1.%20Covid%20cases.xlsx'
covid_data = pd.read_url(data_path)


#1 QUERY: Total number of cases and deaths and the mortality rate

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


#2 QUERY:  Total Death by continent:

aggregated_data2 = filtered_data.groupby('continent')['new_deaths'].sum()\
    .reset_index(name='Total Deaths').sort_values(by='Total Deaths',\
                                                      ascending=False).reset_index(drop=True)


# We need start indexing from 1:
aggregated_data2.index += 1

#Our second data to visualize:
print(aggregated_data2)


#3 QUERYy: People infected and percentage infected per country:

# Aggregating data to calculate the maximum number of infected individuals
aggregated_data3 = (filtered_data.groupby(['location', 'population'])
                    .agg(TotalPeopleInfected=('total_cases', 'max'))
                    .reset_index())

# Calculating the percentage of the population that is infected
aggregated_data3['PercentagePopulationInfected'] = (aggregated_data3['TotalPeopleInfected'] / aggregated_data3['population']) * 100

# Sorting the data by the percentage of the population that is infected
aggregated_data3 = aggregated_data3.sort_values(by='PercentagePopulationInfected', ascending=False)

# Our 3 data to visualize:
print(aggregated_data3)


#4 QUERY: Total people infection history per country:

# Aggregating data to calculate the maximum number of infected individuals
aggregated_data4 = (filtered_data.groupby(['location', 'population', 'date'])
                    .agg(TotalPeopleInfected=('total_cases', 'max'))
                    .reset_index())

# Calculating the percentage of the population that is infected
aggregated_data4['PercentagePopulationInfected'] = (aggregated_data4['TotalPeopleInfected'] / aggregated_data3['population']) * 100

# Sorting the data by the percentage of the population that is infected
aggregated_data4 = aggregated_data4.sort_values(by='PercentagePopulationInfected', ascending=False)

# Our 4 data to visualize:
print(aggregated_data4)















