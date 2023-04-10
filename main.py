import geopandas as gpd
import pandas as pd

# Lê o arquivo XLSX
df = pd.read_excel('Resultado Merge.xlsx')

# Cria um GeoDataFrame a partir do DataFrame, usando as colunas de latitude e longitude como geometria
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df['ende_longitude'], df['ende_latitude']))

# Salva o arquivo como GeoJSON
gdf.to_file('arquivo2.geojson', driver='GeoJSON')
