# shape
ESRI Shapefile（shp），或简称shapefile，是美国环境系统研究所公司（ESRI）开发的一种空间数据开放格式。目前，该文件格式已经成为了地理信息软件界的一个开放标准，这表明ESRI公司在全球的地理信息系统市场的重要性。Shapefile也是一种重要的交换格式，它能够在ESRI与其他公司的产品之间进行数据互操作。
Shapefile文件用于描述几何体对象：点，折线与多边形。例如，Shapefile文件可以存储井、河流、湖泊等空间对象的几何位置。除了几何位置，shp文件也可以存储这些空间对象的属性，例如一条河流的名字，一个城市的温度等等。


Shapefile是一种比较原始的矢量数据存储方式，它仅仅能够存储几何体的位置数据，而无法在一个文件之中同时存储这些几何体的属性数据。因此，Shapefile还必须附带一个二维表用于存储Shapefile中每个几何体的属性信息。Shapefile中许多几何体能够代表复杂的地理事物，并为他们提供强大而精确的计算能力。
Shapefile文件指的是一种文件存储的方法，实际上该种文件格式是由多个文件组成的。其中，要组成一个Shapefile，有三个文件是必不可少的，它们分别是".shp", ".shx"与 ".dbf"文件。表示同一数据的一组文件其文件名前缀应该相同。例如，存储一个关于湖的几何与属性数据，就必须有lake.shp，lake.shx与lake.dbf三个文件。而其中“真正”的Shapefile的后缀为shp，然而仅有这个文件数据是不完整的，必须要把其他两个附带上才能构成一组完整的地理数据。除了这三个必须的文件以外，还有八个可选的文件，使用它们可以增强空间数据的表达能力。所有的文件名都必须遵循MS DOS的8.3文件名标准（文件前缀名8个字符，后缀名3个字符，如shapefil.shp），以方便与一些老的应用程序保持兼容性，尽管现在许多新的程序都能够支持长文件名。此外，所有的文件都必须位于同一个目录之中。


必须的文件:
.shp— 图形格式，用于保存元素的几何实体。
.shx— 图形索引格式。几何体位置索引，记录每一个几何体在shp文件之中的位置，能够加快向前或向后搜索一个几何体的效率。
.dbf— 属性数据格式，以dBase IV的数据表格式存储每个几何形状的属性数据。
其他可选的文件：
.prj— 投帧式，用于保存地理坐标系统与投影信息，是一个存储well-known text投影描述符的文本文件。
.sbnand.sbx— 几何体的空间索引
.fbnand.fbx— 只读的Shapefiles的几何体的空间索引
.ainand.aih— 列表中活动字段的属性索引。
.ixs— 可读写Shapefile文件的地理编码索引
.mxs— 可读写Shapefile文件的地理编码索引(ODB格式)
.atx—.dbf文件的属性索引，其文件名格式为shapefile.columnname.atx(ArcGIS 8及之后的版本)
.shp.xml— 以XML格式保存元数据。
.cpg— 用于描述.dbf文件的代码页，指明其使用的字符编码。

在每个.shp,.shx与.dbf文件之中，图形在每个文件的排序是一致的。也就是说，.shp的第一条记录与.shx及.dbf之中的第一条记录相对应，如此类推。此外，在.shp与.shx之中，有许多字段的字节序是不一样的。因此用户在编写读取这些文件格式的程序时，必须十分小心地处理不同文件的不同字节序。
Shapefile通常以X与Y的方式来处理地理坐标，一般X对应经度，Y对应纬度，用户必须注意X，Y的顺序。

Shapefile图形格式 (.shp)
Shapefile格式的主文件包含了地理参照数据。该文件由一个定长的文件头和一个或若干个变长的记录数据组成。每一条变长数据记录包含一个记录头和一些记录内容。详细的数据存储格式由Esri Shapefile技术描述.提供。注意，虽然Shapefile文件的后缀名与AutoCAD的图形字体源格式它们的文件后缀名相同的，都是.shp，请不要把它们混淆。
[reference](https://baike.baidu.com/item/shapefile%E6%96%87%E4%BB%B6/11041662?fr=aladdin)
# Geojson
GeoJSON is a format for encoding a variety of geographic data structures.

        {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [125.6, 10.1]
        },
        "properties": {
            "name": "Dinagat Islands"
        }
        }
eoJSON supports the following geometry types: Point, LineString, Polygon, MultiPoint, MultiLineString, and MultiPolygon. Geometric objects with additional properties are Feature objects. Sets of features are contained by FeatureCollection objects.

[reference](https://geojson.org/)
[GeoJSON格式规范说明](https://www.oschina.net/translate/geojson-spec)
[GEOJSON标准格式学习](https://www.jianshu.com/p/852d7ad081b3)
[Json 格式生成工具](http://geojson.io/#map=2/18.6/-1.1)
# mvt

# mapbox 
