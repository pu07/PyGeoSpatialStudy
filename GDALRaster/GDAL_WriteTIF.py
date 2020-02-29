import numpy as np
import gdal
import os
from GDALRaster.GDAL_OpenTIF import read_img
from GDALRaster.GDAL_ShowTIF import showTIFF,showGreyTIFF

#输出栅格函数，指定格式为GTiff
#InputData用于获取坐标、投影等信息；
# output_filename目标文件格式为GTiff格式;
# OutPutData为要写出的数据，
#format为输出格式
def writeimage(InputData,output_filename,OutPutData,format):
    #获取栅格投影信息
    projinfo=InputData.GetProjection()
    ##获取栅格仿射转换信息
    geotransform = InputData.GetGeoTransform()
    #栅格列数
    Raster_XSize = InputData.RasterXSize
    #栅格行数
    Raster_YSize = InputData.RasterYSize
    #定义输出格式
    #format = "GTiff"
    #输出格式驱动参数
    driver = gdal.GetDriverByName(format)
    #创新输出栅格驱动并赋值相关参数
    dst_ds = driver.Create(output_filename,Raster_XSize, Raster_YSize,1, gdal.GDT_Float32 )
    #定义输出栅格的仿射转换信息
    dst_ds.SetGeoTransform(geotransform)
    #定义输出栅格投影信息
    dst_ds.SetProjection(projinfo)
    #执行输出栅格
    dst_ds.GetRasterBand(1).WriteArray(OutPutData)
    #清除缓存
    dst_ds = None

#切换路径到待处理图像所在文件夹
os.chdir(r'D:\tmpdata\threelakefarm')
#读数据并获取影像信息
data = read_img('S2_20190727San.tif')
#获取波段1数据
band2 = data.GetRasterBand(2)
showGreyTIFF(band2)
#转数组
band2_data=band2.ReadAsArray()
#输出的NDVI文件名
outputname= "S2_20190727San_band2.tif"
#调用栅格输出函数，输出NDVI，并指定为GTiff格式
writeimage(data,outputname,band2_data,"GTiff")

