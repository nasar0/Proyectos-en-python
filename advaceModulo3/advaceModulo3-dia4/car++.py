import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(url)

df = df[["mpg", "cylinders", "hp", "weightlbs"]].dropna()

X = df[[ "cylinders", "hp", "weightlbs"]]
y = df["mpg"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

modelo_lineal = LinearRegression()
modelo_ridge = Ridge(alpha=1.0)
modelo_lasso = Lasso(alpha=0.1)

modelo_lineal.fit(X_train, y_train)
modelo_ridge.fit(X_train, y_train)
modelo_lasso.fit(X_train, y_train)

y_pred_lineal = modelo_lineal.predict(X_test)
y_pred_ridge = modelo_ridge.predict(X_test)
y_pred_lasso = modelo_lasso.predict(X_test)

def evaluar_modelo(nombre, y_test, y_pred):
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"{nombre} - MSE: {mse:.2f}, R²: {r2:.2f}")
    plt.scatter(y_test, y_pred)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.xlabel(nombre)
    plt.ylabel("Precio predicho")
    plt.title("Regresión: Precio real vs Predicho")
    plt.grid(True)
    plt.show()

evaluar_modelo("Regresión Lineal", y_test, y_pred_lineal)
evaluar_modelo("Ridge", y_test, y_pred_ridge)
evaluar_modelo("Lasso", y_test, y_pred_lasso)

coef = pd.DataFrame({
    "Lineal": modelo_lineal.coef_,
    "Ridge": modelo_ridge.coef_,
    "Lasso": modelo_lasso.coef_,
}, index=X.columns)

coef.plot(kind='barh')
plt.title("Coeficientes por modelo")
plt.xlabel("Valor del coeficiente")
plt.grid(True)
plt.show()