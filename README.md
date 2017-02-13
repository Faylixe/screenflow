# ScreenFlow

**ScreenFlow** is a light UI engine built on top of Pygame.
It is primarily designed for building interface for IoT devices like RaspberryPi.

## ScreenFlow is based on Screen

There is no screen flow without screen obviously, an application built with **ScreenFlow**
requires to create and connect together a serie of screens. The application switch from
one screen to another by sliding horizontally, keeping the navigation state into an internal stack.

A **Screen** aims to be dedicated to a single task, for exemple : 

- Input text
- Allow user to select option
- View a list or a grid of items
- And so on ...

That is why lot of basic **Screen** implementation are already available as in.

## Getting started

First install **ScreenFlow** using ``pip``:

```bash
pip install screenflow
```

Now let implements a basic flow with one screen:
```python
from screenflow import ScreenFlow
from screenflow.screens import InputScreen

def consume_input(text):
    print('Hello %s' % text)

input_screen = InputScreen('Enter your name')
input_screen.on_validate(consume_input).then(flow.quit)

flow = ScreenFlow()
flow.add_screen('first', input_screen)
flow.run()
```

## Define your flow with XML

You can also (and better have to) define all your screens using XML file like in the following exemple :

```xml
<?xml version="1.0" encoding="utf-8" ?>
<screenflow start="first">
    <screen name="first" type="input">
        <label>Enter your age</label>
    </screen>
</screenflow>
```

Then back to python load the flow by calling ``load_with_xml`` method :

```python
from screenflow import ScreenFlow

def consume_input(text):
    print('Hello %s' % text)

flow = ScreenFlow()
flow.load_from_xml('')
flow.first.on_validate(consume_input).then(flow.quit)
flow.run()
```

A **SceneFlow** instance bind attribute access with scene name for better readability,
so you can access your previously XML defined screen by ``flow.first`` like in the previous exemple.
