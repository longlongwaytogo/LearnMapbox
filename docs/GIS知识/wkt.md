https://www.cnblogs.com/tiandi/archive/2012/07/18/2598093.html


# WKT 
## 1. WKT 概念
WKT(Well-known text)是一种文本标记语言，用于表示矢量几何对象、空间参照系统及空间参照系统之间的转换。它的二进制表示方式，亦即WKB(well-known binary)则胜于在传输和在数据库中存储相同的信息。该格式由开放地理空间联盟(OGC)制定。

## 2. WKT 几何对象
KT可以表示的几何对象包括：点，线，多边形，TIN（不规则三角网）及多面体。可以通过几何集合的方式来表示不同维度的几何对象。
几何物体的坐标可以是2D(x,y),3D(x,y,z),4D(x,y,z,m),加上一个属于线性参照系统的m值。
以下为几何WKT字串样例：
        POINT(6 10)
        LINESTRING(3 4,10 50,20 25)
        POLYGON((1 1,5 1,5 5,1 5,1 1),(2 2,2 3,3 3,3 2,2 2))
        MULTIPOINT(3.5 5.6, 4.8 10.5)
        MULTILINESTRING((3 4,10 50,20 25),(-5 -8,-10 -8,-15 -4))
        MULTIPOLYGON(((1 1,5 1,5 5,1 5,1 1),(2 2,2 3,3 3,3 2,2 2)),((6 3,9 2,9 4,6 3)))
        GEOMETRYCOLLECTION(POINT(4 6),LINESTRING(4 6,7 10))
        POINT ZM (1 1 5 60)
        POINT M (1 1 80)
        POINT EMPTY
        MULTIPOLYGON EMPTY

## 3. WKT - 空间参照系统】
一个表示空间参照系统的WKT字串描述了空间物体的测地基准、大地水准面、坐标系统及地图投影。
WKT在许多GIS程序中被广泛采用。ESRI亦在其shape文件格式(*.prj)中使用WKT。
以下是空间参照系统的WKT表示样例：
        COMPD_CS["OSGB36 / British National Grid + ODN",
        PROJCS["OSGB 1936 / British National Grid",
        GEOGCS["OSGB 1936",
        DATUM["OSGB_1936",
        SPHEROID["Airy 1830",6377563.396,299.3249646,AUTHORITY["EPSG","7001"]],
        TOWGS84[375,-111,431,0,0,0,0],
        AUTHORITY["EPSG","6277"]],
        PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],
        UNIT["DMSH",0.0174532925199433,AUTHORITY["EPSG","9108"]],
        AXIS["Lat",NORTH],
        AXIS["Long",EAST],
        AUTHORITY["EPSG","4277"]],
        PROJECTION["Transverse_Mercator"],
        PARAMETER["latitude_of_origin",49],
        PARAMETER["central_meridian",-2],
        PARAMETER["scale_factor",0.999601272],
        PARAMETER["false_easting",400000],
        PARAMETER["false_northing",-100000],
        UNIT["metre",1,AUTHORITY["EPSG","9001"]],
        AXIS["E",EAST],
        AXIS["N",NORTH],
        AUTHORITY["EPSG","27700"]],
        VERT_CS["Newlyn",
        VERT_DATUM["Ordnance Datum Newlyn",2005,AUTHORITY["EPSG","5101"]],
        UNIT["metre",1,AUTHORITY["EPSG","9001"]],
        AXIS["Up",UP],
        AUTHORITY["EPSG","5701"]],
        AUTHORITY["EPSG","7405"]


基础知识：
  坐标参照系有三种最常见的子类：
  - 地心坐标系(geocentric cs、GEOCCS)，
  - 地理坐标系(geographic cs、GEOGCS)
  - 投影坐标系(projected cs、PROJCS)
《坐标参照系》。投影参数内容：Ellipsoid 、 Datum ；Projection，可以参考《地图投影为什么》。

地理坐标系的格式：<geographic cs> = GEOGCS["<name>", <datum>, <prime meridian>, <angular unit>]

**WGS1984的地理坐标系WKT形式：**
        
        GEOGCS["WGS 84", 
        DATUM["WGS_1984",   // 基准面
        SPHEROID["WGS 84", 6378137, 298.257223563, AUTHORITY["EPSG", "7030"]], 
        AUTHORITY["EPSG", "6326"]], 
        PRIMEM["Greenwich", 0, AUTHORITY["EPSG", "8901"]], 
        UNIT["degree", 0.0174532925199433, AUTHORITY["EPSG", "9122"]],
        AUTHORITY["EPSG", "4326"]]

**投影坐标系的格式：**  
     
        <projected cs> = PROJCS["<name>", <geographic cs>, <projection>, {<parameter>,}* <linear unit>]

WGS1984地理坐标，统一横轴墨卡托(UTM)投影，中央经线117E的投影坐标系WKT形式：

        PROJCS["WGS 84 / UTM zone 50N", 
        GEOGCS["WGS 84", DATUM["WGS_1984", SPHEROID["WGS 84", 6378137, 298.257223563, AUTHORITY["EPSG", "7030"]], AUTHORITY["EPSG", "6326"]], PRIMEM["Greenwich", 0, AUTHORITY["EPSG", "8901"]], UNIT["degree", 0.0174532925199433, AUTHORITY["EPSG", "9122"]], AUTHORITY["EPSG", "4326"]], 
        PROJECTION["Transverse_Mercator"], 
        PARAMETER["latitude_of_origin", 0], 
        PARAMETER["central_meridian", 117], 
        PARAMETER["scale_factor", 0.9996], 
        PARAMETER["false_easting", 500000], 
        PARAMETER["false_northing", 0], 
        UNIT["metre", 1, AUTHORITY["EPSG", "9001"]], 
        AUTHORITY["EPSG", "32650"]]

地心坐标系格式相似于地理坐标系：<geocentric cs> = GEOCCS["<name>", <datum>, <prime meridian>, <linear unit>]