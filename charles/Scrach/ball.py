class Ball:
    # Ball(x,y)
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.size = 10

    def draw(self, window):
        window.drawCircle(self.x, self.y, self.size, 0, 0.3, 0.5)

    def update(self):
        self.x += self.vx

        # print(self.x)
        # print(self.vy)
        # print(self.vx)

        rightWall = (800 - self.size)
        leftWall = self.size
        if self.x > rightWall or self.x < leftWall:
            self.vx *= -0.82
            self.x = leftWall if self.x < leftWall else rightWall

        self.y += self.vy
        self.vy += 0.1
        if self.y >= (550 - self.size) or self.y <= self.size:
            self.vy *= -0.90

