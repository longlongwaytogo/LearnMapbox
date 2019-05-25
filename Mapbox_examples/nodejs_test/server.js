var express = require('express');
var http = require('http');
var app = express();
var tilelive = require('tilelive');
require('mbtiles').registerProtocols(tilelive);


// 放置的矢量瓦片数据位置
//tilelive.load('mbtiles:///Users/lsw/Desktop/mapbox-server/hechi4326.mbtiles', function(err, source) {
    tilelive.load('C:\dev\LearnMapbox\Mapbox_examples\nodejs_test\out.mbtiles', function(err, source) { 
   if (err) {
       throw err;
   }

   // 设置端口为7777
   app.set('port', 7777);

   app.use(function(req, res, next) {
       // 服务端要支持跨域，否则会出现跨域问题
       res.header("Access-Control-Allow-Origin", "*");
       res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
       next();
   });

   //访问的url是：http://localhost:7777/tiles/{z}/{x}/{y}.pbf
   app.get(/^\/tiles\/(\d+)\/(\d+)\/(\d+).pbf$/, function(req, res) {
       var z = req.params[0];
       var x = req.params[1];
       var y = req.params[2];
       console.log('get tile %d, %d, %d', z, x, y);


       source.getTile(z, x, y, function(err, tile, headers) {
           if (err) {
               res.status(404)
               res.send(err.message);
               console.log(err.message);
           } else {
               res.set(headers);
               res.send(tile);
           }
       });
   });

   http.createServer(app).listen(app.get('port'), function() {
       console.log('Express server listening on port ' + app.get('port'));
   });
});