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
    word = getting_word[0]  # слово
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

    print(describe)
    players_flag = 1
    while ''.join(res) != word:
        baraban_value = baraban[config.get_random(baraban)]
        input_letter = input("Введите букву: ")
        flag = 0
        for i in range(len(res)):
            if(input_letter == word_list[i]):
                res[i] = word_list[i]
                flag+=1
        players['pl' + str(players_flag % 3)]['count'] += flag*baraban_value

        flag = 0
        players_flag += 1
    else:
        config.result(
            players['pl1'],
            players['pl2'],
            players['pl3'],
            word
        )







game()
