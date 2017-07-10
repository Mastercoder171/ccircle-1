class Ball:
    # Ball(x,y)
    def __init__(self, x, y, vx):
        self.x = x
        self.y = y
        self.vx = vxA
        self.size = 10

    def draw(self, window):
        window.drawCircle(self.x, self.y, self.size, 0, 0.3, 0.5)

    def update(self):
        self.x += self.vx
        if self.x >= (800 - self.size) or self.x <= self.size:
            self.vx *= -1