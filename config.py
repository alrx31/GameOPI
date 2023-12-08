import random

def word_gen():
    f = open("words.txt")
    words = []
    for line in f.readlines():
        words.append(line.split("#"))
    f.close()
    r = random.randint() % 50
    return  words[r]