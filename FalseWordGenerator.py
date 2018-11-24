import random

class meaninglessWords():

    def __init__(alphabet, meaningfulWords):
        self.wordList = []

        #find the longest word
        maxLength = 0
        for word in meaningfulWords:
            if len(word) > maxLength:
                maxLength = len(word)
                
        #init a length frequency array
        lengthFrequenyArray = [range(maxLength)]
        
        #calculate the frequencies
        for word in meaningfulWords:
            lengthFrequenyArray[len(word)] += 1
        
       #create one meaningless word of length n for each meaningful word of length n
       
       #each word length
       for length in range(len(lengthFrequenyArray)):
       
          #generate a number of words with that length
          for times in range(lengthFrequenyArray[length])
            
            falseWord = ""
            
            #append one random letter to false word for each unit of length
            for stringLength in range(length):
                falseWord.append(random.choice.(alphabet))
            if falseWord not in meaningfulWords:
                self.wordList.append(falseWord)
            
    def getAllWords(self):
        return self.wordList

