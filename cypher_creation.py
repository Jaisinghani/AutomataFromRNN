# -*- coding: utf-8 -*-

import random

def rotate_sentence(sentence, alphabet):
    
    print(sentence)
    cy_sentence=""
    temp= sentence.split()

    for word in temp:
        t_list=""
        for letter in word:
            num= alphabet.index(letter)
        
            if ((num + 1) >= len(alphabet)):
                num=-1
            
            t_list += alphabet[num+1]
        cy_sentence += t_list
        cy_sentence += ' '
        
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
    
    random_Letters = ['e', 'a', 't', 's', 'o', 'i', 'n']
    
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
      

def user_Input():
    sentence= input('Please enter your message: ')
    encrypted, rule = nested_swap(sentence)
    print('Encrypted Message: ', encrypted)
    print('Rule used for encryption: ', rule)
    

    