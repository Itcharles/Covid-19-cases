import pandas as pd

# Loading excel files.
df1 = pd.read_excel('C:\\ Your directory \\Covid cases.xlsx')
df2 = pd.read_excel('C:\\ Your directory \\Covid vaccinations.xlsx')

# Saving files in csv format.
df1.to_csv('Covid cases csv.csv', index=False
df2.to_csv('Covid vacinnations csv.csv', index=False           
