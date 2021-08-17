import rasterio

#Landsat8 Blue-Green-Red-NIR Bands
b2 = 'D:/pansharpening_l8_s2/landsat8/LC08_L1TP_180031_20190325_20200829_02_T1_B2.tif' 
b3 = 'D:/pansharpening_l8_s2/landsat8/LC08_L1TP_180031_20190325_20200829_02_T1_B3.tif' 
b4 = 'D:/pansharpening_l8_s2/landsat8/LC08_L1TP_180031_20190325_20200829_02_T1_B4.tif' 
b5 = 'D:/pansharpening_l8_s2/landsat8/LC08_L1TP_180031_20190325_20200829_02_T1_B5.tif' 

file_list = [b2, b3, b4, b5]

stacked_path = 'D:/pansharpening_l8_s2/stacked_landsat8.tif' #Path of new stacked file

# Read metadata of first file
with rasterio.open(file_list[0]) as src0:
    meta = src0.meta

# Update meta to reflect the number of layers
meta.update(count = len(file_list))

# Read each layer and write it to stack
with rasterio.open(stacked_path, 'w', **meta) as dst:
    for id, layer in enumerate(file_list, start=1):
        with rasterio.open(layer) as src1:
            dst.write_band(id, src1.read(1))
raster = rasterio.open(stacked_path)
#raster.crs
raster_arr = raster.read()
print(raster_arr.shape)
