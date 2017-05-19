from random import randint

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

easy_answers = ["in", "out", "shake", "hokey", "turn"]
pro_answers = ["shape", "magnet", "falling", "body", "discovering"]
allround_answers = ["grace", "sweet", "wretch", "once", "found"]
legend_answers = ["look", "only", "extraordinary", "adore", "love", "game", "break", "made"]

levels = ["easy-peasy", "pro-wannabe", "all-rounder", "legend"]

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
    global easy_song, pro_song, allround_song, legend_song
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
    elif level=="pro-wannabe":
        pro_song_split=pro_song.split()
        for word in pro_song_split:
        	replacement = "__" + str(sequence) + "__"
        	word = word.replace(replacement, pro_answers[sequence-1])
        	replaced.append(word)
        pro_song=" ".join(replaced)
        return pro_song
    elif level=="all-rounder":
        allround_song_split=allround_song.split()
        for word in allround_song_split:
        	replacement = "__" + str(sequence) + "__"
        	word = word.replace(replacement, allround_answers[sequence-1])
        	replaced.append(word)
        allround_song=" ".join(replaced)
        return allround_song


def wrong_chances(level,sequence,count,counter):
	while count<counter:
		if level == "easy-peasy":
			answer = raw_input("\nErr.. That's not the right lyric, try again! You have " + str(counter-count) + " chances left. What is your answer for __" + str(sequence+1) + "__? ")
			if answer == easy_answers[sequence]:
				sequence+=1
				break
			else:
				count+=1
		elif level == "pro-wannabe":
			answer = raw_input("\nErr.. That's not the right lyric, try again! You have " + str(counter-count) + " chances left. What is your answer for __" + str(sequence+1) + "__? ")
			if answer == pro_answers[sequence]:
				sequence+=1
				break
			else:
				count+=1
		elif level == "all-rounder":
			answer = raw_input("\nErr.. That's not the right lyric, try again! You have " + str(counter-count) + " chances left. What is your answer for __" + str(sequence+1) + "__? ")
			if answer == allround_answers[sequence]:
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
		answer = raw_input("\nYou chose easy-peasy! Don't worry if you can't guess it right the first time, you have " + str(counter) + " chances to do it. Let's sing along! \n\n" + easy_song + "\n\n" + "What is your answer for __" + str(sequence+1) + "__? ")
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

def pro(sequence,counter):
	count=0
	if sequence==0:
		answer = raw_input("\nYou chose pro-wannabe! Don't worry if you can't guess it right the first time, you have " + str(counter) + " chances to do it. Let's sing along! \n\n" + pro_song + "\n\n" + "What is your answer for __" + str(sequence+1) + "__? ")
		count+=1
		if answer==pro_answers[sequence]:
			return sequence+1
		else:
			sequence = wrong_chances("pro-wannabe",sequence,count,counter)
			return sequence
	elif sequence==1:
		answer = raw_input("\nWhat is your answer for __" + str(sequence+1) + "__? ")
		count+=1
		if answer==pro_answers[sequence]:
			return sequence+1
		else:
			sequence = wrong_chances("pro-wannabe",sequence,count,counter)
			return sequence
	elif sequence==2:
	    answer = raw_input("\nWhat is your answer for __" + str(sequence+1) + "__? ")
	    count+=1
	    if answer==pro_answers[sequence]:
	        return sequence+1
	    else:
	    	sequence = wrong_chances("pro-wannabe",sequence,count,counter)
	        return sequence
	elif sequence==3:
	    answer = raw_input("\nWhat is your answer for __" + str(sequence+1) + "__? ")
	    count+=1
	    if answer==pro_answers[sequence]:
	        return sequence+1
	    else:
	    	sequence = wrong_chances("pro-wannabe",sequence,count,counter)
	        return sequence
	elif sequence==4:
	    answer = raw_input("\nWhat is your answer for __" + str(sequence+1) + "__? ")
	    count+=1
	    if answer==pro_answers[sequence]:
	        return sequence+1
	    else:
	    	sequence = wrong_chances("pro-wannabe",sequence,count,counter)
	        return sequence

