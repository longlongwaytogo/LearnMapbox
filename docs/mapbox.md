
# MapBox

　MapBox 最初是与 OpenStreetMaps 合作的开源项目，后来开始独立发展。当 Google 开始为地图 API 收费的时候，Mapbox 获得了巨大的发展机会。它的客户曾有 NPR、卫报、绿色和平组织和 FCC ，如今它为 Foursquare、Evernote 等公司提供地图服务。最近，MapBox 开始了一项野心勃勃的计划——构建世界上最漂亮的地图。

# TileMill
TileMill是基于 Mapnik, node.js,backbone.js, express and CodeMirror.这几个开源的软件构建起来的，看看开源的东西也还是非常强大的，只是我们很少去愿意使用他们，并不比商业的软件差多少。对其源码构建的可以去github上看看，地址：https://github.com/mapbox/tilemill。Mapnik提供地图的渲染,node.js及backbone.js等提供地图展示，地图配图使用Carto 的语言进行地图各个图层的配图样式等设计，和css很类似，但是比原先的mapnik的xml要方便和可读性要好很多。TileMill主要的功能有如下：

1、支持 ESRI Shapefile, KML, GeoJSON, GeoTIFF, PostGIS, and SQLite数据来源。
2、新版本支持大数据量栅格数据的加载与显示，支持山体阴影，分层设色等功能。
3、支持数据的查询，也就是属性数据的浏览。
4、支持以Carto css样式语言对地图进行配色设计（比xml要方便很多）
5、支持svg图标，truetype字体样式等，基于Mapnik提供（mapnik2.0出来了又强大了不少）
6、支持地图tooltip、图片、图表、utf-8 Grid(不是很了解这个技术)等自定义信息提示
7、支持直接发布到Mapbox，和朋友共享你制作的地图。


你可以把你的地图放在Mapbox的网站上。也可以使用他们提供的开源软件自己架设地图服务。
Mapbox的地图方案包括web，ios和android。 不过android目前属于不成熟阶段。但是相信很快就会成熟起来。

一个比较舒服的地图自制流程如下：

Qgis 处理各种GIS数据，导出为shp或GeoJson等格式 ==> TileMill 生成 .mbtile ==> tilestream 在线地图服务 或 直接由Android/IOS SDK 渲染地图。

QGIS的使用推荐教程：http://www.qgistutorials.com/en/
TileMill教程：https://www.mapbox.com/tilemill/docs/crashcourse/introduction/

reference:
- [MapBox：构建世界上最漂亮的地图 ](http://blog.sina.com.cn/s/blog_663d9a1f0101fb0g.html)

- [Mapbox使用详解](https://www.cnblogs.com/cg919/archive/2018/07/19/9336020.html)
- [MapBox教程](https://blog.csdn.net/jwdstef/article/details/38760111)
- [快速入门MapboxGL](https://blog.csdn.net/supermapsupport/article/details/78343391)

# mvt 生成工具
## tippecanoe 
Tippecanoe是Mapbox的一个开源切片工具，项目地址：https://github.com/mapbox/tippecanoe，Mapbox常规的切片方法tilelive-copy参见另一篇博客。Tippecanoe主要在处理大数据量时有很大的优势，具有很高的效率，并且有很多参数可以控制。Tippecanoe只能处理GeoJSON，因此在切片前需要将矢量数据转换为GeoJSON，推荐使用ogr2ogr工具转换。切片以后的格式为mbtiles，可自行导入mongodb等数据库。
--------------------- 
作者：山上九头鸟 
来源：CSDN 
原文：https://blog.csdn.net/wan_yanyan528/article/details/59071539 
版权声明：本文为博主原创文章，转载请附上博文链接！

[使用Tippecanoe工具处理大数据量的矢量数据切片](https://blog.csdn.net/wan_yanyan528/article/details/59071539?utm_source=blogxgwz2)
[tippecanoe](https://github.com/mapbox/tippecanoe)
[tippecanoe使用及参数](https://blog.csdn.net/wan_yanyan528/article/details/70226123)

## awesome-vector-tiles
  [awesome-vector-tiles](https://github.com/mapbox/awesome-vector-tiles)
 [矢量地图切片技术分析](http://qiancy.com/2016/12/10/vector-tiles/)

## mapbox Vector tiles [mvt]

[Vector tiles](https://docs.mapbox.com/vector-tiles/reference/)
[Vector tiles specification](https://docs.mapbox.com/vector-tiles/specification/)
[矢量瓦片标准](https://github.com/jingsam/vector-tile-spec/blob/master/2.1/README_zh.md)

# vector 发布工具

[josm、tippecanoe、tileserver-gl-light、mapbox发布自己的瓦片地图](https://blog.csdn.net/qq_26540693/article/details/86491049)
[windows安装tippecanoe并生成mbtiles](https://blog.csdn.net/weixin_42655593/article/details/87603044)
[矢量地理数据如何切片](https://www.zhihu.com/question/30404999)
[【GISER && Painter】矢量切片(Vector tile)](https://www.cnblogs.com/escage/p/6387529.html)





# 自己尝试的MVT切片工具：
1. Geoserver  参考：[利用geoserver发布矢量切片，mapbox进行调用](https://blog.csdn.net/qq_24622397/article/details/78411587)

  GeoServer ：
  user： admin
  paswword： geoserver
  port:8080
http://localhost:8080/geoserver/web/



安装tmcat,并拷贝文件
  tmcat 
  root 666666
[geoserver 矢量切片发布](https://www.jianshu.com/p/df45b0f6455b)
[geoserver 矢量切片发2](https://www.jianshu.com/p/4a35e935c466)
[Geoserver如何安装或部署最新图文教程](http://sh.qihoo.com/pc/9ade76f64d13f3a47?cota=4&tj_url=xz&sign=360_e39369d1&refer_scene=so_1)
[Publishing a GeoServer Layer for use with Mapbox Styles¶](https://docs.geoserver.org/latest/en/user/styling/mbstyle/source.html)

# 数据：
[高德地图行政区域下载](https://giser.xyz/2018/04/25/20180425-GetDistrictByAMap/)
[下载中国县级行政区划的边界数据并处理成geojson数据和Echarts的json数据](https://github.com/xioix2011/GeoJSON-for-ECharts)
[高德下载器](https://giser.xyz/demo/03-Dist-AMap/index.html)
[geojson 在线浏览工具](http://geojson.io)
[node-shapefile-viewer浏览工具](https://github.com/ginkgoch/node-shapefile-viewer/releases)

# mbtiles-server 
[mbtiles-server](https://github.com/chelm/mbtiles-server)
[mbtiles-server use](https://www.npmjs.com/package/mbtiles-server)


# tileserver-gl-light ：用来发布瓦片文件


