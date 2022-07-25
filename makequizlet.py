with open("allwords.txt", "r") as r:
	with open("quizletwords.txt", "w") as w:
		for i in r:
			l = i.split("\t")
			w.write(l[0])
			w.write("\t")
			w.write(l[1])
			w.write("\n")