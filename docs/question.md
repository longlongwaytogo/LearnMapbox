# Difference of Mapzen Vector Tiles (mvt) to pbf extracted from .mbtiles

I was wondering what is the difference between a mvt tile and a pbf extracted from a .mbtiles container using mbutil?

Mvt is in pbf as well. The pbf is supposed to be a vector tile as well.

They are not exactly the same, since I tried to read the pbf like I read a mvt file, but I was not successful. Could anyone explain the difference to me?


# What is the difference between *.mvt and *.vector.pbf formats? #69
 [github issues](https://github.com/mapbox/vector-tile-spec/issues/69)

 1.At this page, it use *.vector.pbf format.
http://a.tiles.mapbox.com/v4/mapbox.mapbox-streets-v6/14/4823/6160.vector.pbf?access_token=

But, this page said the vector tile format is *.mvt files.
The filename extension for Vector Tile files SHOULD be mvt. For example, a file might be named vector.mvt.

3.How can I parse the *.vector.pbf files?

So, I'm confused about them...
I want to show own vector map data in Android devices by Mapbox, the other formats files needs to be converted to *.mvt or *.vector.pbffiles?
