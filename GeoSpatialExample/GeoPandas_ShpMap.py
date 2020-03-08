# _*_ coding: utf-8 _*_
# 导入geopandas
import geopandas,os
import numpy as np
import matplotlib.pyplot as plt

#用来正常显示中文标签
#plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['figure.dpi'] = 200 #分辨率

#利用geopandas打开shp数据并绘图
def ShpMap():
    #geopandas自带数据
    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    print(world.head())
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




#主函数
if __name__ == '__main__':

    #获取工程根目录的路径
    ShpMap()