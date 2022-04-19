import random
import words
import sys

def quiz():
	print("\nWhat do you want to learn?\n")
	print("\tAll words:         type a")
	print("\tRecent new words:  type b")
	print("\tToday's new words: type c")
	print("")
	while True:
		learn = input("Type of learning: ")
		if learn == "a":
			words.fillAll()
			break
		elif learn == "b":
			words.fillRecent()
			break
		elif learn == "c":
			words.fillToday()
			break
		else:
			print("Not a proper key. Type either a, b, or c")
	
	print("")
	print("\t-d to show definitions")
	print("\nBegin...\n")
	
	indicesOfTestWords = [i for i in range(len(words.allWords))]
	
	while (len(indicesOfTestWords) != 0):
		score = 0
		random.shuffle(indicesOfTestWords)
		
		indiciesOfWrongWords = []
		question = 1
		for i in indicesOfTestWords:
			
			print("%i)" % question, end = ' ')
			example = words.allExamples[i]
			exampleL = example.split()
			try:
				exampleL[exampleL.index(words.allWords[i])] = '______'
			except:
				print("Problem finding the %s in this example %s" % (words.allWords[i], example))
				continue
			print(' '.join(exampleL))

			choices = random.sample(words.allWords, random.randrange(4,6))
			if words.allWords[i] not in choices:
				choices.append(words.allWords[i])
			random.shuffle(choices)
			for j in range(len(choices)):
				print("\t%i. %s" % (j, choices[j]))
			while True:
			
				val = input("Your response: ")
				if val == "-d":
					print("Definition: ", end='')
					print(words.allDefinitions[i])
					continue
				try:
					val = int(val)
				except ValueError:
					print("Not a number. Respond with the index of the word you choose.")
					continue
				if val >= len(choices) or val < 0:
					print("Not in range. Respond with the index of the word you choose. ")
					continue
				if choices[val] == words.allWords[i]:
					print("Correct :)")
					score += 1
					break
				else:
					print("Incorrect :(")
					indiciesOfWrongWords.append(i)
					break
			print("---------------------------")
			question += 1
		print("your score is: %i/%i\n" % (score, len(indicesOfTestWords)))
		indicesOfTestWords = indiciesOfWrongWords
		if len(indicesOfTestWords) != 0:
			print("Now, attempt the ones you got wrong.")

	print("Nice job")

quiz()