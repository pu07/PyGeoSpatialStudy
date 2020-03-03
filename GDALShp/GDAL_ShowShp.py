# _*_ coding: utf-8 _*_
# 导入geopandas
import geopandas
import matplotlib.pyplot as plt

#用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['figure.dpi'] = 200 #分辨率

#利用geopandas打开shp数据并绘图
def showShp(shpfilename):
    #创建空间数据
    gdf = geopandas.GeoDataFrame
    #读取SHP文件
    shp = gdf.from_file(shpfilename)
    #Shp文件绘图
    shp.plot()
    plt.axis('off') # 不显示坐标轴
    plt.show()


#SHP文件路径
strVectorFile ="D:\\GitHub\PyGdalStudy\\GDALShp\\Data\\TestPolygon.shp"
#showShp(strVectorFile)