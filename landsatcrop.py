import geopandas as gpd
from rasterio.crs import CRS
import rioxarray as rxr

from shapely.geometry import mapping


#Shapefile representing map
map_file = gpd.read_file(
    "D:/pansharp_data/map.geojson")
#map_file.crs


#Represent our study area
aoi_path = ('D:/pansharp_data/layers2/POLYGON.shp');
crop_extent = gpd.read_file(aoi_path)
crop_extent_wgs84 = crop_extent.to_crs(map_file.crs)
map_clip = gpd.clip(map_file, crop_extent_wgs84)


landsat_path =("D:/pansharpening_l8_s2/stacked_landsat8.tif")
landsat = rxr.open_rasterio(landsat_path,
                              masked=True).squeeze()

#landsat.rio.crs


landsat_wgs84 = landsat.rio.reproject(map_clip.crs)
landsat_wgs84.rio.crs

crs_wgs84 = CRS.from_string('EPSG:4326')

# Reproject the data using the crs object
landsat_wgs84_2 = landsat.rio.reproject(crs_wgs84)
landsat_wgs84_2.rio.crs



landsat_clipped = landsat_wgs84_2.rio.clip(crop_extent.geometry.apply(mapping),
                                      # This is needed if your GDF is in a diff CRS than the raster data
                                      crop_extent.crs)


path_to_tif_file = ("D:/pansharpening_l8_s2/landsat_cropped.tif")
landsat_clipped.rio.to_raster(path_to_tif_file)
clipped_chm = rxr.open_rasterio(path_to_tif_file)