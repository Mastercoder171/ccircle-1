import ccircle

class Background:

    def __init__(self, angle, pos):
        self.background = ccircle.Image("background.jpg")
        self.angle = angle
        self.pos = pos
        self.state = 'up'
    def position(self):

        self.pos = (self.pos + 1) % 4

    def draw(self):
        if self.state == 'up':
            self.background.draw(0, 0, 1600, 800, 0)


        if self.state == 'right':
            self.background.draw(400, -400, 800, 1600, 90)

        if self.state == 'down':
            self.background.draw(0, 0, 1600, 800, 180)

        if self.state == 'left':
            self.background.draw(400, -400, 800, 1600, 270)


