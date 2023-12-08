import config


def game():
    pl1_count = 0
    pl2_count = 0
    pl3_count = 0


    word = config.word_gen()[0] # слово
    res = word.split('')   # массив  - - - 
    for i in range(len(res)):
        res[i] = '_'
    while res.join() != word.join() :
        print(1)
    else:
        config.result(pl1_count,pl2_count,pl3_count,word)