# -*- coding: utf-8 -*-
import numpy as np
import gdal
import os
from GDALRaster.GDAL_OpenTIF import read_img
from GDALRaster.GDAL_ShowTIF import showTIFF,showGreyTIFF,showMultiBandTIFFGray

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

#获取影像的所有波段并写入文件夹
def GetBandFromTIF(path,filename):
    #切换路径到待处理图像所在文件夹
    os.chdir(path)
    #读数据并获取影像信息
    data = read_img(filename)
    #获取文件名【不包含后缀名】
    shorFilename = filename.split('.')[0]
    #获取波段数量
    num_bands= data.ReadAsArray().shape[0]
    print('波段数为：'+str(num_bands))
    for index in range(num_bands):
        print(index+1)
        #获取各波段数据，索引是从0开始，0-3，而波段是从1开始，1-4，因此需要给index+1，否则GetRasterBand(0)会出错
        band = data.GetRasterBand(index+1)
        #转数组
        band_data=band.ReadAsArray()
        #输出的NDVI文件名
        outputname= shorFilename+"_band"+str(index+1)+".tif"
        print('outputname:'+outputname)
        #调用栅格输出函数，输出NDVI，并指定为GTiff格式
        writeimage(data,outputname,band_data,"GTiff")
        #显示各波段灰度图片
    showMultiBandTIFFGray(data)

#主函数
if __name__ == '__main__':
    #获取工程根目录的路径
    rootPath = os.path.abspath(os.path.dirname(__file__))
    #print('rootPath:'+rootPath)
    #数据文件路径
    dataPath = os.path.abspath(rootPath + r'\data')
    #print('dataPath:'+dataPath)
    #切换目录
    os.chdir(dataPath)
    #测试影像数据
    filename ='S2_20190727San.tif'
    #调用函数
    GetBandFromTIF(dataPath,filename)

