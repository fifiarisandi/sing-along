easy_song = '''You put your right hand __1__, you take your right hand __2__, 
			you put your right hand __1__, and you __3__ it all about.
			You do the __4__ pokey, and you __5__ yourself around.
			That's what it's all about!'''

easy_answers = ["in", "out", "shake", "hokey", "turn"]
levels = ["easy-peasy", "amateur", "pro-wannabe", "song-master"]

def easy(level, sequence, answer):
	count=3
	next=False
	if sequence==0:
		#if level=="easy-peasy":
		answer_input = raw_input("You choose " + level + "\n" + "Don't worry if you can't guess it right the first time, you have 3 chances to make it right! \n" + "Let's sing along! \n" + easy_song + "\n" + "What do you think the right word to fill __1__?")
		count=count-1
		if answer_input!=easy_answers[sequence]:
			while count>0:
				answer_input = raw_input("That's probably another song. Try again! You have " + count + " chances left")
				if answer_input==easy_answers[sequence]:
					next=True
					break
				count=count-1
			if next==False:
				return "It looks like you never heard this song before. No worries though, you can try again anytime you're ready!"
		else:
			next=True
	elif next==True:
		#elif sequence==1:
		count=count-1
			while count>0:
				if answer_input==easy_answers[sequence]:
					return True, sequence+1
				else:
					answer_input = raw_input("You have " + count + " chances to make it right! \n" + "Let's sing along! \n" + easy_song + "\n" + "What do you think the right word to fill __2__?")
				count=count-1
			return False, len(easy_answers)	


def fill_in_the_blanks(sequence, level):
	if level=="easy-peasy":
		easy_song_split=easy_song.split()
		for word in easy_song_split:
			if sequence in word:
				word=word.replace(word, easy_answers[0])
		easy_song=" ".join(easy_song_split)
		return easy_song


def lets_sing_along():
	seq=0
	level_input = raw_input("Choose your level: easy-peasy  amateur  pro-wannabe  song-master")
	if level_input in levels:
		if level_input=="easy-peasy":
			message=easy() 


			answer_status, seq = questions(level_input, seq, "")
			if answer_status==False:
				return "It looks like you never heard this song before. No worries though, you can try again anytime you're ready!"
			elif answer_status==True and seq==1:
				easy_song = fill_in_the_blanks(seq, level_input)
				answer_input = raw_input("You got that right! \n" + easy_song + "\n" + "What do you think the right word to fill __2__?")
				questions(level_input, seq, answer_input)








