from pygame import *
from random import randint, choice 

init()
font.init()
mixer.init()

display.set_caption("Перега Сират Радик мм ее")
window = display.set_mode((900,600))
clock = time.Clock()
ELEMENTS = ['Q', 'W', 'E']
SPELLS = {
    'QQQ': ['Cold Snap','images/Cold snap.png'],
    'WWW': ['EMP','images/EMP.png'],
    'EEE': ['Sun Strike','images/Sun strike.png'],
    'QWE': ['Deafening Blast','images/deafeaning blast.png'],
    'QWW': ['Tornado','images/Tornado.png'],
    'QEE': ['Forge Spirit','images/forge spirit1.png'],
    'WQE': ['Chaos Meteor','images/Chaos meteor.png'],
    'QQE': ['Ice Wall','images/ice wall.png'],
    'WWE': ['Alacrity','images/Alacrity.png'],
    'QQW': ['Ghost Walk','images/Ghost walk.png']
}
FONTNAME = "Marvel-Bold.ttf"

class Label(sprite.Sprite):
    def __init__(self, text, x, y, fontsize=30, color=(255, 255, 255) , font_name=FONTNAME):
        super().__init__()
        self.color = color
        self.font = font.Font(FONTNAME, fontsize)
        self.image = self.font.render(text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y  = y
    
    def set_text(self, new_text, color=(255, 255, 255)):
        self.image = self.font.render(new_text, True, color) 

class Spell(sprite.Sprite):
    def __init__(image,text,width,height,x,y):
        super().__init__()
        self.image = transform.scale(sprite_image,(height,height))
        self.text = Label(text,x+height+20,y,fontsize=30)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self,window):
        window.blit(self.image, (self.rect.x, self.rect.y))
        window.blit(self.text.image, (self.text.rect.x, self.text.rect.y))


ColdSnap = Spell('images/Cold snap.png','Cold Snap', 50, 50, 750, 50)

finish = False 
run = True
while run:
    window.fill((0,0,0))
    for e in event.get():
        if e.type == QUIT:
            run = False
 
    display.update()
    clock.tick(60)


