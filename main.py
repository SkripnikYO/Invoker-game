from pygame import *
from random import choice

init()
font.init()
mixer.init()

FONTNAME = "Marvel-Bold.ttf"

display.set_caption("Перега Сират Радик мм ее")
window = display.set_mode((1000, 700))
clock = time.Clock()

ELEMENTS = {
    'q': transform.scale(image.load('images/quas.png'), (70, 70)),
    'w': transform.scale(image.load('images/wex.png'), (70, 70)),
    'e': transform.scale(image.load('images/exort.png'), (70, 70)),
    'ntg': transform.scale(image.load('images/ntg.png'), (70, 70))
}

ORIGINAL_SPELLS = {
    'QQQ': ['Cold Snap', 'images/Cold snap.png'],
    'WWW': ['EMP', 'images/EMP.png'],
    'EEE': ['Sun Strike', 'images/Sun strike.png'],
    'EQW': ['Deafening Blast', 'images/deafeaning blast.png'],
    'QWW': ['Tornado', 'images/Tornado.png'],
    'EEQ': ['Forge Spirit', 'images/forge spirit1.png'],
    'EEW': ['Chaos Meteor', 'images/Chaos meteor.png'],
    'EQQ': ['Ice Wall', 'images/ice wall.png'],
    'EWW': ['Alacrity', 'images/Alacrity.png'],
    'QQW': ['Ghost Walk', 'images/Ghost walk.png']
}

SPELLS = ORIGINAL_SPELLS.copy()

class Label(sprite.Sprite):
    def __init__(self, text, x, y, fontsize=30, color=(255, 255, 255), font_name=FONTNAME):
        super().__init__()
        self.color = color
        self.font = font.Font(font_name, fontsize)
        self.image = self.font.render(text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_text(self, new_text, color=(255, 255, 255)):
        self.image = self.font.render(new_text, True, color)

class Spell(sprite.Sprite):
    def __init__(self, sprite_image, text, width, height, x, y):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (height, height))
        self.text = Label(text, x + height + 20, y, fontsize=30)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = text

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
        window.blit(self.text.image, (self.text.rect.x, self.text.rect.y))

class CardSpell(Spell):
    def __init__(self, sprite_image, text, width, height, x, y):
        super().__init__(sprite_image, text, width, height, x, y)
        self.text = Label(text, x + 35, y, fontsize=25)

# Интерфейс
spells = sprite.Group()
spells.add(Spell('images/Cold snap.png', 'Cold Snap - QQQ', 50, 50, 700, 0))
spells.add(Spell('images/EMP.png', 'EMP - WWW', 50, 50, 700, 55))
spells.add(Spell('images/Sun strike.png', 'Sun Strike - EEE', 50, 50, 700, 110))
spells.add(Spell('images/Tornado.png', 'Tornado - WWQ', 50, 50, 700, 165))
spells.add(Spell('images/forge spirit1.png', 'Forge Spirit - EEQ', 50, 50, 700, 220))
spells.add(Spell('images/ice wall.png', 'Ice Wall - QQE', 50, 50, 700, 275))
spells.add(Spell('images/Alacrity.png', 'Alacrity - WWE', 50, 50, 700, 330))
spells.add(Spell('images/Ghost walk.png', 'Ghost Walk - QQW', 50, 50, 700, 385))
spells.add(Spell('images/Chaos meteor.png', 'Chaos Meteor - EEW', 50, 50, 700, 440))
spells.add(Spell('images/deafeaning blast.png', 'Deafening Blast - QWE', 50, 50, 700, 495))

controls = sprite.Group()
controls.add(Spell('images/quas.png', 'Quas - Q', 75, 75, 0, 0))
controls.add(Spell('images/wex.png', 'Wex - W', 75, 75, 0, 80))
controls.add(Spell('images/exort.png', 'Exort - E', 75, 75, 0, 160))
controls.add(Spell('images/ntg.png', 'Spell 1 - D', 75, 75, 0, 240))
controls.add(Spell('images/ntg.png', 'Spell 2 - F', 75, 75, 0, 320))
controls.add(Spell('images/invoke.png', 'Invoke - R', 75, 75, 0, 400))
controls.add(Spell('images/invoker.png', '', 400, 250, 300, 0))

