import matplotlib.pyplot as plt

import geopandas as gpd
from rasterio.crs import CRS
import rioxarray as rxr


from shapely.geometry import mapping

#Shapefile representing map
map_file = gpd.read_file(
    "D:/pansharpening_l8_s2/map.geojson")

#map_file.crs

##Represent our study area
aoi_path = ('D:/pansharpening_l8_s2/layers2/POLYGON.shp');
crop_extent = gpd.read_file(aoi_path)
crop_extent_wgs84 = crop_extent.to_crs(map_file.crs)
map_clip = gpd.clip(map_file, crop_extent_wgs84)
f, ax = plt.subplots(figsize=(10, 4))

crop_extent_wgs84.plot(ax=ax,
                       edgecolor="blue",
                       color="white")

map_clip.plot(ax=ax,
                color="grey")
ax.set(title="Plot of study area")
plt.show()

sentinel_path =("D:/pansharpening_l8_s2/sentinel2/L1C_T35TPF_A019481_20201128T090329/S2B_MSIL1C_20201128T090319_N0209_R007_T35TPF_20201128T100606.SAFE/GRANULE/L1C_T35TPF_A019481_20201128T090329/IMG_DATA/T35TPF_20201128T090319_B08.jp2")
sentinel = rxr.open_rasterio(sentinel_path,
                              masked=True).squeeze()

#sentinel.rio.crs


sentinel_wgs84 = sentinel.rio.reproject(map_clip.crs)
sentinel_wgs84.rio.crs

crs_wgs84 = CRS.from_string('EPSG:4326')

# Reproject the data using the crs object
sentinel_wgs84_2 = sentinel.rio.reproject(crs_wgs84)
sentinel_wgs84_2.rio.crs

f, ax = plt.subplots(figsize=(10, 5))
sentinel_wgs84_2.plot.imshow(ax=ax)

crop_extent_wgs84.plot(ax=ax,
                 alpha=.8)
ax.set(title="Raster Layer with Shapefile Overlayed")

ax.set_axis_off()
plt.show()

sentinel_clipped = sentinel_wgs84_2.rio.clip(crop_extent.geometry.apply(mapping),
                                      # This is needed if your GDF is in a diff CRS than the raster data
                                      crop_extent.crs)

f, ax = plt.subplots(figsize=(10, 4))
sentinel_clipped.plot(ax=ax)
ax.set(title="Raster Layer Cropped to Geodataframe Extent")
ax.set_axis_off()
plt.show()

path_to_tif_file = ("D:/pansharpening_l8_s2/sentinel_cropped.tif")
sentinel_clipped.rio.to_raster(path_to_tif_file)
clipped_chm = rxr.open_rasterio(path_to_tif_file)


f, ax = plt.subplots(figsize=(10, 4))
clipped_chm.plot(ax=ax,
                 cmap='Greys')
ax.set(title="Final Clipped Image")
ax.set_axis_off()
plt.show()
