# mapbox 本地切片的制作和访问 
## 1. 使用 tippecanoe 制作mbtiles 数据库 
## 2. 使用 mbutil 从mbTiles中获取 bpf片 [也可以直接使用tippecanoe 导出pbf本地数据]
## 3. 由于mapbox只能加载未压缩的pbf格式数据，但直使用tippecanoe或mbuitl生成的pbf是经过gzip压缩的数据[不执行解压缩，mapbox加载数据会报："Unimplemented type: 3" 错误]，所以需要解压缩，可以通过py脚本执行解压工作

```bat
    UnGzip_pbf.py 源路径[压缩pbf路径] 目标路径[解压路径] 扩展名[默认扔使用pbf格式，也可改为mvt]

```

## 4. 安装nodejs的 anywhere服务器
``` bash
    npm i anywhere -g 
```

## 5. 将解压后的目录通过anywhere建立文件服务

![](file_server.PNG)

## 6. 编写mapbox代码
参考mabox例子[Add a vector tile source](https://docs.mapbox.com/mapbox-gl-js/example/vector-source/)
主要设置正确的切片路径
