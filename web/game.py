import config
import time

def game():
    players = {
        'pl1': {
            'count': 0,
            'name': "Player 1",
        },
        'pl2': {
            'count': 0,
            'name': "Player 2",
        },
        'pl3': {
            'count': 0,
            'name': "Player 3",
        },
    }

    baraban = config.baraban()  # массив баррабана
    getting_word = config.word_gen() # получение слова
    word = getting_word[0].upper()  # слово
    describe = getting_word[1] # описание слова
    word_list = list(word)
    res = list(word_list)     # массив  - - -
    entered_words = []  #array of entered letter




    for i in range(len(res)):
        res[i] = '_'


    print(describe,'\n',res)
    players_flag = 1
    
    while ''.join(res) != word:
        print(f"Ход игрока номер {3 if players_flag % 3 == 0 else players_flag % 3}\n")

        baraban_value = int(baraban[config.get_random(baraban)])

        
        if baraban_value == -1:
            print("вы пропускаете ход")
            time.sleep(1)
            players_flag+=1
            continue

        if baraban_value == 0:
            print("Сектотр + на барабане")
            while True:
                input_letter_num = input("введите номер буквы: ").strip()
                if input_letter_num.isdigit():
                    input_letter_num = int(input_letter_num)
                    if input_letter_num>0 and input_letter_num <= len(res):
                        input_letter = word_list[input_letter_num-1]
                        break
                
                                        
            for i in range(len(res)):
                if input_letter == word_list[i]:
                    res[i] = word_list[i]
                    entered_words.append(word_list[i])
            print(res)
            continue


        print(baraban_value)
        while True:
            input_letter = input("Введите букву: ").upper()
            if not input_letter in entered_words:
                break
        
        game_flag = 0
        entered_words.append(input_letter)
        for i in range(len(res)):

            if(input_letter == word_list[i]):
                res[i] = word_list[i]
                game_flag+=1

        if(baraban_value > 100):
            players[('pl' +str(players_flag % 3)) if  players_flag%3!=0 else 'pl3']['count'] += game_flag*baraban_value

        print(res)
        players_flag += 1 if game_flag == 0 else 0
        print("\n")
        print("________________________\n")
        print()
        game_flag = 0
    else:
        print(f"победил игрок номер {3 if players_flag % 3 == 0 else players_flag % 3}\n")
        config.result(
            players['pl1'],
            players['pl2'],
            players['pl3'],
            word
        )







game()
