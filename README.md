# Web Mapping and Web-GIS from Dev to Deployment: GeoDjango

This django app allows the user to load `.tiff` files and zipped `.shp` files into `geoserver` software, where they are used as source to display their representation on the map of the frontend part of the app.

The upload can be done via the django-admin UI page.

The tiff file is directly loaded into geoserver, while the shp file is also loaded into postgres as table having name equal to the name specified in the upload UI panel.


# source

The app is based on [iamtekson](https://github.com/iamtekson "iamtekson")'s [geodjango-from-dev-to-deployment](https://github.com/iamtekson/geodjango-from-dev-to-deployment "geodjango-from-dev-to-deployment") project.


## requirements

This app requires java 11 or 17, geoserver, postgres and postgis extension for postgres.


## original source of the code

### original repo name

    geodjango-from-dev-to-deployment

### verbose project name

    Web Mapping and Web-GIS from Dev to Deployment: GeoDjango


## refactored code

### project name

    geoApp

### django apps

    geoApp
    shp
    tiff


## Installation guide

https://github.com/tommasosansone91/geoApp/blob/master/dev_utils/install_on_raspberrypi.md