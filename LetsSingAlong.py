easy_song = '''You put your right hand __1__, you take your right hand __2__, 
you put your right hand __1__, and you __3__ it all about.
You do the __4__ pokey, and you __5__ yourself around.
That's what it's all about!'''

pro_song = '''I'm in love with the __1__ of you, 
we push and pull like a __2__ do.
Although my heart is __3__ too,
I'm in love with your __4__.
Oh I oh I oh I oh I
I'm in love with your __4__.
Oh I oh I oh I oh I
I'm in love with your __4__.
Oh I oh I oh I oh I
I'm in love with your __4__.
Every day __5__ something brand new,
I'm in love with the __1__ of you.'''

allround_song = '''Amazing __1__, how __2__ the sound,
that saved a __3__ like me. 
I __4__ was lost, but now I'm __5__,
was blind, but now I see.'''

legend_song = '''L is for the way you __1__ at me, 
O is for the __2__ one I see,
V is very, very __3__,
E is even more than anyone that you __4__.
And __5__ is all that I can give to you,
__5__ is more than just a __6__ for two. 
Two in __5__ can make it,
Take my heart and please don't __7__ it, 
__5__ was __8__ for me and you!'''

correct_msg = "\nYou got that right!" + "\n\n"
fail_text = "\nGame over! You had your chances, it seems like you need to upgrade your songs database. Try again anytime you're ready! Thanks for playing!\n"

easy_answers = ["in", "out", "shake", "hokey", "turn"]
pro_answers = ["shape", "magnet", "falling", "body", "discovering"]
allround_answers = ["grace", "sweet", "wretch", "once", "found"]
legend_answers = ["look", "only", "extraordinary", "adore", "love", "game", "break", "made"]

levels = ["easy-peasy", "pro-wannabe", "all-rounder", "legend"]

#This function fills the empty blanks with the correct answers given by the player.
def fill_in_the_blanks(level,sequence):
	global easy_song, pro_song, allround_song, legend_song
	replaced=[]
	if level=="easy-peasy":
		song_split=easy_song.split()
	elif level=="pro-wannabe":
		song_split=pro_song.split()
	elif level=="all-rounder":
		song_split=allround_song.split()
	else:
		song_split=legend_song.split()
	for word in song_split:
		replacement = "__" + str(sequence) + "__"
		if level=="easy-peasy":
			word = word.replace(replacement,easy_answers[sequence-1])
		elif level=="pro-wannabe":
			word = word.replace(replacement,pro_answers[sequence-1])
		elif level=="all-rounder":
			word = word.replace(replacement,allround_answers[sequence-1])
		else:
			word = word.replace(replacement,legend_answers[sequence-1])
		replaced.append(word)
	if level=="easy-peasy":
		easy_song = " ".join(replaced)
		return easy_song
	elif level=="pro-wannabe":
		pro_song = " ".join(replaced)
		return pro_song
	elif level=="all-rounder":
		allround_song = " ".join(replaced)
		return allround_song
	else:
		legend_song = " ".join(replaced)
		return legend_song

#This function gives responds for wrong answers by players as many as they specified when they start playing the game
#Its output is the sequence number which indicates whether or not the player eventually gives the correct answers.
def wrong_chances(level,sequence,count,counter):
	if level=="easy-peasy":
		answers_list=easy_answers
	elif level=="pro-wannabe":
		answers_list=pro_answers
	elif level=="all-rounder":
		answers_list=allround_answers
	else: 
		answers_list=legend_answers
	while count<counter:
		answer = raw_input("\nErr.. That's not the right lyric, try again! You have " + str(counter-count) + " chances left. What is your answer for __" + str(sequence+1) + "__? ")
		if answer == answers_list[sequence]:
			sequence+=1
			break
		else:
			count+=1
		if count==counter:
			break
	return sequence

#This function handles the Q&A process in each level. The output (sequence number) is used to determine which message will be given to the player.
def QAprocess(level,sequence,counter):
	count=0
	if sequence==0:
		if level=="easy-peasy":
			answer = raw_input("\nYou chose easy-peasy! Don't worry if you can't guess it right the first time, you have " + str(counter) + " chances to do it. Let's sing along! \n\n" + easy_song + "\n\n" + "What is your answer for __" + str(sequence+1) + "__? ")
		elif level=="pro-wannabe":
			answer = raw_input("\nYou chose pro-wannabe! Don't worry if you can't guess it right the first time, you have " + str(counter) + " chances to do it. Let's sing along! \n\n" + pro_song + "\n\n" + "What is your answer for __" + str(sequence+1) + "__? ")
		elif level=="all-rounder":
			answer = raw_input("\nYou chose all-rounder! Don't worry if you can't guess it right the first time, you have " + str(counter) + " chances to do it. Let's sing along! \n\n" + allround_song + "\n\n" + "What is your answer for __" + str(sequence+1) + "__? ")
		else:
			answer = raw_input("\nYou chose legend! Don't worry if you can't guess it right the first time, you have " + str(counter) + " chances to do it. Let's sing along! \n\n" + legend_song + "\n\n" + "What is your answer for __" + str(sequence+1) + "__? ")
		count+=1
		if answer in [easy_answers[sequence], pro_answers[sequence], allround_answers[sequence], legend_answers[sequence]]:
			return sequence+1
		else:
			sequence = wrong_chances(level,sequence,count,counter)
			return sequence
	else:
		answer = raw_input("\nWhat is your answer for __" + str(sequence+1) + "__? ")
		count+=1
		if level=="legend":
			if answer==legend_answers[sequence]:
				return sequence+1
			else:
				sequence = wrong_chances("legend",sequence,count,counter)
				return sequence
		else:
			if answer in [easy_answers[sequence], pro_answers[sequence], allround_answers[sequence]]:
				return sequence+1
			else:
				sequence = wrong_chances(level,sequence,count,counter)
				return sequence

