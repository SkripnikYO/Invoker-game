from pygame import *
from random import randint, choice 

init()
font.init()
mixer.init()

display.set_caption("Перега Сират Радик мм ее")
window = display.set_mode((1000,700))
clock = time.Clock()
ELEMENTS = ['Q', 'W', 'E']
SPELLS = {
    'QQQ': ['Cold Snap','images/Cold snap.png'],
    'WWW': ['EMP','images/EMP.png'],
    'EEE': ['Sun Strike','images/Sun strike.png'],
    'EQW': ['Deafening Blast','images/deafeaning blast.png'],
    'QWW': ['Tornado','images/Tornado.png'],
    'EEQ': ['Forge Spirit','images/forge spirit1.png'],
    'EEW': ['Chaos Meteor','images/Chaos meteor.png'],
    'EQQ': ['Ice Wall','images/ice wall.png'],
    'EWW': ['Alacrity','images/Alacrity.png'],
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
    def __init__(self,sprite_image,text,width,height,x,y):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image),(height,height))
        self.text = Label(text,x+height+20,y,fontsize=30)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = text

    def draw(self,window):
        window.blit(self.image, (self.rect.x, self.rect.y))
        window.blit(self.text.image, (self.text.rect.x, self.text.rect.y))

class CardSpell(Spell):
    def __init__(self,sprite_image,text,width,height,x,y):
        super().__init__(sprite_image,text,width,height,x,y)
        self.text = Label(text,x+35,y,fontsize=25)

spells = sprite.Group()
spells.add(Spell('images/Cold snap.png','Cold Snap', 50, 50, 750, 0))
spells.add(Spell('images/EMP.png','EMP', 50, 50, 750, 50))
spells.add(Spell('images/Sun strike.png','Sun Strike', 50, 50, 750, 100))
spells.add(Spell('images/Tornado.png','Tornado', 50, 50, 750, 150))
spells.add(Spell('images/forge spirit1.png','Forge Spirit', 50, 50, 750, 200))
spells.add(Spell('images/ice wall.png','Ice Wall', 50, 50, 750, 250))
spells.add(Spell('images/Alacrity.png','Alacrity', 50, 50, 750, 300))
spells.add(Spell('images/Ghost walk.png','Ghost Walk', 50, 50, 750, 350))
spells.add(Spell('images/Chaos meteor.png','Chaos Meteor', 50, 50, 750, 400))
spells.add(Spell('images/deafeaning blast.png','Deafening Blast', 50, 50, 750, 450))

controls =sprite.Group()
controls.add(Spell('images/quas.png','Quas - Q',50,50,100,0))
controls.add(Spell('images/wex.png','Wex - W',50,50,100,50))
controls.add(Spell('images/exort.png','Exort - E',50,50,100,100))
controls.add(Spell('images/ntg.png','Spell 1 - D',50,50,100,150))
controls.add(Spell('images/ntg.png','Spell 2 - F',50,50,100,200))
controls.add(Spell('images/invoke.png','Invoke - R',50,50,100,250))
controls.add(Spell('images/invoker.png','',250,250,375,0))


card_spells = sprite.Group()
card_spells.add(CardSpell('images/quas.png','Q',50,50,300,600))
card_spells.add(CardSpell('images/wex.png','W',50,50,350,600))
card_spells.add(CardSpell('images/exort.png','E',50,50,400,600))
card_spells.add(CardSpell('images/ntg.png','D',50,50,450,600))
card_spells.add(CardSpell('images/ntg.png','F',50,50,500,600))
card_spells.add(CardSpell('images/invoke.png','R',50,50,550,600))

curent_spell = choice(list(SPELLS.keys()))
spellcard = Spell(SPELLS[curent_spell][1], SPELLS[curent_spell][0], 100, 100, 350, 300)
curentbuttons = ""

finish = False 
run = True
while run:
    window.fill((0,0,0))
    for e in event.get():
        if e.type == KEYDOWN:
            pressedkey = key.name(e.key)
            curentbuttons+=pressedkey
            if len(curentbuttons)>=3:
                sorted_btns = sorted(curentbuttons.upper())
                sorted_btns = ''.join(sorted_btns)
                check = SPELLS.get(sorted_btns)
                print(curentbuttons)
                curentbuttons = ""
                
                if check:
                    del SPELLS[curent_spell]
                    print('Правильно')
                    curent_spell = choice(list(SPELLS.keys()))
                    spellcard = Spell(SPELLS[curent_spell][1], SPELLS[curent_spell][0], 100, 100, 350, 300)
                    curentbuttons = ""
                
        if e.type == QUIT:
            run = False
    for spell in spells:
        spell.draw(window)
    for control in controls:
        control.draw(window)
    for card_spell in card_spells:
        card_spell.draw(window)
    spellcard.draw(window)
    display.update()
    clock.tick(60)


