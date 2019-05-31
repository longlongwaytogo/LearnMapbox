# 从pbf格式转换到Geojson格式


## 1. 使用 vt2geojson工具：

### 1.1 安装nodejs
### 1.2 安装vt2geojson: 
   
        npm i -g vt2geojson

## 1.3 使用方法：
    vt2geojson -x 13487 -y 6201 -z 14 D://Git/mapboxpbf2text/13487_6201_14.pbf > D://Git/mapboxpbf2text/test.geojson
[参考](https://blog.csdn.net/flowerspring/article/details/89318021)


# 2. 使用tippecanoe-decode 工具：

tippecanoe-decode
The tippecanoe-decode utility turns vector mbtiles back to GeoJSON. You can use it either on an entire file:

tippecanoe-decode file.mbtiles
or on an individual tile:

            tippecanoe-decode file.mbtiles zoom x y
            tippecanoe-decode file.vector.pbf zoom x y