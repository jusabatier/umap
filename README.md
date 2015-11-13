
# uMap project (CAS Version)

## About

uMap lets you create maps with OpenStreetMap layers in a minute and embed them in your site.
*Because we think that the more OSM will be used, the more OSM will be ''cured''.*
It uses [django-leaflet-storage](https://github.com/umap-project/django-leaflet-storage) and [Leaflet.Storage](https://github.com/umap-project/Leaflet.Storage),  built on top of Django and Leaflet.

CAS version is a fork from [uMap](https://github.com/umap-project/umap)

## Quickstart

Install python 3.4 and pip :

    apt-get install python3.4 python3-pip

Install virtualenv :

    pip3 install virtualenv

Install Django, GeoSpatial librairies and Postgres/PostGIS :

    apt-get install python-django
    apt-get install binutils libproj-dev gdal-bin libgeoip1 python-gdal
    apt-get install postgresql-9.4-postgis-2.1 postgresql-server-dev-9.4 python-psycopg2

Create the virtualenv and use it :

    virtualenv umap
    source umap/bin/activate

Get sources :

    apt-get install git
    mkdir sources
    cd sources
    git clone -b cas https://github.com/jusabatier/umap.git
    cd umap

Get dependencies : 

    apt-get install libjpeg-dev
    pip3 install -r requirements.txt
    pip3 install -e .

Create a default local settings file :

    cp umap/settings/local.py.sample umap/settings/local.py

Set database connexion informations in `local.py` :

    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'umap',
            'USER': 'umap',
            'PASSWORD': 'password',
            'HOST': '<server_ip>',
            'PORT': '5432',
        }
    }

Add a `SECRET_KEY` in `local.py` with a long random secret key :

    SECRET_KEY = "a long and random secret key that must not be shared"

uMap CAS uses [django-cas-client](https://github.com/kstateome/django-cas/) for user authentication. So you will need to configure it according to your needs.

For example

    CAS_SERVER_URL = 'http://<cas_ip>:8080/cas/'
    CAS_LOGOUT_COMPLETELY = True
    CAS_PROVIDE_URL_TO_LOGOUT = True

Adapt the `STATIC_ROOT` and `MEDIA_ROOT` to your local environment.

Create the tables

    python manage.py migrate

Collect and compress the statics

    python manage.py collectstatic
    python manage.py compress

Add a site object

    python manage.py shell
    from django.contrib.sites.models import Site
    Site.objects.create(name='example.com', domain='example.com')

Start the server

    python manage.py runserver 0.0.0.0:8000

Go to the admin (http://localhost:8000/admin/), it will redirect you to your CAS server login page.

Login with the account you want to promote as admin in uMap.

It will redirect you to a Forbidden page, saying that you're not a staff member.

At this moment, connect to your Postgres Database and in the **auth_user** table, set **is_superuser** and **is_staff** values to true.

Then refresh the previous page and you should access to the administration of umap.

Now for starting, you need to add :

- at least one license
- at least one tile layer

## Search

UMap uses Postgresql tsvector for searching. It case your database is big, you
may want to add an index. For that, you sould do so:

    CREATE EXTENSION unaccent;
    CREATE EXTENSION btree_gin;
    ALTER FUNCTION unaccent(text) IMMUTABLE;
    ALTER FUNCTION to_tsvector(text) IMMUTABLE;
    CREATE INDEX search_idx ON leaflet_storage_map USING gin(to_tsvector(unaccent(name)), share_status);

## Translating

Everything is managed through Transifex: https://www.transifex.com/projects/p/umap/
