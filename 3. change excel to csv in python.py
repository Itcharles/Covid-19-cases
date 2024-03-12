import pandas as pd

# Loading excel files.
df1 = pd.read_excel('C:\\ Your directory \\Covid cases.xlsx')
df2 = pd.read_excel('C:\\ Your directory \\Covid vaccinations.xlsx')

# We need to change population column to float type in Covid cases.xlsx otherwise we will no be able to load the data to SQL:
if 'population' in df1.columns:
  df1['population'] = df1['population'].astype('float')

# Saving files in csv format.
df1.to_csv('Covid cases csv.csv', index=False
df2.to_csv('Covid vacinnations csv.csv', index=False           
