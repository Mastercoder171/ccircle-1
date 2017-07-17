class World:
    def __init__(self, name):
        self.name = name
        self.objects = []

    def add(self,obj):
        self.objects.append(obj)

    def draw(self, window):
        
        window.drawRect(300, 200, 800, 400, 0.7, 0.2, 0.3)
        for obj in self.objects:
            obj.draw(window)

    def update(self):
        for obj in self.objects:
            obj.update()