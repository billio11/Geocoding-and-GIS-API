
import geopandas as gpd
from shapely.geometry import Point

# Load catchment area data (GeoDataFrame)
catchment_areas = gpd.read_file('path/to/catchment_areas.shp')

# Create a GeoDataFrame from the list of addresses
addresses = gpd.GeoDataFrame(geometry=gpd.points_from_xy([longitude_list], [latitude_list]))

# Perform spatial join
joined_data = gpd.sjoin(addresses, catchment_areas, how="left", op="within")

# The 'index_right' column will contain the catchment area index for each address
print(joined_data[['Address', 'index_right']])
