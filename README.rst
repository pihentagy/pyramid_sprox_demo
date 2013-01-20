This demo just shows the setup required to get Sprox working under Pyramid.

::

    git clone https://github.com/mmerickel/pyramid_sprox_demo.git
    cd pyramid_sprox_demo
    virtualenv env
    env/bin/python setup.py develop
    env/bin/demo_initdb development.ini
    env/bin/pserve development.ini
