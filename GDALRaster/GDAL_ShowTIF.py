# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

#用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['figure.dpi'] = 300 #分辨率
# 默认的像素：[6.0,4.0]，分辨率为100，图片尺寸为 600&400
# 指定dpi=200，图片尺寸为 1200*800
# 指定dpi=300，图片尺寸为 1800*1200
# 设置figsize可以在不改变分辨率情况下改变比例

#显示灰度图
def showGreyTIFF(RasterData):
    #打开指定图片
    image = RasterData.ReadAsArray()
    # 加载灰度图，可以添加 cmap 参数解决
    plt.imshow(image, cmap='Greys_r')
    plt.axis('off') # 不显示坐标轴
    #窗口中展示灰度图
    plt.show()

#显示多个图片
def showTIFF(RasterData):
    #打开指定图片
    image = RasterData.ReadAsArray()
    #定义图片框
    plt.figure()
    # 将画板分为1行两列，本幅图位于第一个位置
    plt.subplot(1,2,1)
    plt.title("彩色图片")
    #图片显示原始图像
    plt.imshow(image)
    # 将画板分为1行两列，本幅图位于第3个位置
    plt.subplot(1,2,2)
    plt.title("灰度图")
    # 加载灰度图，可以添加 cmap 参数解决
    plt.imshow(image, cmap='Greys_r')
    #窗口中展示图片
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
    #窗口中展示图片
    plt.show()
