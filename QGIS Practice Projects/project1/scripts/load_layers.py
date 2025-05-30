from qgis.core import QgsVectorLayer, QgsProject
import os

# Base folder that holds the subfolders
base_folder = r"C:\Users\JohnKenny\OneDrive - Pathway to Adventure Council\Desktop\qgis\project1\data"

# Map of display names to their subfolder and shapefile name
layers = {
    "Lakes (areawater)": ("tl_2024_17097_areawater", "tl_2024_17097_areawater.shp"),
    "Roads": ("tl_2024_17097_roads", "tl_2024_17097_roads.shp"),
    "Streams": ("IL_Streams_From_100K_DLG_Ln", "IL_Streams_From_100K_DLG_Ln.shp")
}

# Loop through each item and attempt to load
for label, (subfolder, filename) in layers.items():
    path = os.path.join(base_folder, subfolder, filename)
    layer = QgsVectorLayer(path, label, "ogr")

    if not layer.isValid():
        print(f"❌ Failed to load: {label} — Checked path: {path}")
    else:
        QgsProject.instance().addMapLayer(layer)
        print(f"✅ Loaded: {label}")
