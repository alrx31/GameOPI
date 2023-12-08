import config

def game():
    players = {
        'pl1': {
            'count': 2,
            'name': "Player 1",
        },
        'pl2': {
            'count': 3,
            'name': "Player 2",
        },
        'pl3': {
            'count': 4,
            'name': "Player 3",
        },
    }

    config.result(
        players['pl1'],
        players['pl2'],
        players['pl3'],
        "wert"
    )
    getting_word = config.word_gen() # получение слова
    word = getting_word[0]  # слово
    describe = getting_word[1] # описание слова
    res = list(word)  # массив  - - -

    for i in range(len(res)):
        res[i] = '_'
    p = 0
    # while ''.join(res) != word or p < 2:
    print(describe)
    while p<2:
        print(1)
        p+=1
    else:
        config.result(
            players['pl1'],
            players['pl2'],
            players['pl3'],
            word
        )

game()
