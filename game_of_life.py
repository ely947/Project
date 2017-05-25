from gol import GOL_DICTIONARY

def show_topic(question,options_dictionary):
	"""Prints the question, and options"""
	print question
	for option in sorted(options_dictionary):
		print option, options_dictionary[option]

def get_next_topic(topic, sub_topic):
	user_input = raw_input(">> ").upper()
	return GOL_DICTIONARY["INTRO"]["Options"][user_input].upper()

def get_answer_key():
	user_input = raw_input(">> ").upper()
	return user_input

def keep_going():
	keep_going_input = raw_input("Do you want to play again? ").lower()
	if keep_going_input == "yes":
		return True
	else:
		print "Bye Felicia!"
		return False

print "Welcome to the game of life! The goal of the game is to get to know Alice a little better."
topic = "INTRO"
sub_topic = "Options"

while True:
	show_topic("What are you interested in learning about?", GOL_DICTIONARY[topic][sub_topic])
	topic = get_next_topic(topic, sub_topic)
	sub_topic = "Options"
	show_topic("Awesome! What would you like to know about that topic?", GOL_DICTIONARY[topic][sub_topic])
	answer_key = get_answer_key()
	print(GOL_DICTIONARY[topic]['Answers'][answer_key])
	if keep_going() == True:
		topic = "INTRO"
		sub_topic = "Options"
		continue
	else:
		break


# lets_play = raw_input("Are you ready to play the game of Alice's life? ")

# if lets_play == "yes":
# 	print ("Welcome to the game of Alice's life. The object of the game is to "
# 	"get to know Alice a little better and have fun. ")
	
# 	while True:
# 		main_menu = raw_input("Where do you want to start?\n"

# 		"A. Traveling experiences\n"
# 		"B. Career decisions\n"
# 		"C. Extracurricular activities\n"
# 		"D. Nevermind, I don't want to play right now\n"

# 		)
# 		if  main_menu == "D":
# 			break
	
# 		elif main_menu == "A":
# 			traveling_menu = raw_input("""Awesome! I've been lucky to have some
# amazing traveling experiences, which do you want to learn more about?

# 				1. Volunteering in Ghana
# 				2. Studying in Prague
# 				3. Teaching in Thailand 
# 				4. Opps, I made the wrong choice, take me back to the main menu

# 				""")

# 			if traveling_menu == "1":
# 				print """Cool! Let me tell you about Ghana..."""

# 			elif traveling_menu == "2":
# 				print """Prague! Where to begin..."""

# 			elif traveling_menu == "3":
# 				print """Thailand! Such a beautiful place"""

# 			else:
# 				main_menu

# 		elif main_menu == "B":
# 			career_menu = raw_input("""/nWork, work, work, work, work. What choice do you want to
# 				dive into?

# 				1. To teach or not to teach
# 				2. Nonprofit or tech
# 				3. Product vs. sales

# 				""")

# 			if career_menu == "1":
# 				print """Learning to teach the hard way..."""

# 			elif career_menu == "2":
# 				print """Finding a job where you can give back and have intellectual stimulation."""

# 			elif career_menu == "3":
# 				print """Getting sold on product"""

# 			else:
# 				main_menu

# 		elif main_menu == "C":
# 			extracurricular_menu = raw_input("""These are a few of my favorite things! Which do you want
# 				to know more about?

# # 				1. Big Brothers Big Sisters
# # 				2. Women's rights
# # 				3. Product vs. sales

# # 				""")

# # 			if extracurricular_menu == "1":
# # 				print """Envee is the coolest chick you'll ever meet."""

# # 			elif extracurricular_menu == "2":
# # 				print """I'm from a family of four women. I'm a proud feminist!"""

# # 			elif extracurricular_menu == "3":
# # 				print """Coding is how I made this game!"""

# # 			else:
# # 				main_menu


	
