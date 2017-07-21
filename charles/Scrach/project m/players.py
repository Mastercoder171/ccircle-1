import ccircle


class player:

    def __init__(self, angle, x, y, width, height, size, money, type):
        self.pice1 = ccircle.Image("pice 4.jpg")
        self.pice1.eraseWhite()
        self.pice2 = ccircle.Image("pice 9.jpg")
        self.pice2.eraseWhite()
        self.angle = angle
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.size = size
        self.money = 1000
        self.type = type

    def draw(self):

        if self.type == 'piece1':
            self.pice1.draw(self.x, self.y, self.width, self.height, 0)
        if self.type == 'piece2':
            self.pice2.draw(self.x, self.y, self.width, self.height, 0)

  #  def return_balance(self):



