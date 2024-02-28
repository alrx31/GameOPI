import random
def word_gen():
    with open("words.txt", "r", encoding="utf-8") as file:  # Specify the correct encoding for your file
        lines = file.readlines()

    words = [line.strip().split('#') for line in lines]

    r = get_random(words)
    return words[r]


def get_random(a):
    return random.randint(0,len(a) - 1)


def baraban():
    baraban = []
    with open("baraban.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    baraban = [line.strip() for line in lines]
    return baraban

def result(pl1, pl2, pl3, word):
    # max_result = max(
    #     pl1['count'],
    #     pl2['count'],
    #     pl3['count'],
    # )

    # if max_result == pl1['count']:
    #     print("The Winner is :" + pl1['name'] + " with result: " + str(max_result) + "\nIn th word: "+ word)

    # if max_result == pl2['count']:
    #     print("The Winner is :" + pl2['name'] + " with result: " + str(max_result) + "\nIn th word: "+ word)

    # if max_result == pl3['count']:
    #     print("The Winner is :" + pl3['name'] + " with result: " + str(max_result) + "\nIn th word: "+ word)
    print(f"баллы игрока 1: {pl1['count']}")
    print(f"баллы игрока 2: {pl2['count']}")
    print(f"баллы игрока 3: {pl3['count']}")
