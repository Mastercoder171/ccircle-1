import ccircle


class player:

    def __init__(self, angle, x, y, width, height, size, money):
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

    def return_balance(self):
        print(self.money)