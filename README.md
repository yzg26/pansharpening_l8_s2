# pansharpening_l8_s2
landsat8-sentinel2 pansharpening

Landsat8 ve Sentinel2 görüntülerinin pansharp'ı için Landsat8 uydu görüntüsünün Blue,Red,Green,NIR bandı, Sentinel2 görüntüsünün NIR bandı kullanılmıştır.
Shapefile ve geojson kullanılarak görüntüler crop edilmiştir. Landsat8'in B,G,R,NIR bantları birleştirilmiştir. Birleşen ve crop edilen görüntüler birkaç yöntemle pansharp
edilmiştir. Kodların çalışma sırası "sentinel_crop.py", "mergebands.py", "landsatcrop.py", "pansharpening_l8_s2" şeklindedir.