def game(level,sequence,counter):
	count=0
	if level=="legend":
		dfa
	else:
		while count < len(easy_answers):
			new_sequence=QAprocess(level,sequence,counter)
			if new_sequence==sequence:
				return fail_text
			else:
				if count==len(easy_answers)-1:
					if level=="easy-peasy":
						return "\nCongratulations! You did it! You are as good as my 4 years-old niece! Now, let's sing along!" +"\n\n" + fill_in_the_blanks(level,new_sequence) + "\n" 
					elif level=="pro-wannabe":
						return "\nCongratulations! You did it! But, don't you think it was too easy? I mean, come on, everybody knows Ed Sheeran's songs! Try the next level if you think you are that good ;) Now, let's sing along!" +"\n\n" + fill_in_the_blanks(level,new_sequence) + "\n"
					elif level=="all-rounder":
						return "\nCongratulations! You did it! Not bad, not bad at all! Try the next level if you dare ;) Now, let's sing along!" +"\n\n" + fill_in_the_blanks(level,new_sequence) + "\n"
					else:
						return "\nCongratulations! You did it! You really are a... wait for it... LEGEND! Now, let's sing along!" +"\n\n" + fill_in_the_blanks(level,new_sequence) + "\n"
				else:
					print correct_msg + fill_in_the_blanks(level,new_sequence)
				sequence=new_sequence
			count+=1


#This function iterates as many as the empty blanks in each level. It's called by the main function (lets_sing_along) if the player choose "easy-peasy" level. 
'''def easy_game(sequence,counter):
	count=0
	while count < len(easy_answers):
		new_sequence=QAprocess("easy-peasy",sequence,counter)
		if new_sequence==sequence:
			return fail_text
		else:
			if count==len(easy_answers)-1:
				return "\nCongratulations! You did it! You are as good as my 4 years-old niece! Now, let's sing along!" +"\n\n" + fill_in_the_blanks("easy-peasy",new_sequence) + "\n"
			else:
				print correct_msg + fill_in_the_blanks("easy-peasy",new_sequence)
			sequence=new_sequence
		count+=1'''

#This function iterates as many as the empty blanks in each level. It's called by the main function (lets_sing_along) if the player choose "pro-wannabe" level.
'''def pro_game(sequence,counter):
	count=0
	while count < len(pro_answers):
		new_sequence=QAprocess("pro-wannabe",sequence,counter)
		if new_sequence==sequence:
			return fail_text
		else:
			if count==len(pro_answers)-1:
				return "\nCongratulations! You did it! But, don't you think it was too easy? I mean, come on, everybody knows Ed Sheeran's songs! Try the next level if you think you are that good ;) Now, let's sing along!" +"\n\n" + fill_in_the_blanks("pro-wannabe",new_sequence) + "\n"
			else:
				print correct_msg + fill_in_the_blanks("pro-wannabe",new_sequence)
			sequence=new_sequence
		count+=1'''

#This function iterates as many as the empty blanks in each level. It's called by the main function (lets_sing_along) if the player choose "all-rounder" level.
'''def allround_game(sequence,counter):
	count=0
	while count < len(allround_answers):
		new_sequence=QAprocess("all-rounder",sequence,counter)
		if new_sequence==sequence:
			return fail_text
		else:
			if count==len(allround_answers)-1:
				return "\nCongratulations! You did it! Not bad, not bad at all! Try the next level if you dare ;) Now, let's sing along!" +"\n\n" + fill_in_the_blanks("all-rounder",new_sequence) + "\n"
			else:
				print correct_msg + fill_in_the_blanks("all-rounder",new_sequence)
			sequence=new_sequence
		count+=1'''

#This function iterates as many as the empty blanks in each level. It's called by the main function (lets_sing_along) if the player choose "legend" level.
def legend_game(sequence,counter):
	count=0
	while count < len(legend_answers):
		new_sequence=QAprocess("legend",sequence,counter)
		if new_sequence==sequence:
			return fail_text
		else:
			if count==len(legend_answers)-1:
				return "\nCongratulations! You did it! You really are a... wait for it... LEGEND! Now, let's sing along!" +"\n\n" + fill_in_the_blanks("legend",new_sequence) + "\n"
			else:
				print correct_msg + fill_in_the_blanks("legend",new_sequence)
			sequence=new_sequence
		count+=1

#This is the main function. The game is played by calling this function in the first place. 
def lets_sing_along():
	sequence=0
	level = raw_input("Let's sing along! \n\nChoose your level: \n easy-peasy \n pro-wannabe \n all-rounder \n legend\n\n")
	if level not in levels:
		return "You don't type the right level name."
	counter = int(raw_input("\nChoose how many wrong answers should we spare you? Type any positive numbers. "))
	if level == levels[0]:
		return easy_game(sequence,counter)
	elif level == levels[1]:
		return pro_game(sequence,counter)
	elif level == levels[2]:
		return allround_game(sequence,counter)
	else:
		return legend_game(sequence,counter)


print lets_sing_along()

