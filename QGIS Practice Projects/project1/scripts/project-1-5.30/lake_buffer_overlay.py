import os
import geopandas as gpd
from shapely.ops import unary_union
import matplotlib.pyplot as plt

# --- FILE PATHS ---
lake_path = r"C:\Users\JohnKenny\OneDrive - Pathway to Adventure Council\Desktop\qgis\project1\data\tl_2024_17097_areawater\tl_2024_17097_areawater.shp"
roads_path = r"C:\Users\JohnKenny\OneDrive - Pathway to Adventure Council\Desktop\qgis\project1\data\tl_2024_17097_roads\tl_2024_17097_roads.shp"
output_dir = r"C:\Users\JohnKenny\OneDrive - Pathway to Adventure Council\Desktop\qgis\project1\outputs"
output_file = os.path.join(output_dir, "lake_buffer_100ft.shp")

# --- BUFFER DISTANCE ---
buffer_distance_m = 30.5  # 100 ft in meters

# --- ENSURE OUTPUT FOLDER EXISTS ---
os.makedirs(output_dir, exist_ok=True)

# --- LOAD AND REPROJECT LAKES ---
lakes = gpd.read_file(lake_path)
lakes = lakes.to_crs(epsg=3435)  # Illinois State Plane East (ft/m)

# --- CREATE BUFFER ---
lake_buffer = lakes.buffer(buffer_distance_m)
buffer_union = unary_union(lake_buffer)
buffer_gdf = gpd.GeoDataFrame(geometry=[buffer_union], crs=lakes.crs)

# --- SAVE BUFFER ---
buffer_gdf.to_file(output_file)
print(f"Lake buffer saved to: {output_file}")

# --- LOAD ROADS ---
roads = gpd.read_file(roads_path).to_crs(epsg=3435)

# --- PLOT RESULTS ---
fig, ax = plt.subplots(figsize=(12, 12))
roads.plot(ax=ax, color="gray", linewidth=0.5, label="Roads")
lakes.plot(ax=ax, color="lightblue", alpha=0.6, edgecolor="blue", label="Lakes")
buffer_gdf.plot(ax=ax, color="red", alpha=0.3, label="Lake 100ft Buffer")

plt.title("Lakes and 100 ft Buffer (McHenry County)")
plt.legend()
plt.tight_layout()
plt.savefig(os.pa