card_spells = sprite.Group()
card_spells.add(CardSpell('images/quas.png', 'Q', 100, 100, 0, 600))
card_spells.add(CardSpell('images/wex.png', 'W', 100, 100, 110, 600))
card_spells.add(CardSpell('images/exort.png', 'E', 100, 100, 220, 600))
card_spells.add(CardSpell('images/ntg.png', 'D', 100, 100, 330, 600))
card_spells.add(CardSpell('images/ntg.png', 'F', 100, 100, 440, 600))
card_spells.add(CardSpell('images/invoke.png', 'R', 100, 100, 550, 600))

btns_spell = sprite.Group()
spell_1 = Spell('images/ntg.png', '', 70, 70, 330, 500)
spell_2 = Spell('images/ntg.png', '', 70, 70, 430, 500)
spell_3 = Spell('images/ntg.png', '', 70, 70, 530, 500)
btns_spell.add(spell_1, spell_2, spell_3)

curent_spell = choice(list(SPELLS.keys()))
spellcard = Spell(SPELLS[curent_spell][1], SPELLS[curent_spell][0], 100, 100, 350, 300)
curentbuttons = ""

start_ticks = time.get_ticks()
timer_font = font.Font(FONTNAME, 40)

game_over = False
restart_font = font.Font(FONTNAME, 50)
restart_button = Rect(400, 400, 200, 80)

final_time = 0  # Для хранения времени когда игра закончилась

run = True
while run:
    window.fill((0, 0, 0))
    for e in event.get():
        if e.type == QUIT:
            run = False

        if not game_over:
            if e.type == KEYDOWN:
                if e.key in [K_q, K_w, K_e, K_d, K_f]:
                    pressedkey = key.name(e.key)
                    curentbuttons += pressedkey
                    if len(curentbuttons) > 3:
                        curentbuttons = curentbuttons[1:]

                    spell_1.image = ELEMENTS[curentbuttons[0]]
                    spell_2.image = ELEMENTS[curentbuttons[1]] if len(curentbuttons) >= 2 else ELEMENTS['ntg']
                    spell_3.image = ELEMENTS[curentbuttons[2]] if len(curentbuttons) >= 3 else ELEMENTS['ntg']

                if e.key == K_r:
                    sorted_btns = ''.join(sorted(curentbuttons.upper()))
                    check = SPELLS.get(sorted_btns)
                    if check:
                        del SPELLS[curent_spell]
                        if not SPELLS:
                            game_over = True
                            final_time = (time.get_ticks() - start_ticks) // 1000
                        else:
                            curent_spell = choice(list(SPELLS.keys()))
                            spellcard = Spell(SPELLS[curent_spell][1], SPELLS[curent_spell][0], 100, 100, 350, 300)
                            curentbuttons = ""
                            spell_1.image = ELEMENTS['ntg']
                            spell_2.image = ELEMENTS['ntg']
                            spell_3.image = ELEMENTS['ntg']

        elif e.type == MOUSEBUTTONDOWN:
            if restart_button.collidepoint(e.pos):
                SPELLS = ORIGINAL_SPELLS.copy()
                curent_spell = choice(list(SPELLS.keys()))
                spellcard = Spell(SPELLS[curent_spell][1], SPELLS[curent_spell][0], 100, 100, 350, 300)
                curentbuttons = ""
                spell_1.image = ELEMENTS['ntg']
                spell_2.image = ELEMENTS['ntg']
                spell_3.image = ELEMENTS['ntg']
                start_ticks = time.get_ticks()
                game_over = False
                final_time = 0

    # Отрисовка
    for spell in spells:
        spell.draw(window)
    for control in controls:
        control.draw(window)
    for card_spell in card_spells:
        card_spell.draw(window)
    spellcard.draw(window)
    btns_spell.draw(window)

    # Таймер
    if not game_over:
        seconds = (time.get_ticks() - start_ticks) // 1000
    else:
        seconds = final_time  # Показываем время, зафиксированное при окончании

    timer_text = timer_font.render(f"Time: {seconds}s", True, (255, 255, 255))
    window.blit(timer_text, (800, 650))

    # Кнопка рестарта
    if game_over:
        draw.rect(window, (50, 100, 200), restart_button)
        text = restart_font.render("RESTART", True, (255, 255, 255))
        window.blit(text, (restart_button.x + 25, restart_button.y + 20))

    display.update()
    clock.tick(60)