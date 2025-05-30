# QGIS Script to Load Three Counties Lakes Data
# Run this in the QGIS Python Console or save as a .py file

from qgis.core import QgsVectorLayer, QgsProject
import os

# Define the file paths
file_paths = [
    r"Z:\johnv\GIS-learning\QGIS Practice Projects\project1\data\cook_county_lakes\tl_2024_17031_areawater.shp",
    r"Z:\johnv\GIS-learning\QGIS Practice Projects\project1\data\dupage_county_lakes\tl_2024_17043_areawater.shp",
    r"Z:\johnv\GIS-learning\QGIS Practice Projects\project1\data\lake_county_lakes\tl_2024_17097_areawater.shp",
    r"Z:\johnv\GIS-learning\QGIS Practice Projects\project1\data\mchenry_county_lakes\tl_2024_17111_areawater.shp"
]

# Define layer names (more readable than file paths)
layer_names = [
    "Cook County Lakes",
    "DuPage County Lakes", 
    "Lake County Lakes",
    "McHenry County Lakes"
]

# Load each shapefile
for i, file_path in enumerate(file_paths):
    # Check if file exists
    if os.path.exists(file_path):
        # Create vector layer
        layer = QgsVectorLayer(file_path, layer_names[i], "ogr")
        
        # Check if layer is valid
        if layer.isValid():
            # Add layer to project
            QgsProject.instance().addMapLayer(layer)
            print(f"Successfully loaded: {layer_names[i]}")
        else:
            print(f"Failed to load layer: {layer_names[i]}")
            print(f"Invalid layer from file: {file_path}")
    else:
        print(f"File not found: {file_path}")

print("Script completed!")