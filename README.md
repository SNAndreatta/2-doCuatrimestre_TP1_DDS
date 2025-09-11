# Análisis PBI vs Sedes Diplomáticas Argentinas

## Descripción
Este proyecto corresponde al **Trabajo Práctico Nº1** de la materia *Desarrollo de Sistemas* (Instituto Industrial Luis A. Huergo, 2025 – Cuatrimestre Nº2).  
El objetivo es analizar la relación entre el **PBI per cápita de los países (2023)** y la cantidad de **sedes diplomáticas argentinas** en el exterior.  

Se trabajó con datos abiertos del **Banco Mundial** y del **Ministerio de Relaciones Exteriores de Argentina**, realizando procesos de **limpieza**, **normalización**, **análisis estadístico** y **visualización de datos**.

---

## Estructura del proyecto

```plaintext
.
├── core/                # Clase CustomDataFrame y utilidades
├── data_limpia/         # Datos procesados y corregidos
├── reportes/            # Reportes estadísticos (CSV + scripts)
└── graficos/            # Gráficos generados (PNG + scripts)
```
---

## Actividades principales
- **Limpieza de datos**: eliminación de comentarios, normalización de columnas, imputación y filtrado de valores faltantes.  
- **Procesamiento**: implementación de la clase `CustomDataFrame` para encapsular operaciones de pandas.  
- **Reportes**: generación de reportes estadísticos en formato `.csv`.  
- **Visualizaciones**: gráficos con *matplotlib* y *seaborn* para el análisis exploratorio.  
- **Análisis de correlación**: estudio de la relación entre PBI per cápita y número de sedes diplomáticas.  

---

## Resultados
- La correlación entre **PBI per cápita** y **cantidad de sedes** es **débil positiva (0.107)**.  
- Se concluye que la distribución de sedes argentinas responde más a **factores geográficos, históricos y estratégicos** que al nivel económico de los países.  
- Casos puntuales (EE.UU., China, Canadá) muestran correspondencia entre economía y cantidad de sedes, pero no son la regla general.  

---

## Tecnologías utilizadas
- **Python 3**  
- **pandas** (procesamiento de datos)  
- **matplotlib** y **seaborn** (visualización)  

---

## Fuentes de datos
- [Representaciones argentinas en el exterior – datos.gob.ar](https://datos.gob.ar/dataset/exterior-representaciones-argentinas)  
- [World Bank – GDP per capita (NY.GDP.PCAP.CD)](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD)  

---

## Autores
- Santino Nicolas Andreatta  
- Pedro Villarino  
- Galo Fernandez Achille  
