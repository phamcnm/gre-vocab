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
	testWords = words.allWords
	testDefinitions = words.allDefinitions
	
	while (len(testWords) != 0):
		
		score = 0
		n = len(testDefinitions)
		l = [i for i in range(len(testWords))]
		random.shuffle(l)
		wrongWords = []
		wrongDefinitions = []
		question = 1
		for i in range(len(l)):
			
			print("%i)" % question, end = ' ')
			print(testDefinitions[l[i]])
			
			val = input("Your response: ")
			if (val == "-c"):
				choices = random.sample(words.allWords, random.randrange(4,8))
				if testWords[l[i]] not in choices:
					choices.append(testWords[l[i]])
				random.shuffle(choices)
				print("Choices: ", end = '')	
				print(choices)
				val = input("Your response: ")
			if val == testWords[l[i]]:
				print("Correct :)")
				score += 1
			else:
				while checkSpelling(val, testWords[l[i]]):
					print("Close. Wrong spelling. Type again.")
					val = input("Your response: ")
					if (val == "-c"):
						choices = random.sample(words.allWords, random.randrange(4,8))
						if testWords[l[i]] not in choices:
							choices.append(testWords[l[i]])
						random.shuffle(choices)
						print("Choices: ", end = '')	
						print(choices)
						val = input("Your response: ")
					if val == testWords[l[i]]:
						print("Correct :)")
						score += 1
						break
				else:
					print("Incorrect :(")
					wrongWords.append(testWords[l[i]])
					wrongDefinitions.append(testDefinitions[l[i]])
			print("---------------------------")
			question += 1
		print("your score is: %i/%i" % (score, len(testWords)))
		print("Now, attempt the ones you got wrong.")
		testWords = wrongWords
		testDefinitions = wrongDefinitions

	print("Nice job")

main()


