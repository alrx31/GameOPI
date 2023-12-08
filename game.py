import config


def game():
    players = {
        "pl1" : {
            "count": 0,
            "name": "Player 1",
        },
        "pl2" : {
            "count": 0,
            "name": "Player 2",
        },
        "pl3" : {
            "count": 0,
            "name": "Player 3",
        },
    }
    


    word = config.word_gen()[0] # слово
    res = word.split('')   # массив  - - - 
    
    for i in range(len(res)):
        res[i] = '_'
    while res.join() != word.join() :
        print(1)
    else:
        config.result(
            players.pl1,
            players.pl2,
            players.pl3,
            word
            )