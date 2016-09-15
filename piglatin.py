#pig latin


def pig_latin(word):
    wordL = list(word)
    if word[0] == 't' and word[1] == 'h' or word[0] == 's' and word[1] == 'h':
        nF = wordL[:2]
        nL = wordL[2:]
    else:
        nF = wordL[:1]
        nL = wordL[1:]
    ay = 'ay'
    finL = nL + nF
    finS = "".join(finL) + ay
    return finS


def select_word():
	print "Enter a word or sentence to be converted to pig-Latin: "
	sentence = raw_input()
	pig_sentence = []
	for i in sentence.split():
	    #pig_latin(i)
	    pig_sentence.append(pig_latin(i))

	pigFin = ' '.join(pig_sentence)

	print pigFin


def begin():
	select_word()
	start = True
	while start:
		print "Would you like to go again? y/n"
		ans = raw_input()
		if ans == 'n':
			print "Goodbye"
			break
		else:
			select_word()

begin()
exit()