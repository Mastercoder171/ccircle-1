import ccircle

window = ccircle.Window()
window.toggleMaximized()
window.hideMouse()

points = []

while window.isOpen():
    window.clear(0.2, 0.2, 0.3)
    mx, my = window.getMousePos()

    if ccircle.isMouseDown('left'):
        points.append((mx, my))

    for point in points:

        window.drawCircle(point[0], point[1], 7, 0.3, 0.5, 0.9)

        if len(points)>= 21:
            window.drawCircle(points[20][0], points[6][1], 16, 1.0,0.3,0.1)

        window.drawCircle(mx, my, 8, 0.1, 0.3, 0.5)
    window.update()