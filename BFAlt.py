import ALPHABET_26
meaningful_words = set(ALPHABET_26.WORDS)
alphabet = ALPHABET_26.ALPHABET
def rtCyCdecode(message):  # Rotation cypher decode

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

#check if the encoded message is a rotational cypher by checking a master list
def checkInList(encodeMessage):
    messages = rtCyCdecode(encodeMessage)
    possibleMatchingMessages = []
    for message in messages:
        messageSet = set(message)
        if messageSet < meaningful_words:
            possibleMatchingMessages.append(message)
    return possibleMatchingMessages


