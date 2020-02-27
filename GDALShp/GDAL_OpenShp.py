# -*- coding: utf-8 -*-
try:
    from osgeo import gdal
    from osgeo import ogr
except ImportError:
    import gdal
    import ogr

def ReadVectorFile():
    # 为了支持中文路径，请添加下面这句代码
    gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8", "NO")
    # 为了使属性表字段支持中文，请添加下面这句
    gdal.SetConfigOption("SHAPE_ENCODING", "GB2312")
    #SHP文件路径
    strVectorFile = "D:\\tmpdata\\boundary\\ChinaProvince\\ChinaProvince.shp"
    # 注册所有的驱动
    ogr.RegisterAll()
    # 打开数据
    ds = ogr.Open(strVectorFile, 0)
    #判断文件是否存在
    if ds == None:
        print("打开文件【%s】失败！", strVectorFile)
        return
    #提示打开成功
    print("打开文件【%s】成功！", strVectorFile)
#调用测试函数
ReadVectorFile()