# Generated by Django 4.1.3 on 2022-11-06 16:27

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_post_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='map',
            field=tinymce.models.HTMLField(default='<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;\n&lt;head&gt;    \n    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;\n    \n        &lt;script&gt;\n            L_NO_TOUCH = false;\n            L_DISABLE_3D = false;\n        &lt;/script&gt;\n    \n    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;\n    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;\n    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/leaflet.js&quot;&gt;&lt;/script&gt;\n    &lt;script src=&quot;https://code.jquery.com/jquery-1.12.4.min.js&quot;&gt;&lt;/script&gt;\n    &lt;script src=&quot;https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js&quot;&gt;&lt;/script&gt;\n    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;\n    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/leaflet.css&quot;/&gt;\n    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css&quot;/&gt;\n    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css&quot;/&gt;\n    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css&quot;/&gt;\n    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;\n    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;\n    \n            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,\n                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;\n            &lt;style&gt;\n                #map_e7fb685c0d5342d1d06ce904011808fd {\n                    position: relative;\n                    width: 100.0%;\n                    height: 100.0%;\n                    left: 0.0%;\n                    top: 0.0%;\n                }\n            &lt;/style&gt;\n        \n&lt;/head&gt;\n&lt;body&gt;    \n    \n            &lt;div class=&quot;folium-map&quot; id=&quot;map_e7fb685c0d5342d1d06ce904011808fd&quot; &gt;&lt;/div&gt;\n        \n&lt;/body&gt;\n&lt;script&gt;    \n    \n            var map_e7fb685c0d5342d1d06ce904011808fd = L.map(\n                &quot;map_e7fb685c0d5342d1d06ce904011808fd&quot;,\n                {\n                    center: [0, 0],\n                    crs: L.CRS.EPSG3857,\n                    zoom: 1,\n                    zoomControl: true,\n                    preferCanvas: false,\n                }\n            );\n\n            \n\n        \n    \n            var tile_layer_8b7dacb58e4702afb5df6002632070a6 = L.tileLayer(\n                &quot;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,\n                {&quot;attribution&quot;: &quot;Data by \\u0026copy; \\u003ca href=\\&quot;http://openstreetmap.org\\&quot;\\u003eOpenStreetMap\\u003c/a\\u003e, under \\u003ca href=\\&quot;http://www.openstreetmap.org/copyright\\&quot;\\u003eODbL\\u003c/a\\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}\n            ).addTo(map_e7fb685c0d5342d1d06ce904011808fd);\n        \n&lt;/script&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>'),
        ),
    ]
