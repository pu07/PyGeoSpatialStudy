#官方网站：https://geopandas.org/mapping.html
#数据结构与基本方法：https://geopandas.org/data_structures.html
#空间分析：https://geopandas.org/geometric_manipulations.html
#空间分析功能索引：https://geopandas.org/reference.html
# _*_ coding: utf-8 _*_
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
    print(world.head())
    print(world.crs)
    # Plot by GDP per capta
    world = world[(world.pop_est>0) & (world.name!="Antarctica")]
    world['gdp_per_cap'] = world.gdp_md_est / world.pop_est

    # Plot population estimates with an accurate legend
    fig, ax = plt.subplots(1, 1)
    #divider = make_axes_locatable(ax)
    #cax = divider.append_axes("right", size="5%", pad=0.1)#pad为图例和主图的距离，size为图例的宽度

    #gdp_per_cap
    world.plot(column='gdp_per_cap', ax=ax, legend=True,legend_kwds={'label': "GDP per capita", 'orientation': "horizontal"})
    #Population by Country
    #world.plot(column='pop_est', ax=ax, legend=True,legend_kwds={'label': "Population by Country", 'orientation': "horizontal"})

    plt.show()

def ShpTwoLayersMap():
    #geopandas自带数据
    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    cities = geopandas.read_file(geopandas.datasets.get_path('naturalearth_cities'))
    base = world.plot(color='white', edgecolor='black')
    cities.plot(ax=base, marker='o', color='green', markersize=5)
    plt.show()

def ShpBuffer():
    #geopandas自带数据
    cities = geopandas.read_file(geopandas.datasets.get_path('naturalearth_cities'))
    print(cities.head())
    print(cities.crs)
    print(cities.crs['init'])
    g = GeoSeries(cities['geometry'])

    print('----------------------buffer-------------------------------')
    buffer=g.buffer(5)
    base = buffer.plot( color='white',edgecolor='black')
    cities.plot(ax=base, marker='o',color='green', markersize=5)
    plt.show()

    #缓冲区数据设置缓冲后的几何信息
    citys_buffer = cities.set_geometry(buffer)
    print(citys_buffer.head())
    citys_buffer.crs=cities.crs['init']
    filename = r'D:\GitHub\PyGeoSpatialStudy\ShpData\citys_buffer.shp'
    citys_buffer.to_file(filename,'ESRI Shapefile')

#主函数
if __name__ == '__main__':

    #获取工程根目录的路径
    #ShpMapWithLenged()

    #ShpTwoLayersMap()

    ShpBuffer()