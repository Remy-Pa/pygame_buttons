import pygame as pg
from .pygame_button import PygameButton

def pgcolor(r, g, b):
    if 0 < r < 1 or 0 < g < 1 or 0 < b < 1:
        return (r*255, g*255, b*255)


class PygamePressableButton(PygameButton):

    def __init__(self, parent, coords, text, function, color = (0.3,0.3,0.3), border_color = (0.05,0.05,0.05), clicked_color = (0.1,0.1,0.1), size = (150,40), active = True):

        super().__init__(parent, coords, text, function, active)
        self.size = size
        self.color = pgcolor(*color)
        self.border_color = pgcolor(*border_color)
        self.clicked_color = pgcolor(*clicked_color)

        self.text_width, self.text_height = self.font.size(self.text)
        if self.size[0] < self.text_width + 20:
            self.size = list(self.size)
            self.size[0] = self.text_width + 20
            print('Text was too wide, button was made wider to fit the text')
        if self.size[1] < self.text_height + 20:
            self.size = list(self.size)
            self.size[1] = self.text_height + 20
            print('Text was too tall, button was made taller to fit the text')
        self.center = (coords[0]+self.size[0]/2, coords[1]+self.size[1]/2)
        self.button_botright = (int(self.center[0]+self.size[0]/2), int(self.center[1]+self.size[1]/2))
        self.button_rect = pg.rect.Rect(*self.coords, *self.size)

    def display(self):

        if min(self.coords) < 0 or self.button_botright[0] > self.parent.get_size()[0] or self.button_botright[1] > self.parent.get_size()[1]:
            print('Invalid coordinates for button')
            return 'Invalid coordinates'

        if not self.clicked:
            pg.draw.rect(self.parent, self.color, self.button_rect, 0, 6)
        else :
            pg.draw.rect(self.parent, self.clicked_color, self.button_rect, 0, 6)

        pg.draw.rect(self.parent, self.border_color, self.button_rect, 2, 6)

        text_topleft = (self.center[0]-self.text_width/2, self.center[1]-self.text_height/2)
        displayable_text = self.font.render(self.text, True, (0,0,0))
        self.parent.blit(displayable_text, text_topleft)
