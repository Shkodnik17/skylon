import pgzrun
import random
import time
WIDTH = 770
HEIGHT = 530
mode = 'menu'
heals = 4
rockets = []

space = Actor('space')
ship = Actor('ship')
skin1 = Actor('skin1',(100,300))
skin2 = Actor('skin2',(333,300))
skin3 = Actor('skin3',(516,300))
skin4 = Actor('ship',(699,300))
buttons = Actor('button',(400,335))



enemies = []
ship.pos = (385,490)
for i in range(5):
    x = random.randint(0, 770)
    y = random.randint(-100,0)
    enemy = Actor('enemy')
    enemy.speed = random.randint(1, 4)
    enemy.pos = (x,y)
    enemies.append(enemy)


def draw():
    global mode
    if mode == 'menu':
        space.draw()
        screen.draw.text('Выберите корабль', topleft=(190,150 ), color="white", fontsize=60)
        skin1.draw()
        skin2.draw()
        skin3.draw()
        skin4.draw()


    if mode == 'end':
        space.draw()
        screen.draw.text('GAME OVER', topleft=(230, 190), color="white",fontsize=80)
        buttons.draw()




    if mode == 'game':
        space.draw()
        for i in range(len(rockets)):
            rockets[i].draw()

        screen.draw.text('Осталось жизней: {} '.format(heals), topleft=(20, 20), color="red", fontsize=35)
        ship.draw()
        for i in range(len(enemies)):
            enemies[i].draw()

def on_mouse_move(pos):
    ship.pos = pos


def enemy_ship():
    for i in range(len(enemies)):
        if enemies[i].y < 600:
            enemies[i].y = enemies[i].y + enemies[i].speed
        else:
            enemies.pop(i)
            new_enemy()

def new_enemy():
    x = random.randint(0, 770)
    y = random.randint(-100, 0)
    enemy = Actor('enemy')
    enemy.speed = random.randint(1, 4)
    enemy.pos = (x, y)
    enemies.append(enemy)


def collisions():
    global heals
    global mode
    for i in range(len(enemies)):
     if  ship.colliderect(enemies[i]):
         heals = heals - 1
         enemies.pop(i)
         new_enemy()

      


    if heals == 0:
        mode = 'end'







def update(dt):
    if mode == 'game':
        enemy_ship()
        collisions()
        for i in range(len(rockets)):
            if rockets[i].y < 0:
                rockets.pop(i)
                break
            else:
                rockets[i].y = rockets[i].y - 10






        if keyboard.k_1:
            ship.image = 'ship'
        if keyboard.k_2:
            ship.image = 'skin1'
        if keyboard.k_3:
            ship.image = 'skin2'
        if keyboard.k_4:
            ship.image = 'skin3'


def on_mouse_down(button, pos):
    global mode,ship
    global buttons
    global heals
    if mode == 'game' and mouse.LEFT:
        rocket = Actor('rocket')
        rocket.pos = ship.pos
        rockets.append(rocket)


    if mode == 'menu' and skin1.collidepoint(pos):
        ship.image = "skin1"
        mode = 'game'
    if mode == 'menu' and skin2.collidepoint(pos):
        ship.image = "skin2"
        mode = 'game'
    if mode == 'menu' and skin3.collidepoint(pos):
        ship.image = "skin3"
        mode = 'game'
    if mode == 'menu' and skin4.collidepoint(pos):
        ship.image = "ship"
        mode = 'game'
    if mode == 'end' and buttons.collidepoint(pos):
        mode = 'menu'
        heals = heals + 3































pgzrun.go()