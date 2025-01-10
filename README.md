# pygame_buttons
Adds two types of buttons to pygame : one pressable and one toggleable

## Installation

To use the module, either download it to your project folder or install it by running `pip install git+https://github.com/Remy-Pa/pygame_buttons.git`

## Use

Both buttons need to be displayed onto a pygame.Surface. Buttons can be initialized before the mainloop and then displayed in the mainloop (see example bellow). They inherit from a PygameButton class which would make adding other types of buttons easy.

```python
import pygame as pg
from pygame_buttons import *

# code to make pygame work
pg.init()
size = (800,800)
window = pg.display.set_mode(size)
clock = pg.time.Clock()

# define the function you want your button to execute
n = 1
def random_function():
    global n
    print(f'The function was used {n} times!')
    n += 1

# initialize buttons
pressable_button = pygame_pressable_button.PygamePressableButton(window, (100,100), 'This button is pressable', random_function) # this is line 1/4 which actually depends on the pygame_buttons module
togglable_button = pygame_togglable_button.PygameTogglableButton(window, (100,200), 'This button is toggleable', function = random_function) # this is line 2/4 which actually depends on the pygame_buttons module

while True:
    # code to make pygame work
    clock.tick(20)
    window.fill((255,255,255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()


    # this line adds the buttons
    pressable_button.add() # this is line 3/4 which actually depends on the pygame_buttons module
    togglable_button.add() # this is line 4/4 which actually depends on the pygame_buttons module
    pg.display.flip()
```

### Output

![image](https://github.com/user-attachments/assets/f72d68fc-e571-45cf-afaa-6ef71844c25e)

As the function is defined that was, every time either button is pressed, it prints a new line in the terminal.

## Detailed description

### Pressable button
The pressable button is a button which calls a function when clicked.

> **pygame_buttons.PygamePressableButton(**parent, coords, text, function, color = (0.3,0.3,0.3), border_color = (0.05,0.05,0.05), clicked_color = (0.1,0.1,0.1), size = (150,40), active = True**)**

* parent : pygame.Surface on which to display the button
* coords : tuple of the coordinates at which to display the button
* text : string of the text to be displayed on the button
* function : function which will be called each time the button is pressed
* color, border_color and clicked_color : tuple of RGB values of the button when it is normal, its border and its color when it is in the process of being pressed. Unit-RGB (any set of numbers which has at least one between 0 and 1) will be converted to regular RGB (0 to 255).
* size : tuple of the size of the button. If the text is too large, the button will be made larger to fit the text so the size can usually be kept at default values.
* active : boolean. If False, the button will not call its function when pressed.

### Toggleable button
The pressable button is a button which holds a boolean depending on wether it is toggled or not. This boolean is stored in the self.checked variable.

> **pygame_buttons.PygameTogglableButton(**parent, coords, text, function = None, check_color = (0.3,0.3,0.3), border_color = (0.05,0.05,0.05), clicked_color = (0.1,0.1,0.1), active = True**)**

* parent : pygame.Surface on which to display the button
* coords : tuple of the coordinates at which to display the button
* text : string of the text to be displayed on the button
* function : function which will be called each time the button is pressed
* check_color, border_color and clicked_color : tuple of RGB values of the button's checkbox, the tick inside the checkbox when it is checked and its color when it is in the process of being pressed. Unit-RGB (any set of numbers which has at least one between 0 and 1) will be converted to regular RGB (0 to 255).
* active : boolean. If False, the button will not call its function when pressed.
