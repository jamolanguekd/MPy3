import pyglet
import random
from pyglet.window import mouse

window = pyglet.window.Window(1024, 768, resizable=True)

MPy3 = pyglet.text.Label('MPy3',
                         font_name='Arial',
                         font_size=70,
                         x=20, y=window.height,
                         anchor_x='left', anchor_y='top')

choose = pyglet.text.Label('CHOOSE AN ALBUM',
                           font_name='Times New Roman',
                           font_size=48,
                           x=window.width // 2, y=window.height - 100,
                           anchor_x='center', anchor_y='top')

name = pyglet.text.Label('',
                         font_name='Arial',
                         font_size=32,
                         x=window.width // 2, y=270,
                         anchor_x='center', anchor_y='bottom')

album = pyglet.image.load('yellow.png')
album.width = 150
album.height = 150

one = pyglet.image.load('red.png')
one.width = 150
one.height = 150

two = pyglet.image.load('blue.png')
two.width = 150
two.height = 150

c = [one, two, album, album, two, one]

x = 0
y = 85
batch = pyglet.graphics.Batch()
albums = []
albums2 = []

for i in range(3):
    x += 210
    albums.append(pyglet.sprite.Sprite(c[i + 3], x, y, batch=batch))
    albums2.append(pyglet.sprite.Sprite(c[i], x, y + 250, batch=batch))


@window.event
def on_mouse_motion(x, y, button, modifiers):
    if x >= 210 and x < 361 and y >= 330 and y < 481:
        name.text = 'one'
    if x >= 420 and x < 571 and y >= 330 and y < 481:
        name.text = 'two'
    if x >= 630 and x < 781 and y >= 330 and y < 481:
        name.text = 'three'
    if x >= 210 and x < 361 and y >= 85 and y < 230:
        name.text = 'four'
    if x >= 420 and x < 571 and y >= 85 and y < 230:
        name.text = 'five'
    if x >= 630 and x < 781 and y >= 85 and y < 230:
        name.text = 'six'


@window.event
def on_draw():
    window.clear()
    batch.draw()
    MPy3.draw()
    choose.draw()
    name.draw()


pyglet.app.run()
