with open("currweek.txt", "r") as r:
	with open("currweek-quizlet.txt", "w") as w:
		for i in r:
			l = i.split("\t")
			w.write(l[0])
			w.write("\t")
			w.write(l[1])
			w.write("\n")