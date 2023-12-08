import random
def word_gen():
    with open("words.txt", "r", encoding="utf-8") as file:  # Specify the correct encoding for your file
        lines = file.readlines()

    words = [line.strip().split('#') for line in lines]

    r = random.randint(0, len(words) - 1)
    return words[r]


def result(pl1, pl2, pl3, word):
    max_result = max(
        pl1['count'],
        pl2['count'],
        pl3['count'],
    )

    if max_result == pl1['count']:
        print("The Winner is :" + pl1['name'] + " with result: " + str(max_result) + "\nIn th word: "+ word)

    if max_result == pl2['count']:
        print("The Winner is :" + pl2['name'] + " with result: " + str(max_result) + "\nIn th word: "+ word)

    if max_result == pl3['count']:
        print("The Winner is :" + pl3['name'] + " with result: " + str(max_result) + "\nIn th word: "+ word)
