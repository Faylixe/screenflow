# ScreenFlow

**ScreenFlow** is a light UI engine built on top of Pygame.
It is primarily designed for building interface for IoT devices like RaspberryPi.

## ScreenFlow is based on Screen

There is no screen flow without screen obviously, an application built with **ScreenFlow**
requires to create and connect together a serie of screens. The application switch from
one screen to another by sliding horizontally, keeping the navigation state into a internal stack.

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
    print(text)

input_screen = InputScreen('What's your age ?')
input_screen.on_validate(consume_input).then(flow.quit)

flow = ScreenFlow()
flow.add_screen('first', input_screen)
flow.run()
```