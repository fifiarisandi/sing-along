from random import randint

easy_song = '''You put your right hand __1__, you take your right hand __2__, 
you put your right hand __1__, and you __3__ it all about.
You do the __4__ pokey, and you __5__ yourself around.
That's what it's all about!'''

easy_answers = ["in", "out", "shake", "hokey", "turn"]
#amateur_answers = 
levels = ["easy-peasy", "amateur", "almost pro", "the song-master"]

#def random_level():
#    random_num = randint(0,3)
#    if random_num == 0:
#        return "easy-peasy"
#    elif random_num == 1:
#        return "amateur"
#    elif random_num ==2:
#    	return "pro-wannabe"
#    else:
#    	return "song-master"

#def random_answer():
#	random_num = randint(0,2)
#	if random_num == 0:
#		return "in"
#	elif random_num == 1:
#	    return "out"
#	else:
#		return "shake"

def fill_in_the_blanks(level,sequence):
    global easy_song
    easy_song_split=[]
    replaced=[]
    if level=="easy-peasy":
        easy_song_split=easy_song.split()
        for word in easy_song_split:
        	replacement = "__" + str(sequence) + "__"
        	word = word.replace(replacement, easy_answers[sequence-1])
        	replaced.append(word)
        easy_song=" ".join(replaced)
        return easy_song

def wrong_chances(level,sequence,count,counter):
	while count<counter:
		if level == "easy-peasy":
			answer = raw_input("Err.. That's not the right lyric, try again! You have " + str(counter-count) + " chances left. What is your answer for __" + str(sequence+1) + "__? ")
			if answer == easy_answers[sequence]:
				sequence+=1
				break
			else:
				count+=1
		if count==counter:
			break
	return sequence


def easy(sequence,counter):
	count=0
	if sequence==0:
		answer = raw_input("You chose easy-peasy! Don't worry if you can't guess it right the first time, you have " + str(counter) + " chances to do it. Let's sing along! \n\n" + easy_song + "\n\n" + "What is your answer for __" + str(sequence+1) + "__? ")
		count+=1
		if answer==easy_answers[sequence]:
			return sequence+1
		else:
			sequence = wrong_chances("easy-peasy",sequence,count,counter)
			return sequence
	elif sequence==1:
		answer = raw_input("\nWhat is your answer for __" + str(sequence+1) + "__? ")
		count+=1
		if answer==easy_answers[sequence]:
			return sequence+1
		else:
			sequence = wrong_chances("easy-peasy",sequence,count,counter)
			return sequence
	elif sequence==2:
	    answer = raw_input("\nWhat is your answer for __" + str(sequence+1) + "__? ")
	    count+=1
	    if answer==easy_answers[sequence]:
	        return sequence+1
	    else:
	    	sequence = wrong_chances("easy-peasy",sequence,count,counter)
	        return sequence
	elif sequence==3:
	    answer = raw_input("\nWhat is your answer for __" + str(sequence+1) + "__? ")
	    count+=1
	    if answer==easy_answers[sequence]:
	        return sequence+1
	    else:
	    	sequence = wrong_chances("easy-peasy",sequence,count,counter)
	        return sequence
	elif sequence==4:
	    answer = raw_input("\nWhat is your answer for __" + str(sequence+1) + "__? ")
	    count+=1
	    if answer==easy_answers[sequence]:
	        return sequence+1
	    else:
	    	sequence = wrong_chances("easy-peasy",sequence,count,counter)
	        return sequence

def lets_sing_along():
	sequence=0
	level = raw_input("Let's sing along! \n\nChoose your level: \n easy-peasy \n amateur \n almost pro \n the song-master\n\n")
	counter = int(raw_input("Choose how many wrong answers we should spare you? Type any positive numbers. "))
	if level=="easy-peasy":
		new_sequence=easy(sequence,counter)
		if new_sequence==sequence:
			return "Game over! You had your chances, but it seems like you need to upgrade your songs database. Try again anytime you're ready! Thanks for playing!"
		else:
			print "You got that right!" + "\n\n" + fill_in_the_blanks(level,new_sequence)
			sequence=new_sequence
			new_sequence=easy(sequence,counter)
			if new_sequence==sequence:
				return "Game over! You had your chances, but it seems like you need to upgrade your songs database. Try again anytime you're ready! Thanks for playing!"
			else:
			    print "You got that right!" + "\n\n" + fill_in_the_blanks(level, new_sequence)
			    sequence=new_sequence
			    new_sequence=easy(sequence,counter)
			    if new_sequence==sequence:
			        return "Game over! You had your chances, but it seems like you need to upgrade your songs database. Try again anytime you're ready! Thanks for playing!"
			    else:
			        print "You got that right!" + "\n\n" + fill_in_the_blanks(level, new_sequence)
			        sequence=new_sequence
			        new_sequence=easy(sequence,counter)
			        if new_sequence==sequence:
			            return "Game over! You had your chances, but it seems like you need to upgrade your songs database. Try again anytime you're ready! Thanks for playing!"
			        else:
			            print "You got that right!" + "\n\n" + fill_in_the_blanks(level, new_sequence)
			            sequence=new_sequence
			            new_sequence=easy(sequence,counter)
			            if new_sequence==sequence:
			                return "Game over! You had your chances, but it seems like you need to upgrade your songs database. Try again anytime you're ready! Thanks for playing!"
			            else:
			                return "Congratulations! You did it! You are as good as my 4 years-old niece! Now, let's sing along!" +"\n\n" + fill_in_the_blanks(level, new_sequence)


print lets_sing_along()















