'''
Function:
    setup the videodl
Author:
    Charles
微信公众号:
    Charles的皮卡丘
GitHub:
    https://github.com/CharlesPikachu
'''
import videodl
from setuptools import setup, find_packages


'''readme'''
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


'''setup'''
setup(
    name=videodl.__title__,
    version=videodl.__version__,
    description=videodl.__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ],
    author=videodl.__author__,
    url=videodl.__url__,
    author_email=videodl.__email__,
    license=videodl.__license__,
    include_package_data=True,
    install_requires=['requests >= 2.22.0', 'click >= 7.0', 'prettytable >= 0.7.2'],
    zip_safe=True,
    packages=find_packages()
)