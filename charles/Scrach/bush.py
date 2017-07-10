class Bush:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, window):
        window.drawTri(self.x, self.y,400,300,420,320,440,340, 0.25 )

    def update(self):
        pass