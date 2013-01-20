from setuptools import setup, find_packages

requires = [
    'genshi',
    'pyramid',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'sprox',
    'SQLAlchemy<0.7.99',
    'transaction',
    'ToscaWidgets',
    'tw.forms',
    'waitress',
    'zope.sqlalchemy',
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
