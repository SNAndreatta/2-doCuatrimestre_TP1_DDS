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

def visualizacion_c_relacion_pbi_sedes_alternativa():
    """c. Relación entre PBI per cápita 2023 y cantidad de sedes argentinas - Versión alternativa"""
    pbi_df, sedes_df = cargar_datos()
    
    if pbi_df is None or sedes_df is None:
        print("No se pudieron cargar los datos necesarios")
        return
    
    # Contar sedes por país
    sedes_por_pais = sedes_df.groupby('pais_iso_3').size().reset_index(name='cantidad_sedes')
    
    # Hacer merge con datos de PBI
    datos_completos = pbi_df.merge(sedes_por_pais, left_on='Country Code', right_on='pais_iso_3', how='inner')
    
    # Crear el scatter plot con figura más grande
    plt.figure(figsize=(16, 10))
    
    # Crear el scatter plot con colores por región
    regiones = datos_completos.merge(sedes_df[['pais_iso_3', 'region_geografica']].drop_duplicates(), 
                                   on='pais_iso_3', how='left')
    
    # Obtener colores únicos para cada región usando seaborn
    regiones_unicas = regiones['region_geografica'].unique()
    colores = sns.color_palette("husl", len(regiones_unicas))
    color_map = dict(zip(regiones_unicas, colores))
    
    # Crear scatter plot con puntos normales
    for region in regiones_unicas:
        datos_region = regiones[regiones['region_geografica'] == region]
        plt.scatter(datos_region['2023'], datos_region['cantidad_sedes'], 
                   c=[color_map[region]], label=region, alpha=0.8, s=100)
    
    # Agregar línea de tendencia original
    z = np.polyfit(datos_completos['2023'], datos_completos['cantidad_sedes'], 1)
    p = np.poly1d(z)
    plt.plot(datos_completos['2023'], p(datos_completos['2023']), 
             "r--", alpha=0.8, linewidth=2, label=f'Tendencia (pendiente: {z[0]:.2e})')
    
    # Agregar línea de mediana móvil para mostrar otra perspectiva de la relación
    # Ordenar datos por PBI
    datos_ordenados = datos_completos.sort_values('2023')
    # Calcular mediana móvil cada 10 países
    ventana = 10
    medianas_moviles = []
    pbi_medianas = []
    
    for i in range(0, len(datos_ordenados), ventana):
        grupo = datos_ordenados.iloc[i:i+ventana]
        if len(grupo) > 0:
            medianas_moviles.append(grupo['cantidad_sedes'].median())
            pbi_medianas.append(grupo['2023'].mean())
    
    plt.plot(pbi_medianas, medianas_moviles, 
             "g-", alpha=0.8, linewidth=3, label=f'Mediana móvil (ventana={ventana})')
    
    # Personalizar el gráfico
    plt.xlabel('PBI per cápita 2023 (USD)', fontsize=12, fontweight='bold')
    plt.ylabel('Cantidad de Sedes Argentinas', fontsize=12, fontweight='bold')
    plt.title('Relación entre PBI per cápita 2023 y Cantidad de Sedes Argentinas\npor País - Visualización Alternativa', 
              fontsize=14, fontweight='bold', pad=20)
    
    # Agregar leyenda
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Agregar grid
    plt.grid(True, alpha=0.3)
    
    # Calcular y mostrar correlación
    correlacion = datos_completos['2023'].corr(datos_completos['cantidad_sedes'])
    plt.text(0.02, 0.98, f'Correlación: {correlacion:.3f}', 
             transform=plt.gca().transAxes, fontsize=12, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.8),
             verticalalignment='top')
    
    # Ajustar layout y guardar
    plt.tight_layout()
    plt.savefig('graficos/grafico_3_1/grafico_3_1.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Correlación entre PBI per cápita y cantidad de sedes: {correlacion:.3f}")
    print("Visualización C alternativa completada: Relación PBI per cápita vs cantidad de sedes")
    print("Gráfico guardado como: grafico_3_1.png")

if __name__ == "__main__":
    visualizacion_c_relacion_pbi_sedes_alternativa()
