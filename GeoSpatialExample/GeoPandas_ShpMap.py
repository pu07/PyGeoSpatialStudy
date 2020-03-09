#官方网站：https://geopandas.org/mapping.html
#数据结构与基本方法：https://geopandas.org/data_structures.html
#空间分析：https://geopandas.org/geometric_manipulations.html
#空间分析功能索引：https://geopandas.org/reference.html
# _*_ coding: cp936 _*_
# 导入geopandas
import geopandas,os
from geopandas import GeoSeries
import numpy as np
import matplotlib.pyplot as plt

#用来正常显示中文标签
#plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['figure.dpi'] = 200 #分辨率

#利用geopandas打开shp数据并绘图
def ShpMapWithLenged():
    #geopandas自带数据
    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    cities = geopandas.read_file(geopandas.datasets.get_path('naturalearth_cities'))
    #打印输出数据属性列
    print(world.head())
    #打印输出数据投影信息
    print(world.crs)
    # Plot by GDP per capta
    world = world[(world.pop_est>0) & (world.name!="Antarctica")]
    #计算人均GDP并赋值给gdp_per_cap
    world['gdp_per_cap'] = world.gdp_md_est / world.pop_est

    # Plot population estimates with an accurate legend
    fig, ax = plt.subplots(1, 1)

    #gdp_per_cap制图，有图例，图例在图下面水平摆放
    world.plot(column='gdp_per_cap', ax=ax, legend=True,legend_kwds={'label': "GDP per capita", 'orientation': "horizontal"})
    #Population by Country
    #world.plot(column='pop_est', ax=ax, legend=True,legend_kwds={'label': "Population by Country", 'orientation': "horizontal"})

    plt.show()

def ShpTwoLayersMap():
    #geopandas自带数据
    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    cities = geopandas.read_file(geopandas.datasets.get_path('naturalearth_cities'))
    #设置世界地图为底图，渲染颜色为黑色边框白色
    base = world.plot(color='white', edgecolor='black')
    #城市点地图显示参数设置，加载世界地底为底图，标记点大小为5，颜色为绿色
    cities.plot(ax=base, marker='o', color='green', markersize=5)
    plt.show()

#输入矢量数据
#半径
def ShpBuffer(strVectorFile,radius):
    #geopandas打开数据
    vector = geopandas.read_file(strVectorFile)
    #打印输出数据属性列
    print(vector.head())
    #打印输出数据投影信息
    #print(vector.crs)
    #打印输出数据投影信息中init:  一般为'ESPG:……'
    print(vector.crs['init'])
    #获取输入矢量数据的几何信息
    g = GeoSeries(vector['geometry'])

    print('----------------------buffer-------------------------------')
    #缓冲区分析，半径为函数的输入参数radius
    buffer=g.buffer(radius)
    #绘图的底图设置，黑色外框，白色内部
    base = buffer.plot(color='white',edgecolor='black')
    #原始输入的矢量文件制图，绿色
    vector.plot(ax=base, color='green')
    #上述两个图层统一制图，对比缓冲前后结果
    plt.show()

    #缓冲区数据设置缓冲后的几何信息
    vector_buffer = vector.set_geometry(buffer)
    print(vector_buffer.head())
    #给缓冲区后的矢量数据定义投影=输入矢量文件投影
    vector_buffer.crs=vector.crs['init']
    #获取文件名【不包含后缀名】
    shorFilename = strVectorFile.split('.')[0]
    #输出缓冲区后矢量文件名
    bufferVectorFile= shorFilename+"_buffer_"+str(radius)+"km.shp"
    #缓冲区文件输出指定文件夹
    vector_buffer.to_file(bufferVectorFile,'ESRI Shapefile')

#主函数
if __name__ == '__main__':

    #获取工程根目录的路径
    rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    #print('rootPath:'+rootPath)
    #数据文件路径
    dataPath = os.path.abspath(rootPath + r'\ShpData')
    #print('dataPath:'+dataPath)
    #切换目录
    os.chdir(dataPath)
    strVectorFile ="SpecialTown.shp"
    #获取工程根目录的路径
    #ShpMapWithLenged()

    #ShpTwoLayersMap()

    ShpBuffer(strVectorFile,1)