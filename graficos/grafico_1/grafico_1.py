import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Configurar el estilo de los gráficos
plt.style.use('default')
sns.set_palette("husl")

def cargar_datos():
    """Cargar los datos desde los archivos CSV"""
    try:
        # Cargar datos de sedes
        sedes_df = pd.read_csv('data_limpia/SEDES.csv')
        return sedes_df
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None

def visualizacion_a_cantidad_sedes_por_region():
    """a. Cantidad de sedes por región geográfica ordenadas de manera decreciente"""
    sedes_df = cargar_datos()
    
    if sedes_df is None:
        print("No se pudieron cargar los datos de sedes")
        return
    
    # Contar sedes por región geográfica
    sedes_por_region = sedes_df['region_geografica'].value_counts().sort_values(ascending=True)
    
    # Crear el gráfico
    plt.figure(figsize=(12, 8))
    colors = sns.color_palette("husl", len(sedes_por_region))
    bars = plt.barh(range(len(sedes_por_region)), sedes_por_region.values, color=colors)
    
    # Personalizar el gráfico
    plt.yticks(range(len(sedes_por_region)), sedes_por_region.index)
    plt.xlabel('Cantidad de Sedes', fontsize=12, fontweight='bold')
    plt.ylabel('Región Geográfica', fontsize=12, fontweight='bold')
    plt.title('Cantidad de Sedes por Región Geográfica\n(Ordenado de manera decreciente)', 
              fontsize=14, fontweight='bold', pad=20)
    
    # Agregar valores en las barras
    for i, bar in enumerate(bars):
        width = bar.get_width()
        plt.text(width + 0.1, bar.get_y() + bar.get_height()/2, 
                f'{int(width)}', ha='left', va='center', fontweight='bold')
    
    # Mejorar la apariencia
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.savefig('graficos/grafico_1/grafico_1.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Visualización A completada: Cantidad de sedes por región geográfica")
    print("Gráfico guardado como: grafico_1.png")

if __name__ == "__main__":
    visualizacion_a_cantidad_sedes_por_region()