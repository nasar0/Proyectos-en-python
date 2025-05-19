import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(url)

df = df[["mpg", "cylinders", "hp", "weightlbs"]].dropna()

df["peso_hp_ratio"] = df["weightlbs"] / df["hp"]
df["potencia_log"] = np.log(df["hp"])

df["peso_hp_ratio"] = (df["peso_hp_ratio"] - df["peso_hp_ratio"].mean()) / df["peso_hp_ratio"].std()


X = df[[ "cylinders", "hp", "weightlbs","peso_hp_ratio","potencia_log"]]
y = df["mpg"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

df.corr()["mpg"].sort_values(ascending=False)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel("Precio real")
plt.ylabel("Precio predicho")
plt.title("Regresión: Precio real vs Predicho")
plt.grid(True)
plt.show()

errores = y_test - y_pred

plt.hist(errores, bins=20, edgecolor='black')
plt.title("Distribución de errores (residuos)")
plt.xlabel("Error")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.show()

coeficientes = pd.Series(modelo.coef_, index=X.columns)
coeficientes.plot(kind='barh')
plt.title("Importancia de cada variable (coeficientes)")
plt.xlabel("Peso en la predicción del precio")
plt.grid(True)
plt.show()