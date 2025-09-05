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
        # Cargar datos de PBI
        pbi_df = pd.read_csv('data_limpia/PBI.csv')
        
        # Cargar datos de sedes
        sedes_df = pd.read_csv('data_limpia/SEDES.csv')
        
        return pbi_df, sedes_df
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None, None

def visualizacion_b_boxplot_pbi_por_region():
    """b. Boxplot del PBI per cápita 2023 por región geográfica para países con delegación argentina"""
    pbi_df, sedes_df = cargar_datos()
    
    if pbi_df is None or sedes_df is None:
        print("No se pudieron cargar los datos necesarios")
        return
    
    # Obtener países con delegación argentina
    paises_con_delegacion = sedes_df['pais_iso_3'].unique()
    
    # Filtrar PBI para países con delegación argentina
    pbi_delegacion = pbi_df[pbi_df['Country Code'].isin(paises_con_delegacion)].copy()
    
    # Hacer merge con información de región geográfica
    pbi_con_region = pbi_delegacion.merge(
        sedes_df[['pais_iso_3', 'region_geografica']].drop_duplicates(), 
        left_on='Country Code', 
        right_on='pais_iso_3', 
        how='inner'
    )
    
    # Calcular medianas por región para ordenar
    medianas_por_region = pbi_con_region.groupby('region_geografica')['2023'].median().sort_values(ascending=False)
    
    # Ordenar las regiones por mediana
    pbi_con_region['region_ordenada'] = pd.Categorical(
        pbi_con_region['region_geografica'], 
        categories=medianas_por_region.index, 
        ordered=True
    )
    
    # Crear el boxplot
    plt.figure(figsize=(14, 8))
    
    # Crear el boxplot
    box_plot = plt.boxplot([pbi_con_region[pbi_con_region['region_ordenada'] == region]['2023'].values 
                           for region in medianas_por_region.index],
                          labels=medianas_por_region.index,
                          patch_artist=True)
    
    # Colorear las cajas usando seaborn palette
    colors = sns.color_palette("husl", len(medianas_por_region))
    for patch, color in zip(box_plot['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    # Personalizar el gráfico
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('PBI per cápita 2023 (USD)', fontsize=12, fontweight='bold')
    plt.xlabel('Región Geográfica', fontsize=12, fontweight='bold')
    plt.title('Boxplot del PBI per cápita 2023 por Región Geográfica\n(Países con delegación argentina, ordenado por mediana)', 
              fontsize=14, fontweight='bold', pad=20)
    
    # Agregar grid
    plt.grid(axis='y', alpha=0.3)
    
    # Ajustar layout y guardar
    plt.tight_layout()
    plt.savefig('graficos/grafico_2/grafico_2.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Visualización B completada: Boxplot PBI per cápita por región")
    print("Gráfico guardado como: grafico_2.png")

if __name__ == "__main__":
    visualizacion_b_boxplot_pbi_por_region()