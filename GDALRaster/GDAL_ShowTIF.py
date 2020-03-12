# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from osgeo import gdal
import os
import numpy as np
import pandas as pd
from GDALRaster.GDAL_OpenTIF import read_img

#用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False# 显示负号
plt.rcParams['figure.dpi'] = 200 #分辨率
# 默认的像素：[6.0,4.0]，分辨率为100，图片尺寸为 600&400
# 指定dpi=200，图片尺寸为 1200*800
# 指定dpi=300，图片尺寸为 1800*1200
# 设置figsize可以在不改变分辨率情况下改变比例

#显示灰度图
def showGreyTIFF(RasterData):
    #将图片转为数组
    image = RasterData.ReadAsArray()
    # 加载灰度图，可以添加 cmap 参数解决
    plt.imshow(image, cmap='Greys_r')
    plt.colorbar()
    plt.axis('off') # 不显示坐标轴
    #窗口中展示灰度图
    plt.show()

#显示简单数组
def showShortTIFF():
    a=np.arange(18).reshape(6,3)
    print(a)

    b=a[[0,1,2]]
    print(b)

    #定义图片框
    plt.figure()
    # 将画板分为1行两列，本幅图位于第一个位置
    plt.subplot(1,2,1)
    plt.title("彩色图片")
    #图片显示原始图像
    plt.imshow(a)
    plt.colorbar()
    # 将画板分为1行两列，本幅图位于第3个位置
    plt.subplot(1,2,2)
    plt.title("灰度图")
    # 加载灰度图，可以添加 cmap 参数解决
    plt.imshow(a, cmap='Greys_r')
    plt.colorbar()

    plt.show()

#显示部分图片
def showShortImage():
    #打开指定图片
    a = plt.imread('xinghuaduotian.jpg')
    print(a.shape)

    plt.title("彩色图片")
    b=a[[0,1,2]]
    print('----------b----------')
    print(b.shape)
    c=b[:,[0,1,2]]
    print('----------c----------')
    print(c.shape)
    #图片显示原始图像
    #plt.imshow(b)
    #定义图片框
    plt.figure()
    #将画板分为1行两列，本幅图位于第一个位置
    plt.subplot(1,2,1)
    plt.title("彩色图片")
    #图片显示原始图像
    plt.imshow(a)
    #plt.colorbar(shrink=0.75)
    # 将画板分为1行两列，本幅图位于第3个位置
    plt.subplot(1,2,2)
    plt.title("灰度图")
    im_r = a[:, :, 0]  # 单通道
    print('------------------单通道------------------------')
    print(im_r.shape)
    # 加载灰度图，可以添加 cmap 参数解决
    plt.imshow(im_r, cmap='Greys_r')
    #plt.colorbar(shrink=0.75)

    plt.show()


#显示彩色图
def showColorTIFF(RasterData):

    image_data = RasterData.ReadAsArray()
    #获取影像的第一波段
    band1 = RasterData.GetRasterBand(1)
    band2 = RasterData.GetRasterBand(2)
    band3 = RasterData.GetRasterBand(3)
    #判断栅格数据的数据类型
    if 'int8' in image_data.dtype.name:
        datatype = gdal.GDT_Byte
    elif 'int16' in image_data.dtype.name:
        datatype = gdal.GDT_UInt16
    else:
        datatype = gdal.GDT_Float32
    bands = np.array((band1,band2,band3))
    # 加载灰度图，可以添加 cmap 参数解决
    plt.imshow(bands)
    #plt.colorbar()
    plt.axis('off') # 不显示坐标轴
    #窗口中展示图
    plt.show()

#并排显示单波段图片
def ListShowTIFF(RasterData):
    #将指定图片转为数组
    image = RasterData.ReadAsArray()
    #定义图片框
    plt.figure()
    # 将画板分为1行两列，本幅图位于第一个位置
    plt.subplot(2,2,1)
    plt.title("彩色图片")

    #图片显示原始图像
    plt.imshow(image)
    plt.colorbar()
    # 将画板分为1行两列，本幅图位于第3个位置
    plt.subplot(2,2,2)
    plt.title("灰度图")

    # 加载灰度图，可以添加 cmap 参数解决
    plt.imshow(image, cmap='Greys_r')
    plt.colorbar()

    plt.subplot(2,2,3)
    plt.title("直方图")

    plt.hist(image, facecolor='g',edgecolor='b')
    plt.legend()

    #窗口中展示图片
    plt.show()

#直方图统计
def ShowTIFFHist(RasterData):
    #将指定图片转为数组
    image = RasterData.ReadAsArray()
    plt.title("Histogram")
    plt.hist(image, facecolor='g',
             edgecolor='b',alpha=0.7)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    #plt.legend()
    #窗口中展示图片
    plt.show()

#直方图统计
def ShowTIFFBoxplot(RasterData):
    #将指定图片转为数组
    image = RasterData.ReadAsArray()
    df = pd.DataFrame(image)
    print('-------------describe-----------------')
    print(df.describe())

    df.plot.box(title="Box Plot")
    plt.grid(linestyle="--", alpha=0.8)
    plt.show()

#显示遥感影像的所有单波段灰度图像
def showMultiBandTIFFGray(RasterData):
    #打开指定图片
    #image = RasterData.ReadAsArray()
    #定义图片框
    plt.figure()
    #获取波段数量
    num_bands= RasterData.ReadAsArray().shape[0]
    print('波段数为：'+str(num_bands))
    for index in range(num_bands):
        print(index+1)
        #获取各波段数据，索引是从0开始，0-3，而波段是从1开始，1-4，因此需要给index+1，否则GetRasterBand(0)会出错
        band = RasterData.GetRasterBand(index+1)
        #转数组
        band_data=band.ReadAsArray()
        # 将画板分为1行多列，各波段从左到右依次排列
        plt.subplot(1,num_bands,index+1)
        #图片标题
        plt.title("band"+str(index+1))
        #图片显示原始图像
        plt.imshow(band_data, cmap='Greys_r')
        plt.axis('off') # 不显示坐标轴
    #plt.colorbar(shrink=0.5)
    #窗口中展示图片
    plt.show()

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
    imagepath ='S2_20190727San_234.tif'

    #引入OpenTIF中的图像读取方法读图像数据
    data = read_img(imagepath)
    #showColorTIFF(data)
    #showGreyTIFF(band1)
    #显示图像
    showMultiBandTIFFGray(data)
    #showTIFF(data)
    #showShortTIFF()
    #showShortImage()