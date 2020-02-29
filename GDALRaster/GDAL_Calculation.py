import numpy as np
import gdal
import os
import matplotlib.pyplot as plt
from GDALRaster.GDAL_OpenTIF import read_img
from GDALRaster.GDAL_WriteTIF import writeimage
import GDALRaster.GDAL_ShowTIF as showTIF

#计算NDVI
#data原始影像
#outputname输出NDVI文件名
def NDVI_Calculation(rasterdata,outputname):
    #将栅格数据转为数组并定义为数据类型为float
    data = rasterdata.ReadAsArray().astype(np.float)
    #也可以用波段获取方式，这样更清楚
    #band1 = dataset.GetRasterBand(1)
    #由于数组是从0开始计数，因此波段名称为0，1，2，3；3为近红外波段；2为红波段
    ndvi = (data[3]-data[2])/(data[3]+data[2])
    #调用栅格输出函数，输出NDVI，并指定为GTiff格式
    writeimage(rasterdata,outputname,ndvi,"GTiff")
    print(outputname+'已OK')

#--------------------测试NDVI计算并输出栅格-------------------
#切换路径到待处理图像所在文件夹
os.chdir(r'D:\tmpdata\threelakefarm')
#读数据并获取影像信息
data = read_img('S2_20190727San.tif')

outputname= "S2_20190727San_NDVI.tif"
#调用NDVI计算函数
#NDVI_Calculation(data,outputname)

#读数据并获取影像信息
NDVI_data = read_img(outputname)
#窗口显示
showTIF.showGreyTIFF(NDVI_data)
showTIF.showTIFFbyCV2(NDVI_data)