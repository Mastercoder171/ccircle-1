import cloud
import world
import ccircle
import random
+

window = ccircle.Window("Lab 1", 800, 600)
my_world = world.World("blah")

for i in range(200):
    x = random.randint(0, 800)
    y = random.randint(0, 150)
    size = random.randint(25, 100)
    my_world.add(cloud.Cloud(x, y, size))


while window.isOpen():
    window.clear(0.1, 0.1, 0.1)
    my_world.draw(window)
    my_world.update
    window.update()