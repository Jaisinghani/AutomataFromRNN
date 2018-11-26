import cypher_creation as c
import Rotation_Checker as RCT
import random
ALPHABET = ['a', 'e', 'i', 'n', 'o', 'r', 's', 't']
def accuracyChecker(wordList, ALPHABET, rnn, dfa):
    RNNcount = 0.0
    DFAcount = 0.0
    for i in range(50):
        pickedList = []
        for x in range(5):
            word = random.choice(wordList)
            pickedList.append(word)
        
        message = ""
        for word in pickedList:
            message += word + " "
        
        cypher1 = c.rotate_sentence(message, ALPHABET)
        matchRNN, matchDFA = RCT.rtCyChecker(cypher1, ALPHABET, rnn, dfa)
        RNNcount += matchRNN
        DFAcount += matchDFA
        
    accuracyRNN = '{percent:.2%}'.format(percent= RNNcount / 50)
    accuracyDFA = '{percent:.2%}'.format(percent= DFAcount / 50)
    
    print("accuracyRNN vs accuracyDFA", accuracyRNN, accuracyDFA)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  