#roads_near_lakes.py

import geopandas as gpd
import os
from shapely.geometry import Polygon
from qgis.core import QgsVectorLayer, QgsProject

# --- File paths ---
data_base = r"C:\Users\JohnKenny\OneDrive - Pathway to Adventure Council\Desktop\qgis\project1\data"
output_base = r"C:\Users\JohnKenny\OneDrive - Pathway to Adventure Council\Desktop\qgis\project1\outputs"

lakes_path = os.path.join(data_base, "tl_2024_17097_areawater", "tl_2024_17097_areawater.shp")
roads_path = os.path.join(data_base, "tl_2024_17097_roads", "tl_2024_17097_roads.shp")
output_path = os.path.join(output_base, "roads_within_100ft_of_lake.shp")

# --- Load layers and reproject to EPSG:3435 (IL State Plane East) ---
lakes = gpd.read_file(lakes_path).to_crs(epsg=3435)
roads = gpd.read_file(roads_path).to_crs(epsg=3435)

# --- Buffer lakes by 30.5 meters (100 ft) ---
lake_buffer = lakes.buffer(30.5)
lake_buffer_union = gpd.GeoDataFrame(geometry=[lake_buffer.unary_union], crs="EPSG:3435")

# --- Spatial join: roads that intersect the lake buffer zone ---
print("Finding roads within 100 ft of any lake...")
roads_near_lakes = gpd.sjoin(roads, lake_buffer_union, how="inner", predicate="intersects")

print(f"✅ Found {len(roads_near_lakes)} roads within 100 ft of a lake.")

# --- Save result ---
roads_near_lakes.to_file(output_path)
print(f"✅ Saved to: {output_path}")

# --- Load into QGIS for immediate viewing ---
layer = QgsVectorLayer(output_path, "Roads Within 100ft of Lakes", "ogr")
if layer.isValid():
    QgsProject.instance().addMapLayer(layer)
    print("✅ Layer loaded into QGIS.")
else:
    print("❌ Failed to load output layer.")
