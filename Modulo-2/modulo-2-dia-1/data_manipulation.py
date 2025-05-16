import pandas as pd

df_csv = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv")
df_json = pd.read_json("https://jsonplaceholder.typicode.com/users")

print(df_csv.head(5))
print(df_json.head(5))
df_csv = df_csv.melt(id_vars="Month",var_name="Year",value_name="pasajeros")
print(df_csv.head(5))