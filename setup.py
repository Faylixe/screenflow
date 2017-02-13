#!/usr/bin/python

""" Setup module for ScreenFlow """

from distutils.core import setup

setup(
    name='screenflow',
    packages=['screenflow'],
    version='1.0',
    description='Light UI engine built on top of Pygame.',
    author='Felix Voituret',
    author_email='felix.voituret@gmail.com',
    url='https://github.com/Faylixe/screenflow',
    download_url='https://github.com/Faylixe/screenflow/tarball/1.0',
    install_requires=['pygame', 'pygame_vkeyboard'],
    keywords=['pygame', 'UI'],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: pygame'
    ],
    include_package_data=True
)
