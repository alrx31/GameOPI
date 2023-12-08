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
    word = config.word_gen()[0]  # слово
    res = list(word)  # массив  - - -

    for i in range(len(res)):
        res[i] = '_'

    while ''.join(res) != word:
        print(1)
    else:
        config.result(
            players['pl1'],
            players['pl2'],
            players['pl3'],
            word
        )

game()
