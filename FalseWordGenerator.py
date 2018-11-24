import random

#class falseWordGenerator():

def generateFalseWords(alphabet, meaningfulWords):
    wordList = []
    #print (meaningfulWords)
    #find the longest word
    maxLength = 0
    for word in meaningfulWords:
        if len(word) > maxLength:

            maxLength = len(word)

    #init a length frequency array
    lengthFrequenyArray = [0 for x in range(maxLength + 1)]

    #calculate the frequencies
    for word in meaningfulWords:
        lengthFrequenyArray[len(word)] += 1
        #print (lengthFrequenyArray)
    
        #create one meaningless word of length n for each meaningful word of length n
   
    #each word length
    for length in range(len(lengthFrequenyArray)):
   
       #generate a number of words with that length
       for times in range(lengthFrequenyArray[length]):
        
          falseWord = ""
        
          #append one random letter to false word for each unit of length
          for stringLength in range(length):
              falseWord += random.choice(alphabet)
          if falseWord.lower() not in meaningfulWords:
              wordList.append(falseWord.lower())
    #print (wordList)
    return wordList
    #def getAllWords(self):
    #    return self.wordList

