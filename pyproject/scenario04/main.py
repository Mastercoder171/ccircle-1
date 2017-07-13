import ccircle
import connection

con = connection.create()
con.send('set_name', {'name': 'Hacker'})
print(con.send('get_boss_pos'))



args = {
    'vx': 0,
    'vy': 0
}

con.send('set_velocity' , args)

while True:

    if ccircle.isKeyDown('w'):
        args['vy'] -= 50
        con.send('set_velocity', args)

    if ccircle.isKeyDown('down'):
        args['vy'] += 50
        con.send('set_velocity', args)



    if ccircle.isKeyDown('left'):
        args['vx'] -= 50
        con.send('set_velocity', args)

    if ccircle.isKeyDown('right'):
        args['vx'] += 50
        con.send('set_velocity', args)

    if ccircle.isKeyDown('space'):
        con.send("damage_boss")


    if ccircle.isKeyDown("up"):
        con.send('send_money'('California', -100000000000000))

    vx = 0
    vy = 0