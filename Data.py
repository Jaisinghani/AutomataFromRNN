import sys

#reading configuration file 
with open('data.txt', 'r',newline='\n') as f:
    x = f.read().splitlines()

x=list(x)
Letters=['e','t','a','o','i','n','s','m','p','r','u']    
meaning_words=[]
for i in range(len(x)):
	a=x[i]
	flag=0
	for j in a:
		if(Letters.__contains__(j)):
			continue	
		else:
			flag=1
			break
	if(flag==0):
		meaning_words.append(a)
	else:
		continue	
print(len(meaning_words))
print(meaning_words)	