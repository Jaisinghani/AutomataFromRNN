def freqAnalysis(MEANINGFULWORDS):
    frequencyAnalysis={}
    letterList=[]
   # with open('words.txt', 'r') as f:
   #     wordList=f.read()
    tempDict=Counter()
    for word in MEANINGFULWORDS:
        for l in word:
            tempDict[l]+=1     
    notWord=["'",","," ","\n",]
    frequencyAnalysis={}
    for k in tempDict:
        if k in notWord:
            continue
        else:
            frequencyAnalysis.update({k:tempDict[k]})

    resultFA=sorted(frequencyAnalysis.items(), key=lambda kv: kv[1],reverse=True)
    frequencyAnalysis={}
    for k in resultFA:
        frequencyAnalysis.update({k[0]:k[1]})
    #print(frequencyAnalysis)
    for k in resultFA:
        letterList.append(k[0]) 
    return letterList

def sentenceOrder(letterList,SENTENCE): 
    sentenceOrder=[]            #pass this value
    letterMapping={}
  #  with open('testSentences.txt', 'r') as f:    ## reading sentence from file
  #      sentence=f.read()
    tempDict=Counter()
    for word in SENTENCE:
        tempDict[word]+=1       
    notWord=[" ","\n"]
    faSentence={}
    for k in tempDict:
        if k in notWord:
            continue
        else:
            faSentence.update({k:tempDict[k]})
    resultFaS=sorted(faSentence.items(), key=lambda kv: kv[1],reverse=True)
    for k in resultFaS:
        sentenceOrder.append(k[0]) 
    #print(sentenceOrder)
    for i,k in enumerate(sentenceOrder):
        letterMapping.update({k[0]:letterList[i]})
    return letterMapping

def freqAnalysisSwap(MEANINGFULWORDS,SENTENCE):
    tempSentence=[]
    sentenceString=""
    tempWord=[]
    letterList=freqAnalysis(MEANINGFULWORDS)
    letterMapping=sentenceOrder(letterList,SENTENCE)
    #print("a:",letterList)
    #print("b:",letterMapping)
    for word in SENTENCE.split():
        tempString=" "
        for l in word:
            if l in letterMapping:
                tempWord.append(letterMapping[l])
            else:
                continue

        tempString.join(tempWord) 
        tempWord.append(tempString)
    result=sentenceString.join(tempWord)
    return result

from collections import Counter
#with open('words.txt', 'r') as f:
#     wordList=f.read()
#MEANINGFULWORDS=[]
#for word in wordList:
#    MEANINGFULWORDS.append(word)
#SENTENCE="eat is ir tae ate"
#output=freqAnalysisSwap(MEANINGFULWORDS,SENTENCE)
#return(output)
