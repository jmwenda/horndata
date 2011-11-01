import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="horndata",
    version="0.1",
    author="Ariel Nunez, Jeffrey Johnson",
    author_email="ingenieroariel@gmail.com",
    description="Code behind horn.rcmrd.org",
    long_description=(read('README')),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: GeoNode',
        'License :: OSI Approved :: GNU Library or General Public License (GPL)',
    ],
    license="GPL 3",
    keywords="horn of africa geonode django",
    url='https://github.com/jmwenda/horndata',
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=False,
)
