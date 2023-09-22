import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
salario_df = pd.read_csv('Salario.csv')

# Hallar la matriz de correlación de Pearson
correlation_matrix_pearson = salario_df.corr(method='pearson')
print("Matriz de correlación de Pearson:")
print(correlation_matrix_pearson)

# Hallar la matriz de correlación de Spearman
correlation_matrix_spearman = salario_df.corr(method='spearman')
print("\nMatriz de correlación de Spearman:")
print(correlation_matrix_spearman)

# Graficar las variables "edad" vs "estudio" y escribir la interpretación del gráfico
plt.scatter(salario_df['edad'], salario_df['estudio'])
plt.xlabel('Edad')
plt.ylabel('Nivel de Estudios')
plt.title('Edad vs Nivel de Estudios')
plt.show()

# Interpretación del gráfico de "edad" vs "estudio":
# El gráfico de dispersión muestra la relación entre la edad y el nivel de estudios de los individuos. Observando el gráfico, podemos notar si existe alguna tendencia o patrón en los datos. Por ejemplo, si los puntos tienden a agruparse de cierta manera, podríamos inferir una posible correlación entre estas dos variables. La interpretación específica dependerá de cómo se distribuyan los puntos en el gráfico.

# Graficar las variables "estudio" vs "ingreso" y escribir la interpretación del gráfico
plt.scatter(salario_df['estudio'], salario_df['ingreso'])
plt.xlabel('Nivel de Estudios')
plt.ylabel('Ingreso')
plt.title('Nivel de Estudios vs Ingreso')
plt.show()

# Interpretación del gráfico de "estudio" vs "ingreso":
# El gráfico de dispersión muestra la relación entre el nivel de estudios y el ingreso de los individuos. Observando el gráfico, podemos evaluar si existe alguna relación entre estas dos variables. Si los puntos tienden a formar una tendencia ascendente o descendente, podría indicar una correlación entre ellas. Por ejemplo, si a medida que aumenta el nivel de estudios, el ingreso tiende a aumentar, esto podría sugerir una correlación positiva entre el nivel de estudios y el ingreso.