def allround(sequence,counter):
	count=0
	if sequence==0:
		answer = raw_input("\nYou chose all-rounder! Don't worry if you can't guess it right the first time, you have " + str(counter) + " chances to do it. Let's sing along! \n\n" + allround_song + "\n\n" + "What is your answer for __" + str(sequence+1) + "__? ")
		count+=1
		if answer==allround_answers[sequence]:
			return sequence+1
		else:
			sequence = wrong_chances("all-rounder",sequence,count,counter)
			return sequence
	elif sequence==1:
		answer = raw_input("\nWhat is your answer for __" + str(sequence+1) + "__? ")
		count+=1
		if answer==allround_answers[sequence]:
			return sequence+1
		else:
			sequence = wrong_chances("all-rounder",sequence,count,counter)
			return sequence
	elif sequence==2:
	    answer = raw_input("\nWhat is your answer for __" + str(sequence+1) + "__? ")
	    count+=1
	    if answer==allround_answers[sequence]:
	        return sequence+1
	    else:
	    	sequence = wrong_chances("all-rounder",sequence,count,counter)
	        return sequence
	elif sequence==3:
	    answer = raw_input("\nWhat is your answer for __" + str(sequence+1) + "__? ")
	    count+=1
	    if answer==allround_answers[sequence]:
	        return sequence+1
	    else:
	    	sequence = wrong_chances("all-rounder",sequence,count,counter)
	        return sequence
	elif sequence==4:
	    answer = raw_input("\nWhat is your answer for __" + str(sequence+1) + "__? ")
	    count+=1
	    if answer==allround_answers[sequence]:
	        return sequence+1
	    else:
	    	sequence = wrong_chances("all-rounder",sequence,count,counter)
	        return sequence


