var DEFAULT_LONLAT = [126.9746921, 37.5728438];

var map;
var lonlat = DEFAULT_LONLAT;

var ignitedUntil = 0;
var oldCount;
var curCount;


function main() {
  var tile = new ol.layer.Tile({
    source: new ol.source.OSM({
      'url': '//cartodb-basemaps-{a-c}.global.ssl.fastly.net/dark_all/{z}/{x}/{y}.png'
    })
  });

  map = new ol.Map({
    target: 'map',
    layers: [tile],
    view: new ol.View({
      center: ol.proj.fromLonLat(DEFAULT_LONLAT),
      zoom: 5,
      minZoom: 2,
      maxZoom: 12
    }),
    interactions: ol.interaction.defaults({
      altShiftDragRotate: false,
      pinchRotate: false
    })
  });
}

main();
