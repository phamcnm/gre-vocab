'''

////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////
////                                                                                    //// 
////                                                                                    ////  
////    VV          VV         OOO              CC CC         AA         BB BB BB       ////
////     V          V      OO       OO       CC              A  A        BB       BB    ////    
////      VV      VV     OO           OO   CC               AA  AA       BB       BB    ////
////       V      V      OO           OO   CC              A      A      BB BB BB       ////
////        VV  VV       OO           OO   CC             AA  AA  AA     BB       BB    ////
////         V  V          OO       OO       CC          A          A    BB       BB    ////
////          VV               OOO              CC CC   AA          AA   BB BB BB       ////  
////                                                                                    //// 
////                                                                                    //// 
////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////

'''
import random
import words

def checkSpelling(response, word):
	rl = list(response)
	wl = list(word)
	i = 0
	j = 0
	strength = 0
	if len(rl) > len(wl):
		strength -= 1
	while True:
		if rl[i] == wl[j]:
			strength += 1
		else:
			if i+1 < len(rl) and j+1 < len(wl):
				if rl[i] == wl[j+1] and rl[i+1] == wl[j]:
					strength += 1
				elif rl[i+1] == wl[j] and rl[i+1] != wl[j+1]:
					strength += 1
					i += 1
				elif rl[i] == wl[j+1] and rl[i+1] != wl[j+1]:
					strength += 1
					j += 1
			else:
				if i+1 < len(rl) and rl[i+1] == wl[j]:
					strength += 1
					i += 1
				elif j+1 < len(wl) and rl[i] == wl[j+1]:
					strength += 1
					j += 1
		i += 1
		j += 1
		if i >= len(rl) or j >= len(wl):
			break
	if strength >= len(word)-1:
		return True
	return False


def main():
	
	print("")
	print("-c to show word choice")
	print("-h to show example sentence")
	print("\nBegin...\n")
	
	words.fillAll()
	indicesOfTestWords = [i for i in range(len(words.allWords))]
	
	while (len(indicesOfTestWords) != 0):
		score = 0
		random.shuffle(indicesOfTestWords)
		
		indiciesOfWrongWords = []
		question = 1
		for i in indicesOfTestWords:
			
			print("%i)" % question, end = ' ')
			print(words.allDefinitions[i])

			choices = random.sample(words.allWords, random.randrange(4,8))
			if words.allWords[i] not in choices:
				choices.append(words.allWords[i])
			random.shuffle(choices)

			while True:
			
				val = input("Your response: ")
				if (val == "-c"):
					print("Choices: ", end = '')	
					print(choices)
					continue
				if (val == "-h"):
					example = words.allExamples[i]
					exampleL = example.split()
					exampleL[exampleL.index(words.allWords[i])] = '______'
					print(' '.join(exampleL))
					continue
				if val == words.allWords[i]:
					print("Correct :)")
					score += 1
					break
				else:
					if checkSpelling(val, words.allWords[i]):
						print("Close. Wrong spelling. Type again.")
						continue
					else:
						print("Incorrect :(")
						indiciesOfWrongWords.append(i)
						break
			print("---------------------------")
			question += 1
		print("your score is: %i/%i" % (score, len(indicesOfTestWords)))
		print("Now, attempt the ones you got wrong.")
		indicesOfTestWords = indiciesOfWrongWords

	print("Nice job")

main()


