import cloud
import world
import ccircle
import random
import ball
import sun
window = ccircle.Window("Lab 1", 800, 800)
my_world = world.World("blah")

y_change = 0
for i in range(1):
    x = random.randint(0, 800)
    y = random.randint(0, 150)
    size = random.randint(25, 100)
    my_world.add(cloud.Cloud(x, y, size))
    my_world.add(ball.Ball(100, 100 - y_change, 3, 4))
    y_change += 3

while window.isOpen():
    window.clear(0.1, 0.1, 0.1)
    my_world.draw(window)
    my_world.update()
    window.update()
