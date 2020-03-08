#-*- coding: cp936 -*-
import os
try:
    from osgeo import gdal
    from osgeo import ogr
    from osgeo import osr
except ImportError:
    import gdal
    import ogr


def shpBuffer(strVectorFile,bufferVectorFile,layername):
    #-----------------------------GDAL驱动注册-------------
    # 为了支持中文路径，请添加下面这句代码
    gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8","NO")
    # 为了使属性表字段支持中文，请添加下面这句
    gdal.SetConfigOption("SHAPE_ENCODING","GB2312")
    # 注册所有的驱动
    ogr.RegisterAll()
    # 创建数据，这里以创建ESRI的shp文件为例
    strDriverName = "ESRI Shapefile"
    oDriver =ogr.GetDriverByName(strDriverName)
    if oDriver == None:
        print("%s 驱动不可用！\n", strDriverName)
        return
    #------------------------------------------------------

    #------------------------打开数据----------------------
    ds = ogr.Open(strVectorFile, 0)
    #判断文件是否存在
    if ds == None:
        print("打开文件【%s】失败！", strVectorFile)
        return
    #提示打开成功
    print("打开文件【%s】成功！", strVectorFile)
    #------------------------------------------------------

    #-----------------获取指定图层-------------------------
    oLayer = ds.GetLayer('SpecialTown')
    if oLayer == None:
        print("获取第%d个图层失败！\n", 0)
        return
    #图层对象
    oDefn = oLayer.GetLayerDefn()
    #------------------------------------------------------

    #------------------# 创建缓冲区数据源和图层---------------------
    # 创建缓冲区文件数据源
    bufferDS =oDriver.CreateDataSource(bufferVectorFile)
    if bufferDS == None:
        print("创建文件【%s】失败！", bufferVectorFile)
        return
    #获取输入数据的投影信息
    targetSR =oLayer.GetSpatialRef()
    papszLCO = []
    #创建缓冲图层
    bufferLayer =bufferDS.CreateLayer(layername, targetSR, ogr.wkbPolygon, papszLCO)
    if bufferLayer == None:
        print("图层创建失败！\n")
        return
    #获取缓冲区图层的要素
    buff_feat  = ogr.Feature(bufferLayer.GetLayerDefn())
    #------------------------------------------------------------

    #遍历图层中的要素
    oLayer.ResetReading()
    for feat in oLayer:
        #遍历每一个要素并建立1KM的缓冲区
        buff_geom = feat.geometry().Buffer(1000)
        #定义缓冲区输出数据源要素的几何信息为缓冲区后的信息
        bufferDS = buff_feat.SetGeometry(buff_geom)
        #给输出数据源创建图层，将缓冲后的要素赋值给图层
        bufferDS = bufferLayer.CreateFeature(buff_feat)



    bufferDS.Destroy()
    print("缓冲区文件创建完成！\n")






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
    strVectorFile =r"SpecialTown.shp"
    bufferVectorFile=r"SpecialTown_buffer.shp"
    layername='SpecialTown_buffer'
    shpBuffer(strVectorFile,bufferVectorFile,layername)