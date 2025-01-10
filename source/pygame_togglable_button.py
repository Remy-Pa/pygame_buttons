class PygameTogglableButton(PygameButton):

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
