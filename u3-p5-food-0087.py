import pandas as pd
import matplotlib.pyplot as plt
# Alonso Lopez Garcia NC = 0087 | Fecha 23/11/2026
# 1. Leer el archivo CSV
df_food_india = pd.read_csv('indian_food.csv')
print("\n--- DATOS LEÍDOS DESDE CSV, COMIDA INDIA - 0087---")
print(df_food_india)
print("--- MOSTRAR NOMBRE COMIDA + INGREDIENTES - 0087---")
recetas = df_food_india[['name', 'ingredients']]
print(recetas)

print("--- MOTRAR 10 PRIMEROS REGISTROS DE TIEMPO DE COCINADO CON HEAD - 0087---")
name_and_time = df_food_india[['name', 'cook_time']].head(10)
print(name_and_time )