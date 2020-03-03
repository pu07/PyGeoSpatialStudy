#-*- coding: cp936 -*-
#导入相关库包
import osgeo,gdal,os,ogr,osr
import pandas as pd
from GDALShp.GDAL_ShowShp import showShp

#读取Excel表格数据
def readExcelbyFileNameAndSheetName(filename,sheetname):
    #可以通过sheet_name来指定读取的表单
    df=pd.read_excel(filename,sheet_name=sheetname)
    columns = df.columns.values
    print("输出列标题",columns)
    data=df.values#读取全部数据
    print("获取到所有的值:\n{0}".format(data))#格式化输出
    return columns,data


#path，EXCEL文件目录；ExcelName，EXCEL文件名；shpfilename，输出的shp文件名
#Lng_columns_num，经度所在列数；Lat_columns_num纬度所在列数
def Excel2Shp(path,ExcelName,shpfilename,Lng_columns_num,Lat_columns_num):
    # 为了支持中文路径，请添加下面这句代码
    gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8","NO")
    # 为了使属性表字段支持中文，请添加下面这句
    gdal.SetConfigOption("SHAPE_ENCODING","GB2312")
    # 注册所有的驱动
    ogr.RegisterAll()
    #创建输出shp
    driver = ogr.GetDriverByName('ESRI Shapefile')
    os.chdir(path)
    if os.path.exists(shpfilename):
        driver.DeleteDataSource(shpfilename)
    outds = driver.CreateDataSource(shpfilename)
    if outds == None:
        print('创建文件失败！')
    #创建图层
    dst_osr = osr.SpatialReference()
    dst_osr.ImportFromEPSG(4326)
    #获取文件名，不包含扩展名
    layername = os.path.splitext(shpfilename)[0]
    print('layername:=='+layername)
    outlayer = outds.CreateLayer(layername,dst_osr,geom_type = ogr.wkbPoint)
    #获取EXCEL表头及数据
    columns,data=readExcelbyFileNameAndSheetName(ExcelName,'Sheet1')
    #获取表头个数
    columns_count = len(columns)
    print('columns_count==='+str(columns_count))

    #--------------------------创建属性表字段----------------------------------------
    #遍历所有表头并创建属性表字段
    for i in range(columns_count):
        FieldName = columns[i]
        print('FieldName==='+FieldName)

        #设置字段属性
        fieldDefn = ogr.FieldDefn(FieldName,ogr.OFTString)
        fieldDefn.SetWidth(100)
        #图层创建属性
        outlayer.CreateField(fieldDefn)

    #---------------------------创建要素-----------------------------------------------
    #读取要素统一属性
    featuredefn = outlayer.GetLayerDefn()

    #获取数据行数
    rows_count = len(data)
    print('rows_count==='+str(rows_count))

    #遍历所有数据行并将数据填写到shp字段中
    for row in range(rows_count):
        #获取每一行的X坐标WGS84_Lng，这里的参数是固定的，应该把参数分离出去，写活，
        # #否则换个表，如果存经纬度字段的变了顺序，就会出错
        point_x=float(data[row][Lng_columns_num-1])
        print('point_x==='+str(point_x))
        #获取每一行的Y坐标WGS84_Lat
        point_y=float(data[row][Lat_columns_num-1])
        print('point_y==='+str(point_y))

        # 创建点要素
        oFeaturePoint = ogr.Feature(featuredefn)
        #---------------------------给所有点要素的属性一一对应进行赋值-----------------
        #遍历所有列，给所有点要素的属性一一对应进行赋值
        for column in range(columns_count):
            #列名：即字段名，这里应该读取SHP的字段名，不能用EXCEL表头，可能会有创建字段时因为字段名太长而丢失完整字段名
            FieldName = columns[column]
            print('FieldName==='+FieldName)
            #每个cell的数据值
            FieldValue = data[row][column]
            print('FieldValue==='+str(FieldValue))
            #给各字段赋值
            oFeaturePoint.SetField(FieldName, FieldValue)

        #定义矢量要素为点
        geomPoint = ogr.Geometry(ogr.wkbPoint)
        #定义点的X,Y坐标值
        geomPoint.AddPoint(point_x,point_y)
        #给要素设置几何点信息
        oFeaturePoint.SetGeometry(geomPoint)
        #创建要素
        outlayer.CreateFeature(oFeaturePoint)

    outds.Destroy()

#数据所在目录
path ="D:\\GitHub\PyGdalStudy\\GDALShp\\Data"
#目录切换
os.chdir(path)
#EXCEL文件名
ExcelName='SpecialTownList.xlsx'
#输出SHP文件名
shpfilename='SpecialTown.shp'
#调用函数，这个表格中，经度在23列，纬度在24列
Excel2Shp(path,ExcelName,shpfilename,23,24)
#显示SHP
showShp(shpfilename)
