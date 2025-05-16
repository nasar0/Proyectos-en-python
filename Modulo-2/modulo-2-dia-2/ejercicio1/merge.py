import pandas as pd
df_a = pd.DataFrame({
    "id": [1, 2, 3],
    "nombre": ["Ana", "Luis", "Sofía"]
})

df_b = pd.DataFrame({
    "id": [1, 2, 4],
    "edad": [23, 30, 40]
})

df = pd.merge(df_a,df_b,on="id",how = "inner")
print(df)
df = pd.merge(df_a,df_b,on="id",how = "outer")
print(df)
df = pd.merge(df_a,df_b,on="id",how = "left")
print(df)
df = pd.merge(df_a,df_b,on="id",how = "right")
print(df)