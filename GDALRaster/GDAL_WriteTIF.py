import numpy as np
import gdal
import os

def writeimage(filename,dst_filename,data):
    #filename用于获取坐标信息，dst_filename目标文件格式为ENVI格式，data为要写出的数据，
    dataset=gdal.Open(filename)
    projinfo=dataset.GetProjection()
    geotransform = dataset.GetGeoTransform()
    format = "GTiff"
    driver = gdal.GetDriverByName( format )
    dst_ds = driver.Create( dst_filename,dataset.RasterXSize, dataset.RasterYSize,1, gdal.GDT_Float32 )
    dst_ds.SetGeoTransform(geotransform )
    dst_ds.SetProjection( projinfo )
    dst_ds.GetRasterBand(1).WriteArray(data)
    dst_ds = None

#计算NDVI
# import numpy as np
# data = data.astype(np.float)
# ndvi = (data[3]-data[2])/(data[3]+data[2])             #3为近红外波段；2为红波段
# run.write_img('LC81230402013164LGN00_ndvi.tif',proj,geotrans,ndvi) #写为ndvi图像