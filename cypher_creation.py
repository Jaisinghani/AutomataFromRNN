# -*- coding: utf-8 -*-

import random

def rotate_sentence(sentence, alphabet):
    
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

    
def swap_letters(sentence, random_Letters):
    
    temp_list= random_Letters.copy()
    cy_rule={}
    while(len(cy_rule) != len(random_Letters)):
        temp1 = random.choice(temp_list)
        temp2 = random.choice(temp_list)
        if(temp1 != temp2):
            cy_rule.update({temp1:temp2})
            cy_rule.update({temp2:temp1})
            if temp1 in temp_list:
                temp_list.remove(temp1)
            if temp2 in temp_list:    
                temp_list.remove(temp2)
    
    tempSentence=list(sentence.lower())
    i=0
    for letter in tempSentence:
        if letter in cy_rule.keys():
            tempSentence[i]=cy_rule[letter]
            i+=1
        else:
            i+=1
        
    return "".join(tempSentence), cy_rule  
      

def user_Input(alphabet):
    sentence= input('Please enter your message: ')
    encrypted, rule = swap_letters(sentence, alphabet)
    print('Encrypted Message: ', encrypted)
    print('Rule used for encryption: ', rule)
    
 