[source 属性解释](https://docs.mapbox.com/mapbox-gl-js/style-spec/#sources)


# Sources（数据源）
## 说明
## 1. 
source提供的数据将显示在地图上。源的类型由"type"属性指定，并且必须是vector，raster，raster-dem，geojson，image，video之一。添加源不会立即使数据显示在地图上，因为源不包含颜色或宽度等样式细节。图层引用源并为其提供可视化表示。这使得可以以不同的方式对相同的源进行样式化，例如区分高速公路层中的道路类型。

## 2.
Tiled sources（矢量和栅格）必须根据[TileJSON](https://github.com/mapbox/tilejson-spec)规范指定其详细信息。这可以通过以下几种方式完成：

### 2.1
 通过提供TileJSON属性，如"tiles"，"minzoom"以及"maxzoom"直接在source中使用：
```json
        "mapbox-streets": {
            "type": "vector",
            "tiles": [
            "http://a.example.com/tiles/{z}/{x}/{y}.pbf",
            "http://b.example.com/tiles/{z}/{x}/{y}.pbf"
            ],
            "maxzoom": 14
        }
```
服务端可以使用文件服务方式进行发布
### 2.2 
通过提供"url"TileJSON资源：
```json
        "mapbox-streets": {
            "type": "vector",
            "url": "http://api.example.com/tilejson.json"
        }
```
### 2.3 
通过向支持EPSG：3857（或EPSG：900913）的WMS服务器提供URL作为切片数据的来源。服务器URL应包含"{bbox-epsg-3857}"替换标记以提供bbox参数。
```json
        "wms-imagery": {
            "type": "raster",
            "tiles": [
            'http://a.example.com/wms?bbox={bbox-epsg-3857}&format=image/png&service=WMS&version=1.1.1&request=GetMap&srs=EPSG:3857&width=256&height=256&layers=example'
            ],
            "tileSize": 256
        }
```

# vector（矢量）
vector tile source。切片必须采用[Mapbox Vector Tile](https://www.mapbox.com/developers/vector-tiles/)格式。在矢量砖所有几何坐标必须介于-1 * extent和(extent * 2) - 1包容性。使用矢量源的所有图层都必须指定一个"source-layer"值。对于由Mapbox托管的矢量切片，"url"值应为表单。mapbox://mapid
```json
    "mapbox-streets": {
        "type": "vector",
        "url": "mapbox://mapbox.mapbox-streets-v6"
    }
```

## 1. url（地址）
可选字符串。
TileJSON资源的URL。支持的协议是http:，https:和mapbox://<mapid>。

## 2. tiles（切片）
可选的字符串数组。
一个或多个tile源URL的数组，如TileJSON规范中所示。

## 3. bounds（边界）
可选的数字数组s。 默认为[-180,-85.051129,180,85.051129]。
一个数组，按以下顺序包含源边界框的西南角和东北角的经度和纬度：[sw.lng, sw.lat, ne.lng, ne.lat]。当此属性包含在源中时，Mapbox GL不会请求给定边界之外的任何切片。
## 4. scheme(方案)
可选的枚举。 一"xyz"，"tms"。默认为"xyz"。
影响拼贴坐标的y方向。假设全局 - 墨卡托（又称球形墨卡托）轮廓。

"xyz"：
Slippy map tilenames scheme。

"tms"：
OSGeo规范方案。

## 5. MINZOOM（最小缩放）
可选号码。 默认为0。
可用于切片的最小缩放级别，如TileJSON规范中所示。

## 6. MAXZOOM(最大缩放)
可选号码。 默认为22。
可用于切片的最大缩放级别，如TileJSON规范中所示。当以更高的缩放级别显示地图时，将使用maxzoom中的切片数据。

## 7. attribution(归属）
可选字符串。
包含向用户显示地图时要显示地图的归属者。

SDK支持	Mapbox GL JS	Android SDK	iOS SDK	macOS SDK
基本功能

> = 0.10.0	> = 2.0.1	> = 2.0.0	> = 0.1.0
# Raster(光栅)
栅格磁贴源。对于由Mapbox托管的栅格切片，"url"值应为表单。mapbox://mapid

"mapbox-satellite": {
    "type": "raster",
    "url": "mapbox://mapbox.satellite",
    "tileSize": 256
}
网址
可选字符串。
TileJSON资源的URL。支持的协议是http:，https:和mapbox://<mapid>。

### 1. tiles
可选的字符串数组。
一个或多个tile源URL的数组，如TileJSON规范中所示。

### 2. bounds
可选的数字数组s。 默认为[-180,-85.051129,180,85.051129]。
一个数组，按以下顺序包含源边界框的西南角和东北角的经度和纬度：[sw.lng, sw.lat, ne.lng, ne.lat]。当此属性包含在源中时，Mapbox GL不会请求给定边界之外的任何切片。

## 3. minzoom
可选号码。 默认为0。
可用于切片的最小缩放级别，如TileJSON规范中所示。

## 4.maxzoom
可选号码。 默认为22。
可用于切片的最大缩放级别，如TileJSON规范中所示。当以更高的缩放级别显示地图时，将使用maxzoom中的切片数据。

## 5. tileSize
可选号码。 单位为像素。默认为512。
显示此图层切片的最小视觉大小。仅可配置栅格图层。

## 5. scheme（方案）
可选的枚举。 一"xyz"，"tms"。默认为"xyz"。
影响拼贴坐标的y方向。假设全局 - 墨卡托（又称球形墨卡托）轮廓。

"xyz"：
Slippy map tilenames scheme。

"tms"：
OSGeo规范方案。

## 6. attribution
可选字符串。
包含向用户显示地图时要显示的归属者。

SDK支持	Mapbox GL JS	Android SDK	iOS SDK	macOS SDK
基本功能

> = 0.10.0	> = 2.0.1	> = 2.0.0	> = 0.1.0
Raster-dem
栅格DEM源。目前只支持Mapbox Terrain RGB（mapbox://mapbox.terrain-rgb）

"mapbox-terrain-rgb": {
    "type": "raster-dem",
    "url": "mapbox://mapbox.terrain-rgb"
}
## url
可选字符串。
TileJSON资源的URL。支持的协议是http:，https:和mapbox://<mapid>。

## tiles
可选的字符串数组s。
一个或多个tile源URL的数组，如TileJSON规范中所示。

## bounds
可选的数字数组s。 默认为[-180,-85.051129,180,85.051129]。
一个数组，按以下顺序包含源边界框的西南角和东北角的经度和纬度：[sw.lng, sw.lat, ne.lng, ne.lat]。当此属性包含在源中时，Mapbox GL不会请求给定边界之外的任何切片。

## MINZOOM
可选号码。 默认为0。
可用于切片的最小缩放级别，如TileJSON规范中所示。

## MAXZOOM
可选号码。 默认为22。
可用于切片的最大缩放级别，如TileJSON规范中所示。当以更高的缩放级别显示地图时，将使用maxzoom中的切片数据。

## tileSize
可选号码。 单位为像素。默认为512。
显示此图层切片的最小视觉大小。仅可配置栅格图层。

## attribution
可选字符串。
包含向用户显示地图时要显示的属性。

## encoding
可选的枚举。 一"terrarium"，"mapbox"。默认为"mapbox"。
此源使用的编码。默认情况下使用Mapbox Terrain RGB

"terrarium"：
Terrarium格式PNG瓷砖。有关详细信息，请参阅https://aws.amazon.com/es/public-datasets/terrain/。

"mapbox"：
Mapbox Terrain RGB图块。有关详细信息，请参阅https://www.mapbox.com/help/access-elevation-data/#mapbox-terrain-rgb。

SDK支持	Mapbox GL JS	Android SDK	iOS SDK	macOS SDK
基本功能

> = 0.43.0	尚不支持	尚不支持	尚不支持

# GeoJSON
一个GeoJSON的来源。必须通过"data"属性提供数据，该属性的值可以是URL或内联GeoJSON，
如下所示，是一个内嵌的Geojson结构：

"geojson-marker": {
    "type": "geojson",
    "data": {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [-77.0323, 38.9131]
        },
        "properties": {
            "title": "Mapbox DC",
            "marker-symbol": "monument"
        }
    }
}
此GeoJSON源示例通过其URL引用外部GeoJSON文档。GeoJSON文档必须位于同一域中，或使用CORS访问。

"geojson-lines": {
    "type": "geojson",
    "data": "./lines.geojson"
}

## data
可选。
GeoJSON文件的URL或内联GeoJSON。

## MAXZOOM
可选号码。 默认为18。
创建矢量切片的最大缩放级别（更高意味着在高缩放级别时更高的细节）。

## attribution
可选字符串。
包含向用户显示地图时要显示的属性。

## buffer
可选数字之间和包含。 0512默认为128。
每侧的图块缓冲区的大小。值0不产生缓冲区。值512会生成与磁贴本身一样宽的缓冲区。较大的值会在拼贴边缘附近产生较少的渲染瑕疵，并且性能较慢

## tolerance（公差）
可选号码。 默认为0.375。
Douglas-Peucker简化公差（更高意味着更简单的几何形状和更快的性能）。

## cluster（簇）
可选的布尔值。 默认为false。
如果数据是点要素的集合，则将此设置为true会将点按半点聚类成组。群集组成Point为源中的新功能，具有其他属性：

cluster是true如果点是集群
cluster_id集群的unqiue id与集群检查方法一起使用
point_count 分组到此群集中的原始点数
point_count_abbreviated 缩写点数

## clusterRadius
可选数字大于或等于。 0默认为50。
如果启用了群集，则每个群集的半径。值512表示半径等于图块的宽度。

## clusterMaxZoom
可选号码。
如果启用了群集，则最大缩放以对其进行聚类。默认为小于maxzoom的一个缩放（以便最后的缩放功能不会聚集）。

## clusterProperties
可选。
如果启用了群集，则在生成的群集上定义自定义属性的对象，聚合来自群集点的值。有形式{"property_name": [operator, map_expression]}。operator是任何表达式函数，它接受至少2个操作数（例如"+"或"max"） - 它从集群包含的簇/点累积属性值; map_expression产生单个点的值。

示例：{"sum": ["+", ["get", "scalerank"]]}。

对于更高级的用例，operator您可以使用引用特殊["accumulated"]值的自定义reduce表达式代替，例如： {"sum": [["+", ["accumulated"], ["get", "sum"]], ["get", "scalerank"]]}

## LineMetrics
可选的布尔值。 默认为false。
是否计算行距离度量。这是指定line-gradient值的线图层所必需的。

## generateId
可选的布尔值。 默认为false。
是否为geojson功能生成id。启用后，feature.id将根据features数组中的索引自动分配属性，覆盖以前的任何值。

SDK支持	Mapbox GL JS	Android SDK	iOS SDK	macOS SDK
基本功能

> = 0.10.0	> = 2.0.1	> = 2.0.0	> = 0.1.0
集群

> = 0.14.0	> = 4.2.0	> = 3.4.0	> = 0.3.0
线距离度量

> = 0.45.0	> = 6.5.0	> = 4.4.0	> = 0.11.0

# image
图像源。该"url"值包含图像位置。

该"coordinates"数组包含[longitude, latitude]以顺时针顺序列出的图像角的对：左上角，右上角，右下角，左下角。

"image": {
    "type": "image",
    "url": "https://docs.mapbox.com/mapbox-gl-js/assets/radar.gif",
    "coordinates": [
        [-80.425, 46.437],
        [-71.516, 46.437],
        [-71.516, 37.936],
        [-80.425, 37.936]
    ]
}
## url
必填字符串。
指向图像的URL。

## coordinates
需要阵列的阵列的数目小号。
以经度，纬度对指定的图像角。

SDK支持	Mapbox GL JS	Android SDK	iOS SDK	macOS SDK
基本功能

> = 0.10.0	> = 5.2.0	> = 3.7.0	> = 0.6.0
# video
一个视频源。该"urls"值是一个数组。对于阵列中的每个URL，将创建视频元素源，以便支持不同浏览器支持的多种格式的相同媒体。

该"coordinates"数组包含[longitude, latitude]按顺时针顺序列出的视频角对：左上角，右上角，右下角，左下角。

"video": {
    "type": "video",
    "urls": [
        "https://static-assets.mapbox.com/mapbox-gl-js/drone.mp4",
        "https://static-assets.mapbox.com/mapbox-gl-js/drone.webm"
    ],
    "coordinates": [
        [-122.51596391201019, 37.56238816766053],
        [-122.51467645168304, 37.56410183312965],
        [-122.51309394836426, 37.563391708549425],
        [-122.51423120498657, 37.56161849366671]
    ]
}
## urls
必需的字符串数组s。
按首选格式排列的视频内容的URL。

## coordinates
需要阵列的阵列的数目小号。
以经度，纬度对指定的视频角。

SDK支持	Mapbox GL JS	Android SDK	iOS SDK	macOS SDK
基本功能

> = 0.10.0	尚不支持	尚不支持	尚不支持
# Sprite（雪碧图）
样式的sprite属性放入小图像渲染使用提供了一个网址范本background-pattern，fill-pattern，line-pattern，fill-extrusion-pattern和icon-image样式属性。

"sprite": "mapbox://sprites/mapbox/bright-v8"
有效的sprite源必须提供两种类型的文件：

一个索引文件，其是含有包含在所述子画面的每个图像的描述的JSON文档。此文件的内容必须是JSON对象，其键形成标识符以用作上述样式属性的值，其值是描述图像的尺寸（width和height属性）和像素比率（pixelRatio）的对象及其位置精灵（x和y）。例如，包含单个图像的sprite可能具有以下索引文件内容：
{
    "poi": {
        "width": 32,
        "height": 32,
        "x": 0,
        "y": 0,
        "pixelRatio": 1
    }
}
然后样式可以通过创建符号层的布局属性参考此子画面图像"icon-image": "poi"，或使用带标记的值"icon-image": "{icon}"与和矢量瓦片特征icon与所述值属性poi。
图像文件，它是包含精灵数据的PNG图像。
Mapbox SDK将使用sprite样式中的属性值来生成用于加载两个文件的URL。首先，对于这两种文件类型，它将附加@2x到高DPI设备上的URL。其次，它将附加文件扩展名：.json用于索引文件和.png图像文件。例如，如果你指定"sprite": "https://example.com/sprite"，渲染器将加载https://example.com/sprite.json和https://example.com/sprite.png，或https://example.com/sprite@2x.json和https://example.com/sprite@2x.png。

如果您使用的是Mapbox Studio，则将使用Mapbox提供的预构建sprite，或者您可以上传自定义SVG图像以构建您自己的sprite。在任何一种情况下，sprite都将自动构建并由Mapbox API提供。如果你想手工构建一个sprite并自行托管文件，你可以使用spritezero-cli，这是一个命令行实用程序，可以从SVG目录构建Mapbox GL兼容的sprite PNG和索引文件。

# Gglyphs（字形）
style的glyphs属性提供了一个URL模板，用于以PBF格式加载signed-distance-field字形集。

"glyphs": "mapbox://fonts/mapbox/{fontstack}/{range}.pbf"
此网址模板应包含两个令牌：

{fontstack}请求字形时，此标记将替换text-font为符号图层属性中指定的字体堆栈中以逗号分隔的字体列表。
{range}请求字形时，此标记将替换为256个Unicode代码点。例如，要为Unicode Basic Latin和Basic Latin-1 Supplement块加载字形，范围将为0-255。根据需要显示的文本，在运行时确定加载的实际范围。
过

# transition
一个transition属性控制的可转换风格属性以前的值和新值之间的插定时。样式的roottransition属性为该样式提供全局转换默认值。任何可转换样式属性也可以具有其自己的-transition属性，该属性定义该特定图层属性的特定转换时间，从而覆盖全局transition值。

    "transition": {
    "duration": 300,
    "delay": 0
    }

## duration(持续时间)
可选数字大于或等于。 0单位，以毫秒为单位。默认为300。
分配时间以完成转换。

## delay(延迟)
可选数字大于或等于。 0单位，以毫秒为单位。默认为0。
转换开始前的时间长度。


# Layers(图层)
样式的layers属性列出了该样式中可用的所有图层。图层的类型由"type"属性指定，并且必须是background(背景)，fill(填充)，line(线条)，symbol(符号)，raster(栅格)，circle(圆形)，fill-extrusion(填充-挤出)，heatmap(热图)，hillshade(山体阴影)之一。

除了背景类型的图层，每个图层都需要引用一个源。图层从源获取数据，可选择过滤器功能，然后定义这些功能的样式。

"layers": [
  {
    "id": "water",
    "source": "mapbox-streets",
    "source-layer": "water",
    "type": "fill",
    "paint": {
      "fill-color": "#00ffff"
    }
  }
]
## 1. id
必填字符串。
唯一的图层名称。

## 2. type
必需的枚举。 一"fill"，"line"，"symbol"，"circle"，"heatmap"，"fill-extrusion"，"raster"，"hillshade"，"background"。
渲染此图层的类型。

"fill"：
带有可选描边边框的填充多边形。

"line"：
划线。

"symbol"：
图标或文本标签。

"circle"：
一个圆圈。

"heatmap"：
热图。

"fill-extrusion"：
拉伸（3D）多边形。

"raster"：
光栅贴图纹理，如卫星图像。

"hillshade"：
基于DEM数据的客户端山体阴影可视化。目前，该实现仅支持Mapbox Terrain RGB和Mapzen Terrarium tile。

"background"：
地图的背景颜色或图案。

## 3. metadata（元数据）
可选。
任意属性对于跟踪图层很有用，但不影响渲染。应该为属性添加前缀以避免冲突，例如'mapbox：'。

## 4. source
可选字符串。
要用于此图层的源描述的名称。要求所有图层类型除外background。

## 5. source-layer
可选字符串。
要从矢量切片源使用的图层。矢量图块源需要; 禁止用于所有其他源类型，包括GeoJSON源。

## 6. MINZOOM
可选数字之间和包含。 024
图层的最小缩放级别。在缩放级别小于minzoom时，图层将被隐藏。

## 7. MAXZOOM
可选数字之间和包含。 024
图层的最大缩放级别。在缩放级别等于或大于maxzoom时，图层将被隐藏。

## 8 filter 过滤
可选表达式。
指定源要素条件的表达式。仅显示与过滤器匹配的功能。过滤器中的缩放表达式仅在整数缩放级别进行评估。的feature-state表达没有在过滤器表达式支持。

## 9. layout(布局)
可选布局。
图层的布局属性。

## 10. paint
可选涂料。
此图层的默认绘画属性。

图层有两个子属性，用于确定如何呈现来自该图层的数据：layout和paint属性。

布局属性显示在图层的"layout"对象中。它们在渲染过程的早期应用，并定义如何将该层的数据传递给GPU。对布局属性的更改需要异步“布局”步骤。

稍后在渲染过程中应用绘制属性。绘图属性显示在图层的"paint"对象中。对paint属性的更改很便宜并且同步发生。

# 11. background(背景)
能见度
布局属性。可选的枚举。 一"visible"，"none"。默认为"visible"。
是否显示此图层。

"visible"：
该层显示。

"none"：
该层未显示。

SDK支持	Mapbox GL JS	Android SDK	iOS SDK	macOS SDK
基本功能

> = 0.10.0	> = 2.0.1	> = 2.0.0	> = 0.1.0
background-color(背景颜色)
油漆属性。可选颜色。 默认为"#000000"。被 背景图案禁用。 可转变。
用于绘制背景的颜色。

SDK支持	Mapbox GL JS	Android SDK	iOS SDK	macOS SDK
基本功能

> = 0.10.0	> = 2.0.1	> = 2.0.0	> = 0.1.0
backgound-pattern(背景图案)
油漆属性。可选字符串。 可转变。
精灵中用于绘制图像背景的图像名称。对于无缝图案，图像宽度和高度必须是两倍（2,4,8，...，512）。请注意，仅在整数缩放级别评估与缩放相关的表达式。

SDK支持	Mapbox GL JS	Android SDK	iOS SDK	macOS SDK
基本功能

> = 0.10.0	> = 2.0.1	> = 2.0.0	> = 0.1.0
background-opacity(背景不透明度)
油漆属性。可选数字之间和包含。 01默认为1。可转变。
将绘制背景的不透明度。

SDK支持	Mapbox GL JS	Android SDK	iOS SDK	macOS SDK
基本功能

> = 0.10.0	> = 2.0.1	> = 2.0.0	> = 0.1.0
fill
能见度
布局属性。可选的枚举。 一"visible"，"none"。默认为"visible"。
是否显示此图层。

"visible"：
该层显示。

"none"：
该层未显示。

SDK支持	Mapbox GL JS	Android SDK	iOS SDK	macOS SDK
基本功能

> = 0.10.0	> = 2.0.1	> = 2.0.0	> = 0.1.0
fill-antialias
油漆属性。可选的布尔值。 默认为true。
填充是否应该是抗锯齿的。

SDK支持	Mapbox GL JS	Android SDK	iOS SDK	macOS SDK
基本功能

> = 0.10.0	> = 2.0.1	> = 2.0.0	> = 0.1.0
数据驱动的样式

尚不支持	尚不支持	尚不支持	尚不支持
填充不透明度
油漆属性。可选数字之间和包含。 01默认为1。可转变。
整个填充图层的不透明度。与此相反fill-color，如果使用笔划，此值也将影响填充周围的1px笔划。

SDK支持	Mapbox GL JS	Android SDK	iOS SDK	macOS SDK
基本功能

> = 0.10.0	> = 2.0.1	> = 2.0.0	> = 0.1.0
数据驱动的样式

> = 0.21.0	> = 5.0.0	> = 3.5.0	> = 0.4.0
fill-color
油漆属性。可选颜色。 默认为"#000000"。填充模式禁用 。 可转变。
此图层填充部分的颜色。此颜色可以指定为rgbaalpha分量，颜色的不透明度不会影响1px笔划的不透明度（如果使用）。

SDK支持	Mapbox GL JS	Android SDK	iOS SDK	macOS SDK
基本功能

> = 0.10.0	> = 2.0.1	> = 2.0.0	> = 0.1.0
数据驱动的样式

> = 0.19.0	> = 5.0.0	> = 3.5.0	> = 0.4.0
fill-outline-color
油漆属性。可选颜色。 填充模式禁用 。需要 填写抗锯齿是true。 可转变。
填充的轮廓颜色。匹配fill-colorif未指定的值。

SDK支持	Mapbox GL JS	Android SDK	iOS SDK	macOS SDK
基本功能

> = 0.10.0	> = 2.0.1	> = 2.0.0	> = 0.1.0
数据驱动的样式

> = 0.19.0	> = 5.0.0	> = 3.5.0	> = 0.4.0
fill-translate-anchor
h绘图属性。可选的数字数组s。 单位为像素。默认为[0,0]。可转变。
几何的偏移量。值为[x，y] ，其中负数分别表示左和上。

SDK支持	Mapbox GL JS	Android SDK	iOS SDK	macOS SDK
基本功能

> = 0.10.0	> = 2.0.1	> = 2.0.0	> = 0.1.0
数据驱动的样式

尚不支持	尚不支持	尚不支持	尚不支持
填写翻译锚
油漆属性。可选的枚举。 一"map"，"viewport"。默认为"map"。需要 填写翻译。
控制参考框架fill-translate。

"map"：
填充相对于地图进行翻译。

"viewport"：
填充相对于视口进行转换。

SDK支持	Mapbox GL JS	Android SDK	iOS SDK	macOS SDK
基本功能

> = 0.10.0	> = 2.0.1	> = 2.0.0	> = 0.1.0
数据驱动的样式

尚不支持	尚不支持	尚不支持	尚不支持
fill-pattern 填充图案
油漆属性。可选字符串。 可转变。
精灵中用于绘制图像填充的图像名称。对于无缝图案，图像宽度和高度必须是两倍（2,4,8，...，512）。请注意，仅在整数缩放级别评估与缩放相关的表达式。

SDK支持	Mapbox GL JS	Android SDK	iOS SDK	macOS SDK
基本功能

> = 0.10.0	> = 2.0.1	> = 2.0.0	> = 0.1.0
数据驱动的样式

> = 0.49.0	> = 6.5.0	> = 4.4.0	> = 0.11.0
