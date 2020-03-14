# tornado-boilerplate

tornado-boilerplate try to set up an convention for Tornado app layouts.

## Description

The boilerplate project is adapted from some demo projects on the web and tornado's own documentation.

## Directory Structure

```
.
├── README.md
├── __init__.py
├── application.py
├── assets
│   ├── images
│   ├── javascripts
│   └── stylesheets
├── conf
│   └── application.json
├── environment.py
├── handlers
│   └──base.py
├── models
├── requirements.txt
├── services
├── settings.py
├── templates
├── tests
├── urls.py
├── utils
└── vendor
```

### assets

All of images, javascripts, stylesheets go in this directory.

### conf

Default configuration file directory

### handlers

All of your Tornado RequestHandlers go in this directory.

### models

The data models go in this directory.

### templates

Project-wide templates (i.e. those not belonging to any specific app in the `handlers/` folder). 

### vendor

Python package dependencies loaded as git submodules. pip's support for git repositories is somewhat unreliable, and if the specific package is your own code it can be a bit easier to debug if it's all in one place (and not off in a virtualenv).

At Bueda we collect general webapp helpers and views in the separate package`comrade` and share it among all of our applications. It is included here as an example of a Python package as a git submodule (comrade itself should't be considered part of this boilerplate - while it might be useful, it's much less generic).

Any directory in `vendor/` is added to the `PYTHONPATH` by `environment.py`. The packages are *not* installed with pip, however, so if they require any compilation (e.g. C/C++ extensions) this method will not work.

### Files

#### application.py

The main Tornado application, and also a runnable file that starts the Tornado server.

#### environment.py

Modifies the `PYTHONPATH` to allow importing from the `vendor/` directories. This module is imported at the top of `settings.py` to
make sure it runs for both local development (using Django's built-in server) and in production (run through mod-wsgi, gunicorn, etc.).

#### settings.py

A place to collect application settings.

#### urls.py

Urls and Handlers mapping.

## How to Use

## Acknowledgements

This boilerplate is modified based on [bueda/tornado-boilerplate](https://github.com/bueda/tornado-boilerplate).

