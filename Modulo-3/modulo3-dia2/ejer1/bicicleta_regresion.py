import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

np.random.seed(42)

n = 100
df = pd.DataFrame({
    "tamaño_rueda": np.random.choice([26, 27.5, 29], size=n),
    "peso": np.round(np.random.normal(12, 1.5, n), 1),  # en kg
    "marca_premium": np.random.choice([0, 1], size=n)
})

# Puedes crear una fórmula ficticia para simular el precio
df["precio"] = (
    100 * df["marca_premium"] +
    15 * df["tamaño_rueda"] -
    10 * df["peso"] +
    np.random.normal(0, 25, n)  # ruido
).round(2)

X = df[["tamaño_rueda", "peso", "marca_premium"]]
y = df["precio"]

modelo = LinearRegression()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

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