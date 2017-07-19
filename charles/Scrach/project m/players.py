import ccircle


class player:

    def __init__(self, angle, x, y, width, height, size):
        self.pice1 = ccircle.Image("pice 4.jpg")
        self.angle = angle
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.size = size
        self.money = 1000

    def draw(self):
        self.pice1.draw(self.x, self.y, self.width, self.height, self.angle)

'''
        if self.state == 'right':
            self.pice1.draw(100, 100, 10, 10, 90)

        if self.state == 'down':
            self.pice1.draw(100, 100, 10, 10, 180)

        if self.state == 'left':
            self.pice1.draw(100, 100, 10, 10, 270)
'''