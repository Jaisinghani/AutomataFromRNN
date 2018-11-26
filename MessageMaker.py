import random

def makeMessage(wordList, length):
    message = ""
    for i in range(0, length):
        message += ' ' + str(random.choice(wordList))
    return message