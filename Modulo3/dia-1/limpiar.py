import pandas as pd
import numpy as np

datos_sucios = {
    "Nombre": [" Ana", "Luis", None, "Carlos", "maria"],
    "Edad": ["28", "35", None, "22", "treinta"],
    "Ciudad": ["madrid", "Barcelona", "Sevilla", np.nan, "valencia"],
    "Apellido": ["Martinez", "Martinez", "Martinez", None, "Martinez"]
}

df = pd.DataFrame(datos_sucios)

def clean_data(df):
    # Procesar columnas no numéricas primero
    for col in df.select_dtypes(exclude=['number']).columns:
        df[col] = df[col].fillna("Desconocido").astype(str).str.strip().str.capitalize()

    # Procesar columnas numéricas
    for col in df.select_dtypes(include=['object']).columns:
        # Intentar convertir a numérico
        converted = pd.to_numeric(df[col], errors='coerce')
        if not converted.isna().all():  # Si al menos algunos valores son numéricos
            df[col] = converted
            media = df[col].mean()
            df[col] = df[col].fillna(round(media))

    return df

df_clean = clean_data(df.copy())
print(df_clean)