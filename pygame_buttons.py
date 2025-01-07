import pygame as pg

def pgcolor(r, g, b):
    if 0 < r < 1 :
        return (r*255, g*255, b*255)

class PygameButton:
    
    def __init__(self, parent, coords, text, function, active = True):
        self.parent = parent
        self.coords = coords
        self.text = text
        self.function = function
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

class PygamePressableButton(PygameButton):

    def __init__(self, parent, coords, text, function, color = (0.3,0.3,0.3), border_color = (0.05,0.05,0.05), clicked_color = (0.1,0.1,0.1), size = (150,40), active = True):

        super().__init__(parent, coords, text, function, active)
        self.size = size
        self.color = pgcolor(*color)
        self.border_color = pgcolor(*border_color)
        self.clicked_color = pgcolor(*clicked_color)

        self.text_width, self.text_height = text_size = self.font.size(self.text)
        if self.size[0] < self.text_width + 20:
            self.size = list(self.size)
            self.size[0] = self.text_width + 20
            print('Text was too wide, button was made wider to fit the text')
        if self.size[1] < self.text_height + 20:
            self.size = list(self.size)
            self.size[1] = self.text_height + 20
            print('Text was too tall, button was made taller to fit the text')
        self.center = (coords[0]+size[0]/2, coords[1]+size[1]/2)
        self.button_rect = pg.rect.Rect(*self.coords, *self.size)

    def display(self):

        button_topleft = (int(self.center[0]-self.size[0]/2), int(self.center[1]-self.size[1]/2))
        button_botright = (int(self.center[0]+self.size[0]/2), int(self.center[1]+self.size[1]/2))
        if min(button_topleft) < 0 or button_botright[0] > self.parent.get_size()[0] or button_botright[1] > self.parent.get_size()[1]:
            print('Invalid coordinates for button')
            return 'Invalid coordinates'

        if not self.clicked:
            pg.draw.rect(self.parent, self.color, self.button_rect, 0, 6)
        else :
            pg.draw.rect(self.parent, self.clicked_color, self.button_rect, 0, 6)

        pg.draw.rect(self.parent, self.border_color, self.button_rect, 2, 6)

        text_topleft = (int(self.center[0]-self.text_width/2), int(self.center[1]-self.text_height/2))
        displayable_text = self.font.render(self.text, True, (0,0,0))
        self.parent.blit(displayable_text, text_topleft)


class PygameToggleButton(PygameButton):

    def __init__(self, parent, coords, text, function = None, check_color = (0.3,0.3,0.3), border_color = (0.05,0.05,0.05), clicked_color = (0.1,0.1,0.1), active = True):

        super().__init__(parent, coords, text, function, active)
        self.border_color = pgcolor(*border_color)
        self.clicked_color = pgcolor(*clicked_color)
        self.check_color = pgcolor(*check_color)

        self.text_width, self.text_height = text_size = self.font.size(self.text)
        self.size = (self.text_width+30, self.text_height+5)
        self.center = (coords[0]+self.size[0]/2, coords[1]+self.size[1]/2)

        self.button_rect = pg.rect.Rect(*self.coords, *self.size)
        self.checkbox_rect = pg.rect.Rect(self.coords[0], self.center[1]-10, 20,20)
        self.checkmark_rect = pg.rect.Rect(self.coords[0]+5, self.center[1]-5, 10, 10)

        self.checked = False

    def display(self):

        button_topleft = (int(self.center[0]-self.size[0]/2), int(self.center[1]-self.size[1]/2))
        button_botright = (int(self.center[0]+self.size[0]/2), int(self.center[1]+self.size[1]/2))
        if min(button_topleft) < 0 or button_botright[0] > self.parent.get_size()[0] or button_botright[1] > self.parent.get_size()[1]:
            print('Invalid coordinates for button')
            return 'Invalid coordinates'

        if self.clicked:
            pg.draw.rect(self.parent, self.clicked_color, self.checkbox_rect, 2, 6)
            if self.checked:
                self.checked = False
            else:
                self.checked = True
        else :
            pg.draw.rect(self.parent, self.border_color, self.checkbox_rect, 2, 6)

        if self.checked:
            pg.draw.rect(self.parent, self.check_color, self.checkmark_rect, 0, 3)

        text_topleft = (int(self.coords[0]+25), int(self.center[1]-self.text_height/2))
        displayable_text = self.font.render(self.text, True, (0,0,0))
        self.parent.blit(displayable_text, text_topleft)
