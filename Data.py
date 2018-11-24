x=list(x)
Letters_array=['e','t','a','o','i','n','s','r','u','m','p']    #
Letters_array=np.array(Letters_array)

length=[7,8,9,10,11]
for l in length:
	meaning_words=[]
	#name=str(l)+'.py'
	f= open('ALPHABET_'+str(l)+'.py',"w+")
	#print(l)
	Letters=Letters_array[0:l]
	#print(Letters)
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
			#f.write(a)
		else:
			continue
	f.write("WORDS=")	
	f.write(str(meaning_words))
	f.close() 
	#print(meaning_words)
