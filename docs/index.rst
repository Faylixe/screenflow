.. Screenflow documentation master file, created by
   sphinx-quickstart on Thu Mar  9 15:20:09 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Screenflow
==========

Contents:

.. toctree::
   :maxdepth: 2

**ScreenFlow** is a light UI engine built on top of Pygame.
It is primarily designed for building configuration interface for IoT devices like RaspberryPi.

ScreenFlow is based on Screen
------------------------------

There is no screen flow without screen obviously, so an application built with **ScreenFlow**
requires to create and connect together a serie of screens. The application switch from
one screen to another by sliding horizontally, keeping the navigation state into an internal stack.

A **Screen** aims to be dedicated to a single task, for exemple : 

- Input text
- Allow user to select option
- View a list or a grid of items
- And so on ...

That is why lot of basic **Screen** implementation are already available as in.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

