#官方网站：https://geopandas.org/mapping.html
#数据结构与基本方法：https://geopandas.org/data_structures.html
#空间分析：https://geopandas.org/geometric_manipulations.html
#空间分析功能索引：https://geopandas.org/reference.html
# _*_ coding: cp936 _*_
# 导入geopandas
import geopandas,os
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
    ShpTwoLayersMap()
