wordsDay0 = ["beseech", "fluster", "enamored", "ineluctable", "invidious",\
			 "plangent", "incumbent", "nugatory", "contentious", "denouement",\
			 "predilection", "affinity", "sanguine", "choleric", "physiognomy",\
			 "temperament", "humor", "augury"]
definitionsDay0 = ["to beg, plead, implore",\
				   "to make nervous, embarrassed, or confused",\
				   "fond of; feeling love towards",\
				   "certain, inevitable",\
				   "offensive, hateful; tending to cause bitterness and resentment",\
				   "pounding, thundering, resounding",\
				   "one who holds a specific office at the time spoken of",\
				   "of no value or importance",\
				   "quarrelsome, inclined to argue",\
				   "an outcome or solution; the unraveling of a plot",\
				   "preference",\
				   "an attraction to",\
				   "cheerful; optimistic",\
				   "easily angered",\
				   "facial features",\
				   "a person's or animal's nature, especially as it permanently affects their behavior",\
				   "a mood or state of mind",\
				   "a sign of what will happen in the future; an omen"]
examplesDay0 = ["The servant wants to beseech the king for food to feed his starving family.",\
			   "There's nothing you can do or say to fluster Frank.",\
			   "It is not difficult to see why Edward is enamored of her.",\
			   "After being, in turn, anxious, angry, and sometimes morose, he accepts the coming ineluctable defeat with serenity.",\
			   "The local authority could find itself in the invidious position of having to refuse.",\
			   "There was the plangent and echoing sound of sea waves.",\
			   "He defeated the incumbent governor by a large plurality.",\
			   "A nugatory and pointless observation.",\
			   "The socioeconomic plan had been the subject of contentious debate.",\
			   "The film's denouement was unsatisfying and ambiguous.",\
			   "I have a predilection for Asian food.",\
			   "He has an affinity for the music of Berlioz.",\
			   "She is sanguine about prospects for the global economy.",\
			   "A choleric and self-important little man.",\
			   "Friends began to notice a change in his physiognomy after he hears the news.",\
			   "She had an artistic temperament and so no wonder why she thinks like one.",\
			   "Her good humor vanished.",\
			   "They heard the sound as an augury of death."]

wordsDay1 = ["cosmopolitan", "intransigent", "mercenary", "insular", "capricious",\
			"clamorous", "numinous", "empirical", "sonorous", "dearth",\
			"ambiguous", "gainsay", "sterling", "prescient", "proprietary",\
			"didactic", "perpetuate", "feeble", "turbulent", "augment",\
			"repudiate", "brook", "wont", "fecund", "verisimilitude",\
			"irascible", "exasperation"]
definitionsDay1 = ["including or containing people from many different countries",\
			   "unwilling to change one's view",\
			   "primarily concerned with making money, potentially at the expense of ethics",\
			   "ingorant of, or uninterested in outside cultures and ideas",\
			   "sudden changes of mood, or behavior",\
			   "loud and confused noise",\
			   "having a strong religions or spiritual quality",\
			   "verifiable by observation, not just based on theory",\
			   "imposingly deep and full",\
			   "a scarcity, a lack of something",\
			   "open to more than one interpretation",\
			   "deny, contradict",\
			   "excellent or valuable",\
			   "having or showing knowledge of future events",\
			   "relating to an owner or ownership",\
			   "having educational purposes",\
			   "keep alive, make something continue indefinitely",\
			   "weak, frail",\
			   "characterized by conflicts and disorder",\
			   "make greater by adding to it; increase",\
			   "refuse to accept or be associated with",\
			   "tolerate or allow",\
			   "in the habit of doing something",\
			   "fertile",\
			   "the apperance of being true or real",\
			   "having or showing tendency to be easily angered",\
			   "a feeling of intense irratation or arrogance"]
examplesDay1 = ["Cosmopolitan metropolis.",\
			   "Her father had tried persuasion, but she was intransigent and refused to listen.",\
			   "A mercenary Wall St broker.",\
			   "Stubbornly insular farming people.",\
			   "Our livelihood hinges on a capricious boss. It's terrible.",\
			   "A jostling, clamorous mob.",\
			   "The strange numinous beauty of this ancient landmark.",\
			   "There is empirical evidene to support their arugment.",\
			   "He read aloud with a sonorous voice.",\
			   "There is a dearth of evidence, so we deemed it worthless.",\
			   "Confounding variables make the stat ambiguous that people can interpret it differently.",\
			   "They were so persuasive that it's hard to gainsay their conclusion.",\
			   "Given their sterling reputation, it's not in our favor to challenge them.",\
			   "A prescient warning about nrxt year global climate situation.",\
			   "The company has a proprietary rights to the property.",\
			   "The didactic novel taught students how to be kind to neighbors as ourselves.",\
			   "The law was made to perpetuate the interests of the ruling class. it's hard to change the system.",\
			   "My legs are very feeble after the flu.",\
			   "The country's turbulent 20 years has come to an end. It's a day to celebrate.",\
			   "He wants to augment his summer income by painting houses when he's not doing his day job.",\
			   "She will try to repudiate any policies associated with previous party leaders.",\
			   "I would not brook any gossip towards my best friend.",\
			   "I was wont to arise at 5:30 every morning.",\
			   "As an artist, she gets most of her inspiration from nature; her daily walks in the woods are a fecund source of ideas.",\
			   "The detail gives the novel a lot of verisimilitude and realism.",\
			   "You don't want to mess with the irascible professor.",\
			   "She rolled her eys in exasperation when she hears the question about a foundational concept the student should have known 5 weeks ago."]

everything = [[wordsDay0, definitionsDay0, examplesDay0], [wordsDay1, definitionsDay1, examplesDay1]]

allWords = []
allDefinitions = []
allExamples = []

def fillAll():
	for i in range(len(everything)):
		allWords.extend(everything[i][0])
		allDefinitions.extend(everything[i][1])
		allExamples.extend(everything[i][2])

def fillRecent():
	if len(everything) < 5:
		fillAll()
	else:
		for idx in range(len(everything)-5, everything):
			allWords.extend(everything[i][0])
			allDefinitions.extend(everything[i][1])
			allExamples.extend(everything[i][2])

def fillToday():
	i = everything[len(everything)-1]
	allWords.extend(i[0])
	allDefinitions.extend(i[1])
	allExamples.extend(i[2])



# print(len(wordsDay0))
# print(len(definitionsDay0))
# print(len(exampleDay0))

