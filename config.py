import random

def word_gen():
    f = open("words.txt")
    words = []
    for line in f.readlines():
        words.append(line.split("#"))
    f.close()
    r = random.randint() % 50
    return  words[r]


def result(pl1,pl2,pl3,word){
    max_result = max(
        pl1.count,
        pl2.count,
        pl3.count,
    )

    if(max_result == pl1.count):
        print("The Winner is :" + pl1.name + " with result: " + max_result) 
    
    if(max_result == pl2.count):
        print("The Winner is :" + pl2.name + " with result: " + max_result)
    
    if(max_result == pl3.count):
        print("The Winner is :" + pl3.name + " with result: " + max_result)
}