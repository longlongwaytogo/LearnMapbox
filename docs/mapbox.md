
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