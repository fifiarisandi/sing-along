game_data = {
	'easy-peasy': {
		'song':"You put your right hand __1__, you take your right hand __2__, you put your right hand __1__, and you __3__ it all about."\
		 "You do the __4__ pokey, and you __5__ yourself around. That's what it's all about!",
		'answers': ["in", "out", "shake", "hokey", "turn"],
		'success_msg':"\nCongratulations! You did it! You are as good as my 4 years-old niece!\n\nNow, let's sing along!\n\n",
		'first_msg1':"\nYou chose easy-peasy! Don't worry if you can't guess it right the first time, you have "
	},
	'pro-wannabe': {
		'song': "I'm in love with the __1__ of you, we push and pull like a __2__ do. Although my heart is __3__ too, I'm in love with your __4__."\
		 "Oh I oh I oh I oh I I'm in love with your __4__. Oh I oh I oh I oh I I'm in love with your __4__. Oh I oh I oh I oh I I'm in love with your __4__."\
		 "Every day __5__ something brand new, I'm in love with the __1__ of you.",
		'answers': ["shape", "magnet", "falling", "body", "discovering"],
		'success_msg':"\nCongratulations! You did it! But, don't you think it was too easy? I mean, come on, everybody knows Ed Sheeran's songs!"\
		 "Try the next level if you think you are that good ;)\n\nNow, let's sing along!\n\n",
		'first_msg1':"\nYou chose pro-wannabe! Don't worry if you can't guess it right the first time, you have "
	},
	'all-rounder': {
		'song': "Amazing __1__, how __2__ the sound, that saved a __3__ like me. I __4__ was lost, but now I'm __5__, was blind, but now I see.",
		'answers': ["grace", "sweet", "wretch", "once", "found"],
		'success_msg':"\nCongratulations! You did it! Not bad, not bad at all! Try the next level if you dare ;)\n\nNow, let's sing along!\n\n",
		'first_msg1':"\nYou chose all-rounder! Don't worry if you can't guess it right the first time, you have "
	},
	'legend': {
		'song': "L is for the way you __1__ at me, O is for the __2__ one I see, V is very, very __3__, E is even more than anyone that you __4__."\
		 "And __5__ is all that I can give to you, __5__ is more than just a __6__ for two. Two in __5__ can make it,"\
		 "Take my heart and please don't __7__ it, __5__ was __8__ for me and you!",
		'answers': ["look", "only", "extraordinary", "adore", "love", "game", "break", "made"],
		'success_msg':"\nCongratulations! You did it! You really are a... wait for it... LEGEND!\n\nNow, let's sing along!\n\n",
		'first_msg1':"\nYou chose legend! Don't worry if you can't guess it right the first time, you have "
	}
}

messages = {
	'first_msg2': " chances to do it. Let's sing along! \n\n", 'err_msg1':"\nErr.. That's not the right lyric, try again! You have ", 'err_msg2':" chances left.", 
	'correct_msg':"\nYou got that right!" + "\n\n", 'fail_msg':"\nGame over! You had your chances, it seems like you need to upgrade your songs database."\
	 "Try again anytime you're ready! Thanks for playing!\n", 'q1':"\nWhat is your answer for __", 'q2':"__? "
}


def fill_in_the_blanks(level,sequence):
	"""
	Input: fill_in_the_blanks takes level and sequence as input.
	Output: fill_in_the_blanks returns the song of the chosen level with its filled-in blanks. 
	Behavior: This function fills the empty blanks with the correct answers given by the player.
	"""
	replaced=[]
	song_split=game_data[level]['song'].split()
	for word in song_split:
		replacement = "__" + str(sequence) + "__"
		word = word.replace(replacement,game_data[level]['answers'][sequence-1])
		replaced.append(word)
	game_data[level]['song'] = " ".join(replaced)
	return game_data[level]['song']


def wrong_chances(level,sequence,count,counter):
    """
    Input: wrong_chances takes level, sequence, count, and counter as input.
    Output: wrong_chances returns sequence number as output which indicates whether or not the player eventually gives the correct answers.
    Behavior: This function gives responds for wrong answers by players as many as they specified when they start playing the game.
    """
    while count<counter:
		answer = raw_input(messages['err_msg1'] + str(counter-count) + messages['err_msg2'] + messages['q1'] + str(sequence+1) + messages['q2'])
		if answer == game_data[level]['answers'][sequence]:
			sequence+=1
			break
		else:
			count+=1
		if count==counter:
			break
    return sequence 


def QAprocess(level,sequence,counter):
	"""
	Input: QAprocess takes level, sequence, and counter as input.
	Output: QAprocess returns sequence number as output, which is used to determine which message will be given to the player. 
	Behavior: This function handles the Q&A process with the player in each level.
	"""
	count=0
	if sequence==0:
		answer = raw_input(game_data[level]['first_msg1'] + str(counter) + messages['first_msg2'] + game_data[level]['song'] + "\n" + messages['q1'] \
			+ str(sequence+1) + messages['q2'])
		count+=1
		if answer==game_data[level]['answers'][sequence]:
			return sequence+1
		else:
			sequence = wrong_chances(level,sequence,count,counter)
			return sequence
	else:
		answer = raw_input(messages['q1'] + str(sequence+1) + messages['q2'])
		count+=1
		if answer==game_data[level]['answers'][sequence]:
			return sequence+1
		else:
			sequence = wrong_chances(level,sequence,count,counter)
			return sequence


def game(level,sequence,counter):
	"""
	Input: game takes level, sequence, and counter as input.
	Output: game returns a message to the player depending on the status of the given answer. If the answer is correct, it will also return the song text that's
			already filled in with the correct answer, along with the message. 
	Behavior: This function iterates as many as the empty blanks in each level. It's called by the main function (lets_sing_along).
	"""
	count=0
	while count < len(game_data[level]['answers']):
		new_sequence=QAprocess(level,sequence,counter)
		if new_sequence==sequence:
			return messages['fail_msg']
		else:
			if count==len(game_data[level]['answers'])-1:
				return game_data[level]['success_msg'] + fill_in_the_blanks(level,new_sequence) + "\n"
			else:
				print messages['correct_msg'] + fill_in_the_blanks(level,new_sequence)
			sequence=new_sequence
		count+=1


def lets_sing_along():
	"""
	Input:lets_sing_along doesn't take any arguments as input as the input will be gotten from the player's answers to the given question.
	Output: lets_sing_along returns a message to the player depending on the result of the game played by the player. It will give error message if the player 
			types the wrong level name.
	Behavior: This is the main function. The game is played by calling this function in the first place. It calls the relevant function to perform the game.
	"""
	sequence=0
	level = raw_input("Let's sing along! \n\nChoose your level: \n easy-peasy \n pro-wannabe \n all-rounder \n legend\n\n")
	if level not in game_data:
		return "You don't type the right level name."
	counter = int(raw_input("\nChoose how many wrong answers should we spare you? Type any positive numbers. "))
	return game(level,sequence,counter)


print lets_sing_along()

