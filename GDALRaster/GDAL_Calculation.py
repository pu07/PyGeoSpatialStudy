# -*- coding: utf-8 -*-
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
def NDVI_Calculation(imagepath):

    #引入OpenTIF中的图像读取方法读图像数据
    rasterdata = read_img(imagepath)
    #获取文件名【不包含后缀名】
    shorFilename = imagepath.split('.')[0]
    #将栅格数据转为数组并定义为数据类型为float
    data = rasterdata.ReadAsArray().astype(np.float)
    #由于数组是从0开始计数，因此波段名称为0，1，2，3；3为近红外波段；2为红波段
    ndvi = (data[3]-data[2])/(data[3]+data[2])
    #输出的NDVI文件名
    outputname= shorFilename+"_NDVI.tif"
    print('outputname:'+outputname)
    #调用栅格输出函数，输出NDVI，并指定为GTiff格式
    writeimage(rasterdata,outputname,ndvi,"GTiff")
    print(outputname+'已OK')
    NDVI_data = read_img(outputname)
    #窗口显示
    showTIF.showTIFF(NDVI_data)

#--------------------测试NDVI计算并输出栅格-------------------
#主函数
if __name__ == '__main__':
    #获取工程根目录的路径
    rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    #print('rootPath:'+rootPath)
    #数据文件路径
    dataPath = os.path.abspath(rootPath + r'\RasterData')
    #print('dataPath:'+dataPath)
    #切换目录
    os.chdir(dataPath)
    #测试影像数据
    imagepath ='S2_20190727San.tif'
    #调用NDVI计算方法
    NDVI_Calculation(imagepath)