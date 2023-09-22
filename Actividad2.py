import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
iris_df = pd.read_csv('Iris.csv')

# Gráfico de barras de la variable "Species"
species_counts = iris_df['Species'].value_counts()
plt.bar(species_counts.index, species_counts.values)
plt.xlabel('Especies')
plt.ylabel('Número de Ejemplares')
plt.title('Distribución de Especies en el Conjunto de Datos Iris')
plt.show()

# Gráfico de histograma de la variable "SepalWidthCm"
plt.hist(iris_df['SepalWidthCm'], bins=10, edgecolor='k')
plt.xlabel('Ancho del Sépalo (cm)')
plt.ylabel('Frecuencia')
plt.title('Histograma del Ancho del Sépalo en el Conjunto de Datos Iris')
plt.show()