def lets_sing_along():
	sequence=0
	level = raw_input("Let's sing along! \n\nChoose your level: \n easy-peasy \n pro-wannabe \n all-rounder \n legend\n\n")
	counter = int(raw_input("\nChoose how many wrong answers we should spare you? Type any positive numbers. "))
	if level=="easy-peasy":
		new_sequence=easy(sequence,counter)
		if new_sequence==sequence:
			return "\nGame over! You had your chances, but it seems like you need to upgrade your songs database. Try again anytime you're ready! Thanks for playing!\n"
		else:
			print "\nYou got that right!" + "\n\n" + fill_in_the_blanks(level,new_sequence)
			sequence=new_sequence
			new_sequence=easy(sequence,counter)
			if new_sequence==sequence:
				return "\nGame over! You had your chances, but it seems like you need to upgrade your songs database. Try again anytime you're ready! Thanks for playing!\n"
			else:
			    print "\nYou got that right!" + "\n\n" + fill_in_the_blanks(level, new_sequence)
			    sequence=new_sequence
			    new_sequence=easy(sequence,counter)
			    if new_sequence==sequence:
			        return "\nGame over! You had your chances, but it seems like you need to upgrade your songs database. Try again anytime you're ready! Thanks for playing!\n"
			    else:
			        print "\nYou got that right!" + "\n\n" + fill_in_the_blanks(level, new_sequence)
			        sequence=new_sequence
			        new_sequence=easy(sequence,counter)
			        if new_sequence==sequence:
			            return "\nGame over! You had your chances, but it seems like you need to upgrade your songs database. Try again anytime you're ready! Thanks for playing!\n"
			        else:
			            print "\nYou got that right!" + "\n\n" + fill_in_the_blanks(level, new_sequence)
			            sequence=new_sequence
			            new_sequence=easy(sequence,counter)
			            if new_sequence==sequence:
			                return "\nGame over! You had your chances, but it seems like you need to upgrade your songs database. Try again anytime you're ready! Thanks for playing!\n"
			            else:
			                return "\nCongratulations! You did it! You are as good as my 4 years-old niece! Now, let's sing along!" +"\n\n" + fill_in_the_blanks(level, new_sequence) + "\n"
	elif level=="pro-wannabe":
		new_sequence=pro(sequence,counter)
		if new_sequence==sequence:
			return "\nGame over! You had your chances, but it seems like you need to upgrade your songs database. Try again anytime you're ready! Thanks for playing!\n"
		else:
			print "\nYou got that right!" + "\n\n" + fill_in_the_blanks(level,new_sequence)
			sequence=new_sequence
			new_sequence=pro(sequence,counter)
			if new_sequence==sequence:
				return "\nGame over! You had your chances, but it seems like you need to upgrade your songs database. Try again anytime you're ready! Thanks for playing!\n"
			else:
			    print "\nYou got that right!" + "\n\n" + fill_in_the_blanks(level, new_sequence)
			    sequence=new_sequence
			    new_sequence=pro(sequence,counter)
			    if new_sequence==sequence:
			        return "\nGame over! You had your chances, but it seems like you need to upgrade your songs database. Try again anytime you're ready! Thanks for playing!\n"
			    else:
			        print "\nYou got that right!" + "\n\n" + fill_in_the_blanks(level, new_sequence)
			        sequence=new_sequence
			        new_sequence=pro(sequence,counter)
			        if new_sequence==sequence:
			            return "\nGame over! You had your chances, but it seems like you need to upgrade your songs database. Try again anytime you're ready! Thanks for playing!\n"
			        else:
			            print "\nYou got that right!" + "\n\n" + fill_in_the_blanks(level, new_sequence)
			            sequence=new_sequence
			            new_sequence=pro(sequence,counter)
			            if new_sequence==sequence:
			                return "\nGame over! You had your chances, but it seems like you need to upgrade your songs database. Try again anytime you're ready! Thanks for playing!\n"
			            else:
			                return "\nCongratulations! You did it! But, don't you think it was too easy? I mean, come on, everybody knows Ed Sheeran's songs! Try the next level if you think you are that good ;) Now, let's sing along!" +"\n\n" + fill_in_the_blanks(level, new_sequence) + "\n"
	elif level=="all-rounder":
		new_sequence=allround(sequence,counter)
		if new_sequence==sequence:
			return "\nGame over! You had your chances, but it seems like you need to upgrade your songs database. Try again anytime you're ready! Thanks for playing!\n"
		else:
			print "\nYou got that right!" + "\n\n" + fill_in_the_blanks(level,new_sequence)
			sequence=new_sequence
			new_sequence=allround(sequence,counter)
			if new_sequence==sequence:
				return "\nGame over! You had your chances, but it seems like you need to upgrade your songs database. Try again anytime you're ready! Thanks for playing!\n"
			else:
			    print "\nYou got that right!" + "\n\n" + fill_in_the_blanks(level, new_sequence)
			    sequence=new_sequence
			    new_sequence=allround(sequence,counter)
			    if new_sequence==sequence:
			        return "\nGame over! You had your chances, but it seems like you need to upgrade your songs database. Try again anytime you're ready! Thanks for playing!\n"
			    else:
			        print "\nYou got that right!" + "\n\n" + fill_in_the_blanks(level, new_sequence)
			        sequence=new_sequence
			        new_sequence=allround(sequence,counter)
			        if new_sequence==sequence:
			            return "\nGame over! You had your chances, but it seems like you need to upgrade your songs database. Try again anytime you're ready! Thanks for playing!\n"
			        else:
			            print "\nYou got that right!" + "\n\n" + fill_in_the_blanks(level, new_sequence)
			            sequence=new_sequence
			            new_sequence=allround(sequence,counter)
			            if new_sequence==sequence:
			                return "\nGame over! You had your chances, but it seems like you need to upgrade your songs database. Try again anytime you're ready! Thanks for playing!\n"
			            else:
			                return "\nCongratulations! You did it! Not bad, not bad at all! Try the next level if you dare ;) Now, let's sing along!" +"\n\n" + fill_in_the_blanks(level, new_sequence) + "\n"

print lets_sing_along()















