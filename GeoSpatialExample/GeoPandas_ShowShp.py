# _*_ coding: utf-8 _*_
# 导入geopandas
import geopandas,os
import matplotlib.pyplot as plt

#用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['figure.dpi'] = 200 #分辨率

#利用geopandas打开shp数据并绘图
def showShp(shpfilename):
    #创建空间数据
    gdf = geopandas.GeoDataFrame

    #读取SHP文件
    shp = gdf.from_file(shpfilename, encoding='gb18030')

    print(shp.head())  #输出属性表
    #Shp文件绘图
    shp.plot()
    #plt.axis('off') # 不显示坐标轴
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

    #SHP文件路径
    strVectorFile ="TestPolygon.shp"
    showShp(strVectorFile)