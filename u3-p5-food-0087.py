import pandas as pd
import matplotlib.pyplot as plt
# Alonso Lopez Garcia NC = 0087 | Fecha 23/11/2026
# 1. Leer el archivo CSV
df_food_india = pd.read_csv("indian_food.csv")
print("\n--- DATOS LEÍDOS DESDE CSV, COMIDA INDIA - 0087---")
print(df_food_india)
print("--- MOSTRAR NOMBRE COMIDA + INGREDIENTES - 0087---")
recetas = df_food_india[["name", "ingredients"]]
print(recetas)

print("--- MOTRAR 10 PRIMEROS REGISTROS DE TIEMPO DE COCINADO CON HEAD - 0087---")
nombre_y_hora = df_food_india[["name", "cook_time"]].head(10)
print(nombre_y_hora )
print("--- GRÁFICA COMIDA (X) TIEMPO DE COCINADO (Y) - 0087---")
print("--- GRÁFICA COMIDA (X) TEXTO A 30° GRADOS - 0087---")
nombre_y_hora.plot.bar(x="name",y="cook_time", rot=30)
plt.title ("Comida tipica de la India - 0087")
plt.xlabel("Nombre de la comida ")
plt.ylabel("Tiempo de cocinado")
plt.show()

print("--- GRÁFICA DE VARIAS COLUMNAS - ALONSO 0087---")
nombre_y_hora_prep = df_food_india[["name", "prep_time", "cook_time"]].head(10)
nombre_y_hora_prep.plot.bar(x="name", rot=30)
plt.title ("Comida de dos culmnas de la India - 0087")
plt.xlabel("Nombre de la comida ")
plt.ylabel("Tiempo de cocinado y preparación")
plt.show()

print("--- GRÁFICAS APILADAS UNA TRAS OTRA VERTICALMENTE - ALONSO 0087---")
nombre_y_hora_prep.plot.bar(x='name', stacked=True, rot=30)
plt.title ("Grafica con columnnas apiladas de la India - 0087")
plt.xlabel("Nombre de la comida ")
plt.ylabel("Tiempo de cocinado y preparación")
plt.show()

