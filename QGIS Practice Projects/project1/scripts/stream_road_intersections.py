import geopandas as gpd
import os
from qgis.core import QgsVectorLayer, QgsProject

# --- File paths ---
data_base = r"C:\Users\JohnKenny\OneDrive - Pathway to Adventure Council\Desktop\qgis\project1\data"
output_base = r"C:\Users\JohnKenny\OneDrive - Pathway to Adventure Council\Desktop\qgis\project1\outputs"

streams_path = os.path.join(data_base, "IL_Streams_From_100K_DLG_Ln", "IL_Streams_From_100K_DLG_Ln.shp")
roads_path = os.path.join(data_base, "tl_2024_17097_roads", "tl_2024_17097_roads.shp")

intersection_output = os.path.join(output_base, "stream_road_intersections.shp")
centroid_output = os.path.join(output_base, "stream_road_intersections_points.shp")

# --- Load and project layers ---
streams = gpd.read_file(streams_path).to_crs(epsg=3435)
roads = gpd.read_file(roads_path).to_crs(epsg=3435)

# --- Spatial intersection ---
print("Finding intersections between streams and roads...")
intersections = gpd.overlay(roads, streams, how="intersection")
print(f"✅ Found {len(intersections)} intersection features.")

# --- Save the raw intersection geometries ---
intersections.to_file(intersection_output)
print(f"✅ Saved intersection geometries to: {intersection_output}")

# --- Convert to centroid points ---
intersections_centroids = intersections.copy()
intersections_centroids["geometry"] = intersections_centroids.centroid

# Save centroids
intersections_centroids.to_file(centroid_output)
print(f"✅ Saved centroids to: {centroid_output}")

# --- Load the centroid layer into QGIS ---
points_layer = QgsVectorLayer(centroid_output, "Stream–Road Crossings (Points)", "ogr")
if points_layer.isValid():
    QgsProject.instance().addMapLayer(points_layer)
    print("✅ Point layer loaded into QGIS.")
else:
    print("❌ Failed to load centroid layer.")
