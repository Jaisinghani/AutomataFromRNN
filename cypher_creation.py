# -*- coding: utf-8 -*-

import random
import string

def rotate_sentence(sentence, n_rotations):
    
    print(sentence)
    cy_sentence=[]

    for i in range (0, len(sentence)):
        
        print(ord(sentence[i]))
        if (sentence[i]!=" "):
            c= ord(sentence[i]) + n_rotations
            if(c > ord('z')):
                c= c- ord('z') + ord('a') - 1
            if(c <= ord('Z')):
                c+=32
            cy_sentence.append(chr(c))
        else:
            cy_sentence.append(" ")
    
    return cy_sentence   
    
    
def swap_letters(sentence, cy_rule):
    print(sentence)
    
    tempSentence=list(sentence.lower())
    i=0
    for letter in tempSentence:
        if letter in cy_rule.keys():
            tempSentence[i]=cy_rule[letter]
            i+=1
        else:
            i+=1
        
    return "".join(tempSentence), cy_rule  
            
    
def nested_swap(sentence):
    
    random_Letters = string.ascii_lowercase[:]
    
    cy_rule={}
    for letter in random_Letters:
        cy_rule.update({letter:random.choice(random_Letters)})
    
    tempSentence=list(sentence.lower())
    i=0
    for letter in tempSentence:
        if letter in cy_rule.keys():
            tempSentence[i]=cy_rule[letter]
            i+=1
        else:
            i+=1
        
    return "".join(tempSentence), cy_rule  
            
    

