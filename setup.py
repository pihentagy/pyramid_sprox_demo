from setuptools import setup, find_packages

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'waitress',
    'zope.sqlalchemy',
    'tw2.forms',
    'sprox >= 0.8.2'

]

setup(
    name='demo',
    version='0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = demo:main',
        ],
        'console_scripts': [
            'demo_initdb = demo.scripts.initdb:main',
        ],
    },
)
