import config

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

    baraban = config.baraban()


    # config.result(
    #     players['pl1'],
    #     players['pl2'],
    #     players['pl3'],
    #     "wert"
    # )


    getting_word = config.word_gen() # получение слова
    word = getting_word[0].upper()  # слово
    describe = getting_word[1] # описание слова
    word_list = list(word)
    res = list(word_list)     # массив  - - -




    for i in range(len(res)):
        res[i] = '_'


    config.result(
        players['pl1'],
        players['pl2'],
        players['pl3'],
        word
    )

    print(describe,'\n',res)
    players_flag = 1
    while ''.join(res) != word:
        baraban_value = int(baraban[config.get_random(baraban)])
        print(baraban_value)
        input_letter = input("Введите букву: ").upper()
        flag = 0
        for i in range(len(res)):
            if(input_letter == word_list[i]):
                res[i] = word_list[i]
                flag+=1
        if(baraban_value > 100):
            players[('pl' +str(players_flag % 3)) if  players_flag%3!=0 else 'pl3']['count'] += flag*baraban_value
        print(res)
        flag = 0
        players_flag += 1
        print("\n")
    else:
        config.result(
            players['pl1'],
            players['pl2'],
            players['pl3'],
            word
        )







game()
