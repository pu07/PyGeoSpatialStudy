import matplotlib.pyplot as plt
import numpy as np
import cv2

def showGreyTIFF(RasterData):
    #打开指定图片
    image = RasterData.ReadAsArray()

    # 加载灰度图，可以添加 cmap 参数解决
    plt.imshow(image, cmap='Greys_r')
    plt.axis('off') # 不显示坐标轴
    #窗口中展示灰度图
    plt.show()

def showTIFF(RasterData):
    #打开指定图片
    image = RasterData.ReadAsArray()
    #指定图片中的红波段
    #im_r = image[:, :, 0]  # 红色通道
    #图片显示红波段
    #plt.imshow(image, cmap='gist_earth')
    plt.imshow(image)
    #窗口中展示图片
    plt.show()

def Bandcompose(InputData):
    band1 = InputData.GetRasterBand(1)
    band1_data=band1.ReadAsArray()
    band2 = InputData.GetRasterBand(2)
    band2_data=band2.ReadAsArray()
    band3 = InputData.GetRasterBand(3)
    band3_data=band3.ReadAsArray()
    band4 = InputData.GetRasterBand(4)
    band4_data=band4.ReadAsArray()
    OutputData = cv2.merge([band4_data,band3_data,band2_data])
    return OutputData


def showTIFFbyCV2(RasterData):
    #打开指定图片
    image = RasterData.ReadAsArray()
    cv2.imshow('image',image)
    cv2.waitKey()
    cv2.destroyAllWindows()