import pygame as pg

def pgcolor(r, g, b):
    if 0 < r < 1 or 0 < g < 1 or 0 < b < 1:
        return (r*255, g*255, b*255)

class PygameButton:
    
    def __init__(self, parent, coords, text, function, font = 'freesansbold.ttf', active = True):
        self.parent = parent
        self.coords = coords
        self.text = text
        self.function = function
        self.font = font
        try :
            self.font = pg.font.Font(self.font, 20)
        except FileNotFoundError:
            try :
                self.font = pg.font.SysFont(self.font, 20)
            except TypeError:
                self.font = pg.font.Font('freesansbold.ttf', 20)
        self.active = active
        self.clicked = False
        self.clicked_prev_frame = False

    def add(self):

        self.clicked = self.detect_click()

        display_status = self.display()
        if self.active and not display_status == 'Invalid coordinates':
            self.do_function()
        else :
            self.active = False
    
    def display(self):
        print('PygameButton is the parent class to PygamePressButton and PygameToggleButton. It does nothing in itself')

    def detect_click(self):

        mouse_pos = pg.mouse.get_pos()
        left_click = pg.mouse.get_pressed()[0]
        
        if not left_click:
            self.clicked_prev_frame = False

            return False
        

        elif self.button_rect.collidepoint(mouse_pos) and not self.clicked_prev_frame:
            self.clicked_prev_frame = True

            return True
        
        else :

            return False
        
    def do_function(self):

        if self.function is not None and self.clicked:
            self.function()
