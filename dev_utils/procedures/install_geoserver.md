# install geoserver

## install java 11

>[!NOTE] 
> doc of geoserver (not the rest one!) says only java 17 or 11 will work.

    sudo apt update
    sudo apt install openjdk-11-jdk


## build virtualenv for geoserver-rest

    cd /corsi_udemy/web-mapping-and-webgis-geodjango/geoserver-rest

    virtualenv venv

    source venv/bin/activate

    sudo apt install libgdal-dev
    pip install GDAL==$(gdal-config --version | awk -F'[.]' '{print $1"."$2}')

    pip install -r requirements.txt


## install geoserver 

following the documentation https://docs.geoserver.org/latest/en/user/installation/linux.html

linux: select web archive from https://geoserver.org/release/stable/

downloaded<br>
and saved into new path<br>

    cd /usr/share/
    sudo mkdir geoserver

    cp ..../geoserver-2.22.0-bin.zip  /usr/share/geoserver/

---> /usr/share/geoserver/geoserver-2.22.0-bin.zip

unzip via UI

    cd /usr/share/geoserver/
    xdg-open .

e.g. /usr/share/geoserver/lib/

run 

    echo "export GEOSERVER_HOME=/usr/share/geoserver" >> ~/.profile
    . ~/.profile

    sudo chown -R $USER /usr/share/geoserver/

e.g.

    sudo chown -R tommaso /usr/share/geoserver/

## test geoserver

    cd /usr/share/geoserver/bin/ && sh startup.sh 

wait some seconds, then, in a web browser, navigate to http://localhost:8080/geoserver

