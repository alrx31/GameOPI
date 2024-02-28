import pygame
import random
import time
import sys

all_obj = []
class obj:
    global all_obj
    def __init__(self, name, color, x, y, width, height, border = 0, text = None):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border = border
        self.text = text
        all_obj.append(self)
    def draw(self):
        cen_x, cen_y = self.x - (self.width // 2), self.y - (self.height // 2)
        r = pygame.Rect(cen_x, cen_y, self.width, self.height)
        pygame.draw.rect(display, self.color, r, self.border)
        if self.text != None:
            txt = self.text[1].render(self.text[0], True, self.text[2])
            display.blit(txt, (self.x - (txt.get_width() // 2), self.y - (txt.get_height() // 2)))
    def pressed(self, x, y):
        if (self.x - (self.width // 2) < x < self.x + (self.width // 2) and
            self.y - (self.height // 2) < y < self.y + (self.height // 2)):
            return True
        
class text:
    def __init__(self, txt, color, font, x, y):
        self.txt = txt
        self.color = color
        self.font = font
        self.x = x
        self.y = y
    def draw(self):
        txt = self.font.render(self.txt, True, self.color)
        display.blit(txt, (self.x - (txt.get_width() // 2), self.y - (txt.get_height() // 2)))
      


pygame.init()
pygame.display.set_caption("Поле чудес")
# ico = pygame.image.load("sprites/icon.ico")
# pygame.display.set_icon(ico)
clock = pygame.time.Clock()

colors = {
    "blue" : (51, 51, 255),
    "d_blue" : (0, 0, 204),
    "back_blue" : (0, 0, 153),
    "white" : (255, 255, 255),
    "black" : (0, 0, 0),
    "grey" : (192, 192, 192),
    "yellow" : (255, 255, 0),
    "purple" : (76, 0, 153),
    "d_purple" : (51, 0, 102),
    "red" : (255, 0, 0)
}

b_font = pygame.font.Font(size=80)
s_font = pygame.font.Font(size=40)
n_font = pygame.font.Font(size=35)
vs_font = pygame.font.Font(size=30)

display = pygame.display.set_mode((800, 600))

background = pygame.Rect(0, 0, 800, 600)

def pushint():
    return (random.randint(1, 10) + 50)

def get_word():
    f = open("words.txt", "r", encoding="UTF-8")
    lst = f.readlines()
    word, txt = lst[random.randint(0, len(lst) - 1)].strip().split("#")
    f.close()
    return (word.lower(), txt)

def get_roll():
    f = open("baraban.txt", "r", encoding="UTF-8")
    roll = list(map(int, f.read().split("\n")))
    f.close()
    return roll

def new_roll(x):
    global static_roll
    lst = []
    for i in range(len(static_roll)):
        j = (i + x + (len(static_roll) // 2)) % len(static_roll) + 1
        lst.append(j - 1)
    n_roll = []
    for i in range(len(static_roll)):
        j = lst[i]
        n_roll.append(static_roll[j])
    return n_roll

def in_word(l):
    global word
    ans = []
    for i in range(len(word)):
        if l == word[i]:
            ans.append(i)
    return ans


##### values ######
static_roll = get_roll()
current_stage = "menu"
word, explain = str(), str()
word_status = []
background = pygame.image.load("sprites/back.jpg")
keys = sorted(['ё', 'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ',
                'з', 'х', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о',
                'л', 'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю'])
keys_status = [0 for _ in range(len(keys))]
status = "wait"
start_pos = random.randint(1, len(static_roll))
rounds = pushint()
current_payer = 0
points = [0, 0, 0]
players_status = [0, 0, 0]
entering_word = ""


##### menu stage #######
def menu():
    global current_stage, word, explain, word_status, status
    display.blit(background, (0, 0))
    text("Поле чудес", colors["yellow"], b_font, 400, 150).draw()
    buttonPlay = obj("play", colors["purple"], 400, 300, 200, 75, text = ("Играть", s_font, colors["white"]))
    buttonPlay.draw()
    borderPlay = obj("play_border", colors["d_purple"], 400, 300, 200, 75, 5)
    borderPlay.draw()
    buttonRules = obj("rules", colors["purple"], 400, 375, 150, 50, text=("Правила", n_font, colors["white"]))
    buttonRules.draw()
    borderRules = obj("rules_border", colors["d_purple"], 400, 375, 150, 50, 5)
    borderRules.draw()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            for el in all_obj:
                if el.pressed(x, y):
                    if el.name == "play":
                        current_stage = "game"
                        status = "wait"
                        word, explain = get_word()
                        word_status = [0 for _ in range(len(word))]
                    if el.name == "rules":
                        current_stage = "rules"
                        print(2)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    all_obj.clear()
    pygame.display.flip()

#### rules ####
def rules():
    print(1)


##### game stage ######
def game():
    global current_stage, start_pos, rounds, status, current_payer, word, word_status, points, players_status, entering_word
    if sum(players_status) == 3 or sum(word_status) == len(word):
        current_stage = "game_over"
        return
    if players_status[current_payer]:
        current_payer = (current_payer + 1) % 3
        return
    current_sector = static_roll[start_pos - 1]
    display.blit(background, (0, 0))
    roll_back = obj("roll_back", colors["back_blue"], 400, 300, 800, 75)
    roll_back.draw()

    

    #### label #####
    for i in range(len(word)):
        x, y = 37 + (i * 75) - (len(word) * 75 // 2) + 400, 125
        letter_text = word[i] if word_status[i] else " "
        letter = obj("letter " + str(i), colors["white"], x, y, 50, 50, text=(letter_text, s_font, colors["black"]))
        letter.draw()
        letter_border = obj("letter_b", colors["grey"], x, y, 50, 50, 3)
        letter_border.draw()
    text(explain, colors["white"], n_font, 400, 175).draw()
    text(f"Баллы: {points[current_payer]}", colors["white"], n_font, 400, 225).draw()

    ### roll ###
    roll = new_roll(start_pos)
    for i in range(len(roll)):
        x, y = ((i + 1) * 75) + 400 - 975, 300
        if roll[i] == -1:
            sector_text = "-"
        elif roll[i] == 0:
            sector_text = "+"
        else:
            sector_text = str(roll[i])
        sector = obj(sector_text, colors["blue"], x, y, 60, 60, text = (sector_text, n_font, colors["white"]))
        sector.draw()
        sector_border = obj(sector_text + "_b", colors["d_blue"], x, y, 60, 60, 5)
        sector_border.draw()
    arrow = obj("arrow", colors["white"], 400, 325, 2, 25)
    arrow.draw()

    ### keys ####
    if status == "all_word":
        line = obj("line", colors["white"], 400, 470, 300, 3)
        line.draw()
        back = obj("back", colors["purple"], 400, 525, 200, 50, text=("Назад", s_font, colors["white"]))
        back.draw()
        wrd = text(entering_word, colors["white"], s_font, 400, 450)
        wrd.draw()
        obj("back_b", colors["d_purple"], 400, 525, 200, 50, 5).draw()
    else:
        keys_back = obj("keys_back", colors["purple"], 400, 500, 550, 150)
        keys_back.draw()
        obj("keys_back_b", colors["d_purple"], 400, 500, 550, 150, 5).draw()
        for i in range(11):
            x, y = 25 + (i * 50) - (11 * 50 // 2) + 400, 450
            col = colors["red"] if keys_status[i] else colors["white"]
            key = obj("key " + str(i), col, x, y, 25, 25, text = (keys[i], vs_font, colors["black"]))
            key.draw()
            obj("key_b", colors["grey"], x, y, 25, 25, 3).draw()
        for i in range(11, 22):
            x, y = 25 + ((i - 11) * 50) - (11 * 50 // 2) + 400, 500
            col = colors["red"] if keys_status[i] else colors["white"]
            key = obj("key " + str(i), col, x, y, 25, 25, text = (keys[i], vs_font, colors["black"]))
            key.draw()
            obj("key_b", colors["grey"], x, y, 25, 25, 3).draw()
        for i in range(22, 32):
            x, y = 25 + ((i - 22) * 50) - (10 * 50 // 2) + 400, 550
            col = colors["red"] if keys_status[i] else colors["white"]
            key = obj("key " + str(i), col, x, y, 25, 25, text = (keys[i], vs_font, colors["black"]))
            key.draw()
            obj("key_b", colors["grey"], x, y, 25, 25, 3).draw()

    #### actions ####
    pull = obj("pull", colors["purple"], 250, 375, 250, 50, text = ("Вращать барабан", n_font, colors["white"]))
    pull.draw()
    pull_b = obj("pull_b", colors["d_purple"], 250, 375, 250, 50, 5)
    pull_b.draw()
    all_word = obj("all_word", colors["purple"], 550, 375, 250, 50, text = ("Сказать слово", n_font, colors["white"]))
    all_word.draw()
    all_word_b = obj("all_word_b", colors["d_purple"], 550, 375, 250, 50, 5)
    all_word_b.draw()


    ### what to do #####
    if status == "wait" or status == "roll":
        wtd = text(f"Игрок {current_payer + 1}, вращайте барабан", colors["white"], s_font, 400, 50)
        wtd.draw()
    if status == "skip":
        wtd = text(f"Игрок {current_payer + 1} пропускает ход", colors["white"], s_font, 400, 50)
        wtd.draw()
        pygame.display.flip()
        time.sleep(2)
        status = "wait"
    if status == "open":
        wtd = text(f"Игрок {current_payer + 1}, открывайте букву", colors["white"], s_font, 400, 50)
        wtd.draw()
    if status == "choose":
        wtd = text(f"Игрок {current_payer + 1}, выбирайте букву", colors["white"], s_font, 400, 50)
        wtd.draw()
    if status == "all_word":
        wtd = text(f"Игрок {current_payer + 1}, найзывайте слово", colors["white"], s_font, 400, 50)
        wtd.draw()
    if status == "wrong":
        wtd = text(f"Не верно!", colors["white"], s_font, 400, 50)
        wtd.draw()
        pygame.display.flip()
        time.sleep(2)
        status = "wait"


    if status == "roll":
        clock.tick(rounds * 0.75)
        start_pos = (start_pos + 1) % (len(static_roll) + 1)
        start_pos = start_pos + 1 if start_pos == 0 else start_pos
        rounds -= 1
    if rounds == 0 and status == "roll":
        current_sector = static_roll[start_pos - 1]
        if current_sector == -1:
            status = "skip"
            current_payer = (current_payer + 1) % 3
        elif current_sector == 0:
            status = "open"
        else:
            status = "choose"
        print(current_sector)
        clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for el in all_obj:
                if not el.pressed(x, y):
                    continue
                if status == "wait":
                    if el.name == "pull":
                        rounds = pushint()
                        status = "roll"
                    if el.name == "all_word":
                        status = "all_word"
                if status == "choose":
                    if el.name.split()[0] == "key":
                        ind = int(el.name.split()[1])
                        if keys_status[ind] == 0:
                            keys_status[ind] = 1
                            ans = in_word(keys[ind])
                            if not ans:
                                status = "wrong"
                                current_payer = (current_payer + 1) % 3
                            else:
                                status = "wait"
                                for i in range(len(ans)):
                                    word_status[ans[i]] = 1
                                    points[current_payer] += int(current_sector)
                if status == "open":
                    if el.name.split()[0] == "letter":
                        ind = int(el.name.split()[1])
                        if word_status[ind] == 0:
                            ans = in_word(word[ind])
                            status = "wait"
                            keys_status[keys.index(word[ind])] = 1
                            for i in range(len(ans)):
                                word_status[ans[i]] = 1
                if status == "all_word":
                    if el.name == "back":
                        status = "wait"
        if event.type == pygame.KEYDOWN:
            if status == "all_word":
                k = event.dict['unicode'].lower()
                if k == '\r':
                    if entering_word:
                        if word == entering_word:
                            points[current_payer] += ((len(word) - sum(word_status)) * 300)
                            word_status = [1 for _ in range(len(word))]
                        else:
                            players_status[current_payer] = 1
                            entering_word = ""
                            status = "wait"
                elif k in keys:
                    entering_word += k
                elif k == '\x08':
                    entering_word = entering_word[:-1:]
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    all_obj.clear()
    pygame.display.flip()


#### game over #####
def game_over():
    global all_obj, current_stage, players_status, status, word, explain, word_status, points, keys_status, start_pos, rounds, current_payer, entering_word
    display.blit(background, (0, 0))
    if sum(players_status) == 3:
        result = text("Вы проиграли!", colors["white"], b_font, 400, 100)
        result.draw()
    else:
        result = text(f"Победил игрок {current_payer + 1}!", colors["white"], b_font, 400, 100)
        result.draw()
    text(f"Слово: {word}", colors["white"], s_font, 400, 200).draw()

    ### points ###
    text("Очки:", colors["white"], s_font, 400, 250).draw()
    text("Игрок 1", colors["white"], s_font, 200, 300).draw()
    text(f"{points[0]}", colors["white"], s_font, 200, 350).draw()
    text("Игрок 2", colors["white"], s_font, 400, 300).draw()
    text(f"{points[1]}", colors["white"], s_font, 400, 350).draw()
    text("Игрок 3", colors["white"], s_font, 600, 300).draw()
    text(f"{points[2]}", colors["white"], s_font, 600, 350).draw()

    ### restart ###
    restart = obj("restart", colors["purple"], 400, 500, 300, 50, text=("Начать заново", s_font, colors["white"]))
    restart.draw()
    obj("restart_b", colors["d_purple"], 400, 500, 300, 50, 5).draw()


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for el in all_obj:
                if el.pressed(x, y):
                    current_stage = "game"
                    status = "wait"
                    word, explain = get_word()
                    word_status = [0 for _ in range(len(word))]
                    points = [0, 0, 0]
                    players_status = [0, 0, 0]
                    keys_status = [0 for _ in range(len(keys))]
                    start_pos = random.randint(1, len(static_roll))
                    rounds = pushint()
                    current_payer = 0
                    entering_word = ""
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    all_obj.clear()
    pygame.display.flip()


while True:
    if current_stage == "menu":
        menu()
        continue
    if current_stage == "game":
        game()
        continue
    if current_stage == "game_over":
        game_over()
        continue
    pygame.quit()
    sys.exit()
