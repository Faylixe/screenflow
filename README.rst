ScreenFlow
==========

.. image:: https://circleci.com/gh/Faylixe/screenflow.svg?style=svg
    :target: https://circleci.com/gh/Faylixe/screenflow .. image:: https://api.codacy.com/project/badge/Grade/0d99a5f63cf241409f87661703906d33    :target: https://www.codacy.com/app/Faylixe/screenflow?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Faylixe/screenflow&amp;utm_campaign=Badge_Grade .. image:: https://api.codacy.com/project/badge/Coverage/0d99a5f63cf241409f87661703906d33    :target: https://www.codacy.com/app/Faylixe/screenflow?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Faylixe/screenflow&amp;utm_campaign=Badge_Coverage .. image:: https://readthedocs.org/projects/screenflow/badge/?version=latest
:target: http://screenflow.readthedocs.io/en/latest/?badge=latest
:alt: Documentation Status

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

Installation
------------

First screenflow
----------------
