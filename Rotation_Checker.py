import time
from memory_profiler import profile
# check a sentence(a list of words) return if its a rotation cyphered message

def rtCyCdecode(messageList):  # Rotation cypher decode
    letterList = ['a', 'e', 'i', 'n', 'o', 's', 't']
    convertedMsgList = []

    for i in range(1, len(letterList)):
        convertedWordList = []
        for message in messageList:
            charList = list(message.lower())    # split a word to letters
            convertedMsg = ""
            for letter in charList:
                lIndex = letterList.index(letter)
                newLIndex = (lIndex + i) % len(letterList)
                convertedMsg += letterList[newLIndex]
            convertedWordList.append(convertedMsg)
        convertedMsgList.append(convertedWordList)

    return convertedMsgList


#@profile(precision=8)
def checkRNN(convertedMsgList, rnn):
    foundKey = False
    for list in convertedMsgList:
        realWordList = []
        for word in list:
            if rnn.classify_word(word):
                realWordList.append(word)
        if len(realWordList) == len(list):
            foundKey = True
            break

    if foundKey:
        msg = listToString(realWordList)
        print("Cyphered Message is English", msg, "in RNN")
        return True
    else:
        return False



#@profile(precision=8)
def checkDFA(convertedMsgList, dfa):
    foundKey = False
    for list in convertedMsgList:
        realWordList = []
        for word in list:
            if dfa.classify_word(word):
                realWordList.append(word)
        if len(realWordList) == len(list):
            foundKey = True
            break

    if foundKey:
        msg = listToString(realWordList)
        print("Cyphered Message is English", msg, "in DFA")
        return True
    else:
        return False


def listToString(list):
    sentence = ''
    for word in list:
        sentence += ' ' + str(word)

    return sentence


def rtCyChecker(messageList, rnn, dfa):  # Rotation cypher checker
    convertedMsgList = rtCyCdecode(messageList)
    foundKeyRNN = False
    foundKeyDFA = False
    print("Try message in following list", '\n', convertedMsgList)


    startRNN = time.time()
    if checkRNN(convertedMsgList, rnn):
        foundKeyRNN = True
    executeTimeRNN = time.time() - startRNN
    print("RNN execution time", executeTimeRNN)

    startDFA = time.time()
    if checkDFA(convertedMsgList, dfa):
        foundKeyDFA = True
    executeTimeDFA = time.time() - startDFA
    print("DFA execution time", executeTimeDFA)

    if foundKeyRNN != foundKeyDFA:
        print("RNN and DFA returned different result")

    if not foundKeyRNN and not foundKeyDFA:
        print("No rotation cyphered message founded")

    winner = ""
    winTime = ""
    timeDiff = abs(executeTimeRNN - executeTimeDFA)
    if executeTimeRNN <= executeTimeDFA:
        winner = "RNN"
        loser = "DFA"
        winTime = executeTimeRNN
    else:
        winner = "DFA"
        loser = "RNN"
        winTime = executeTimeDFA

    print("RNN, DFA Comparison: " + '\n' + winner, "execute " +
          '{percent:.2%}'.format(percent=timeDiff/winTime) + " faster than", loser)
