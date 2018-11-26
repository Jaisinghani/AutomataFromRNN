import time
from memory_profiler import profile
# check a sentence(a list of words) return if its a rotation cyphered message

def rtCyCdecode(message, alphabet):  # Rotation cypher decode

    messageList = message.split()
    convertedMsgList = []

    for i in range(1, len(alphabet)):
        convertedWordList = []
        for word in messageList:
            charList = list(word.lower())    # split a word to letters
            convertedMsg = ""
            for letter in charList:
                lIndex = alphabet.index(letter)
                newLIndex = (lIndex + i) % len(alphabet)
                convertedMsg += alphabet[newLIndex]
            convertedWordList.append(convertedMsg)
        convertedMsgList.append(convertedWordList)

    return convertedMsgList


#@profile(precision=8)
def checkRtCy(message, alphabet, learner):
    convertedMsgList = rtCyCdecode(message, alphabet)
    maxMatch = float('-inf')
    matchList = []
    for list in convertedMsgList:
        realWordList = []
        for word in list:
            if learner.classify_word(word):
                realWordList.append(word)

        if len(realWordList) >= maxMatch:
            matchList.append(realWordList)
            maxMatch = len(realWordList)

    msgList = []
    for match in matchList:
        msg = listToString(match)
        msgList.append(msg)
    accuracy = '{percent:.2%}'.format(percent= maxMatch/ len(convertedMsgList[0]))

    return (accuracy, msgList)


def listToString(list):
    sentence = ''
    for word in list:
        sentence += ' ' + str(word)

    return sentence


