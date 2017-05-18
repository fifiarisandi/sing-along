from random import randint

easy_song = '''You put your right hand __1__, you take your right hand __2__, 
			you put your right hand __1__, and you __3__ it all about.
			You do the __4__ pokey, and you __5__ yourself around.
			That's what it's all about!'''

easy_answers = ["in", "out", "shake", "hokey", "turn"]
#amateur_answers = 
levels = ["easy-peasy", "amateur", "pro-wannabe", "song-master"]

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

def random_answer():
	random_num = randint(0,2)
	if random_num == 0:
		return "in"
	elif random_num == 1:
	    return "out"
	else:
		return "shake"

def fill_in_the_blanks(level,sequence):
    global easy_song
    easy_song_split=[]
    replaced=[]
    if level=="easy-peasy":
        easy_song_split=easy_song.split()
        for word in easy_song_split:
            if str(sequence) in word:
                word=word.replace(word, easy_answers[sequence-1])
                replaced.append(word)
            else:
                replaced.append(word)
        easy_song=" ".join(replaced)
        return easy_song

def easy(sequence):
	if sequence==0:
		print "You chose easy-peasy. Don't worry if you can't guess it right the first time, you have 3 chances to do it. Let's sing along! \n" + easy_song + "\n" + "What is the answer for__1__?"
		#answer=random_answer()
		answer="in"
		if answer==easy_answers[sequence]:
			return sequence+1
		else:
			return sequence
	elif sequence==1:
		print easy_song + "\n" + "What is the answer for __2__?"
		#answer=random_answer()
		answer="out"
		if answer==easy_answers[sequence]:
			return sequence+1
		else:
			return sequence
	elif sequence==2:
	    print easy_song + "\n" + "What is the answer for __3__?"
	    answer="shake"
	    if answer==easy_answers[sequence]:
	        return sequence+1
	    else:
	        return sequence
	elif sequence==3:
	    print easy_song + "\n" + "What is the answer for __4__?"
	    answer="hokey"
	    if answer==easy_answers[sequence]:
	        return sequence+1
	    else:
	        return sequence
	elif sequence==4:
	    print easy_song + "\n" + "What is the answer for __5__?"
	    answer="turn"
	    if answer==easy_answers[sequence]:
	        return sequence+1
	    else:
	        return sequence

def lets_sing_along():
	sequence=0
	#level=random_level
	level="easy-peasy"
	if level=="easy-peasy":
		new_sequence=easy(sequence)
		if new_sequence==sequence:
			return "That's not the right word, sorry!"
		else:
			print "You got that right!" + "\n" + fill_in_the_blanks(level,new_sequence)
			sequence=new_sequence
			new_sequence=easy(sequence)
			if new_sequence==sequence:
				return "That's not the right word, sorry!"
			else:
			    print "You got that right!" + "\n" + fill_in_the_blanks(level, new_sequence)
			    sequence=new_sequence
			    new_sequence=easy(sequence)
			    if new_sequence==sequence:
			        return "That's not the right word, sorry!"
			    else:
			        print "You got that right!" + "\n" + fill_in_the_blanks(level, new_sequence)
			        sequence=new_sequence
			        new_sequence=easy(sequence)
			        if new_sequence==sequence:
			            return "That's not the right word, sorry!"
			        else:
			            print "You got that right!" + "\n" + fill_in_the_blanks(level, new_sequence)
			            sequence=new_sequence
			            new_sequence=easy(sequence)
			            if new_sequence==sequence:
			                return "That's not the right word, sorry!"
			            else:
			                return "Congratulations! You did it as good as my 4 years-old niece did! Let's sing along!" +"\n" + fill_in_the_blanks(level, new_sequence)


print lets_sing_along()















