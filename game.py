from sys import exit
import textwrap

print " _/_/_/_/    _/_/_/_/     _/_/    _/_/_/_/_/    _/      _/"
print " _/    _/    _/          _/  _/       _/        _/      _/"
print " _/    _/    _/_/_/     _/    _/      _/        _/_/_/_/_/"
print " _/    _/    _/        _/_/_/_/_/     _/        _/      _/"
print " _/_/_/_/    _/_/_/_/  _/       _/    _/        _/      _/ _/_/_/"
print "                                                          "
print "                                                          "

#Where all the items found are stored.
backpack = []

#the second larger room
def second_room():
	class Style:
		BOLD = "\033[1m"
		END = "\033[0m"
	print "You are now in a greate hall called The Inner Sanctum."
	print "A familiar face is seen on the wall. You hear him speak:"
	print "        _ooOoo_         "
	print "       O8888888O        "
	print "      88\"  .  \"88      "
	print "      (| - _ - |)       "
	print "      O\   =   /O       "
	print "    ___/`_ _ _'\___     "
	print "   / \\|       |// \    "
	print "                        "
	print Style.BOLD+"Answer me this riddle or all will be lost!!!"+Style.END
	print Style.BOLD+"What is that which has one voice and yet becomes four-footed and two-footed and three-footed?"+Style.END
	choice = raw_input(">")
	
	if "human beign" in choice:
		text1 = "The room is lit by the multiple torches lighing up.A symbol is drawn upon the face..."
		print textwrap.fill(text1)
		print "Insert symbol here"
		print "What will you do?"
		choice = raw_input(">")
		
		if "touch" in choice:
			text2 = "The symbol lights up and a red sphere is replaced. You take it."
			print textwrap.fill(text2)
			backpack.append("sphere")
		elif "touch symbol" in choice:
			text2 = "The symbol lights up and a red sphere is replaced. You take it."
			print textwrap.fill(text2)
			backpack.append("sphere")
		else:
			second_room()
			

	elif "human" in choice:
		text1 = "The room is lit by the multiple torches lighing up.A symbol is drawn upon the face..."
		print textwrap.fill(text1)
		print "Insert symbol here"
		print "What will you do?"
		choice = raw_input(">")
		
		if "touch" in choice:
			text2 = "The symbol lights up and a red sphere is replaced. You take it."
			print textwrap.fill(text2)
			backpack.append("sphere")
		elif "touch symbol" in choice:
			text2 = "The symbol lights up and a red sphere is replaced. You take it."
			print textwrap.fill(text2)
			backpack.append("sphere")
		else:
			second_room()
			
		
	else:
		print "Your trial end here. All lights shutdown and you sit in darkness."
		dead("Starvation and thirst gets to you.")
	
	
#front air room
def front_room():
	text_wrap = "You've entered the Air room.The door behind you slams shut and the only option is to move ahead.You barely could analise the room but are captured by someone and\nthey put a veil over your head.\"You stand on the edge of the abyss. One step and you shall fall\".As soon as they strip the veil from your head a wierd contraption swirls in front of you.How will you react. You..."
	print textwrap.fill(text_wrap)
	choice = raw_input(">")
	
	if "dodge" in choice:
		print "...dodge the blades that could have otherwise slit your throat."
		print "There was no cliff, it was all a test."
		print "In front of you see a corridor that leads somewhere. Will you stay and explore or continue."
		choice = raw_input(">")
		
		if "continue" in choice:
			print "Unaware you set foot on a trap. You bleed severely"
			dead("An ill fortune ahas befell upon you.\n")
		elif "explore" in choice:
			print "Looking around you observe that on the ground a traps."
			print "With coution you continue towards the corridor and your eyes stumble something\nwritten on the wall."
			print "----------------------------------------------------------"
			print "I am free for the taking through all of your life,\nThough given but once at birth.\nI am less than nothing in weight,\nBut will fell the strongest of you if held."
			print "----------------------------------------------------------"
			choice = raw_input(">")
			
			if "breath" in choice:
				print "All the traps are disable and I think is safe to walk to the exit..."
				print "...but one particular trap explodes letting you see a bottle hidden within. You take it."
				backpack.append("bottle")
				second_room()
			else:
				print "The room start fillig with noxios gas, blood starts gosing through your skin."
				dead("What a fate to be had.\n")
	elif "crouch" in choice:
		print "...crouch and evade the blades that could have otherwise slit your throat."
		print "There was no cliff, it was all a test."
		print "In front of you see a corridor that leads somewhere. Will you stay and explore or continue."
		choice = raw_input(">")
		
		if "continue" in choice:
			print "Unaware you set foot on a trap. You bleed severely"
			dead("An ill fortune ahas befell upon you.\n")
		elif "explore" in choice:
			print "Looking around you observe that on the ground a traps."
			print "With coution you continue towards the corridor and your eyes stumble something\nwritten on the wall."
			print "----------------------------------------------------------"
			print "I am free for the taking through all of your life,\nThough given but once at birth.\nI am less than nothing in weight,\nBut will fell the strongest of you if held."
			print "----------------------------------------------------------"
			choice = raw_input(">")
			
			if "breath" in choice:
				print "All the traps are disable and I think is safe to walk to the exit..."
				print "...but one particular trap explodes letting you see a bottle hidden within. You take it."
				backpack.append("bottle")
				second_room()
			else:
				print "The room start fillig with noxios gas, blood starts gosing through your skin."
				dead("What a fate to be had.\n")
	elif "attack" in choice:
		print " attack but the machine is to powerfull and the blades cut through you like butter."
		dead("What a blood bath.\n")
	elif "stand still" in choice:
		print "...stand still and the blades barely touch you. Your calm has rewarded you."
		print "There was no cliff, it was all a test."
		print "In front of you see a corridor that leads somewhere. Will you stay and explore or continue."
		choice = raw_input(">")
		
		if "continue" in choice:
			print "Unaware you set foot on a trap. You bleed severely"
			dead("An ill fortune ahas befell upon you.\n")
		elif "explore" in choice:
			print "Looking around you observe that on the ground a traps."
			print "With coution you continue towards the corridor and your eyes stumble something\nwritten on the wall."
			print "----------------------------------------------------------"
			print "I am free for the taking through all of your life,\nThough given but once at birth.\nI am less than nothing in weight,\nBut will fell the strongest of you if held."
			print "----------------------------------------------------------"
			choice = raw_input(">")
			
			if "breath" in choice:
				print "All the traps are disable and I think is safe to walk to the exit..."
				print "...but one particular trap explodes letting you see a bottle hidden within. You take it."
				backpack.append("bottle")
				second_room()
			else:
				print "The room start fillig with noxios gas, blood starts gosing through your skin."
				dead("What a fate to be had.\n")
	elif "stay calm" in choice:
		print "...stay calm and the blades barely touch you. Your calm has rewarded you."
		print "There was no cliff, it was all a test."
		print "In front of you see a corridor that leads somewhere. Will you stay and explore or continue."
		choice = raw_input(">")
		
		if "continue" in choice:
			print "Unaware you set foot on a trap. You bleed severely"
			dead("An ill fortune has befell upon you.\n")
		elif "explore" in choice:
			print "Looking around you observe that on the ground a traps."
			print "With coution you continue towards the corridor and your eyes stumble something\nwritten on the wall."
			print "----------------------------------------------------------"
			print "I am free for the taking through all of your life,\nThough given but once at birth.\nI am less than nothing in weight,\nBut will fell the strongest of you if held."
			print "-----------------------------------------------------------"
			choice = raw_input(">")
			
			if "breath" in choice:
				print "All the traps are disable and I think is safe to walk to the exit..."
				print "...but one particular trap explodes letting you see a bottle hidden within. You take it."
				backpack.append("bottle")
				second_room()
			else:
				print "The room start fillig with noxios gas, blood starts gosing through your skin."
				dead("What a fate to be had.\n")
	elif "move back" in choice:
		text_wrap = "As you step back you feel something different while touching the ground. You could lift your foot but you may become unbalanced and hit the blades or you could continue to place your foot gently on the ground and hope it\'s nothing."
		print textwrap.fill(text_wrap)
		choice = raw_input(">")
		
		if "lift foot" in choice:
			text= "Your instinct was right, it was a trap that could slash your foot. The mechanism was a blade swirling, head slashing contraption, you\'re lucky you\'re still alive. There was no cliff, it was all a test. In front of you see a corridor that leads somewhere. Will you stay and explore or continue."
			print textwrap.fill(text)
			choice = raw_input(">")
		
			if "continue" in choice:
				print "Unaware you set foot on a trap. You bleed severely"
				dead("An ill fortune has befell upon you.\n")
			elif "explore" in choice:
				print "Looking around you observe that on the ground a traps."
				print "With coution you continue towards the corridor and your eyes stumble something\nwritten on the wall."
				print "----------------------------------------------------------"
				print "I am free for the taking through all of your life,\nThough given but once at birth.\nI am less than nothing in weight,\nBut will fell the strongest of you if held."
				print "-----------------------------------------------------------"
				choice = raw_input(">")
			
				if "breath" in choice:
					print "All the traps are disable and I think is safe to walk to the exit..."
					print "...but one particular trap explodes letting you see a bottle hidden within. You take it."
					backpack.append("bottle")
					second_room()
				else:
					print "The room start fillig with noxios gas, blood starts gosing through your skin."
					dead("What a fate to be had.\n")
		elif "continue" in choice:
			dead("You should have listen to your instinct. Your foot has been slashed by the trap in which you steped. You bleed...")
			
	else:
		front_room()
		
#the continuation of the right room
def next_section_right_room():
	print "You feel to the ground after almost loosing hope\nof ever seeing the shore. You were guided by the dim light that stood next to a wall."
	print "Now you could see that the wall had an image on it. A mozaic showing the figure of a fish."
	print "You also see a corridor. Will you continue or stop to look around?"
	choice = raw_input(">")
	
	if "continue" in choice:
		second_room
	elif "look around" in choice:
		print "Your coriosity is fruitfull and you see a writing on the wall."
		print "Lighter than what I am made of,\nMore of me is hidden than is seen,\nI am the bane of the mariner,\nA tooth within the sea.\nSpeak my name. "
		choice = raw_input(">")
		
		if "ice" in choice:
			print "You verbalize the answer and a sword is seen to rise from the grownd.\nYou take it."
			backpack.append("Sword")
			print "You now have a %s and procced to on to the corridor."% backpack[0]
			second_room()
		else:
			dead("Spikes burst from beneath you, killing you instantly.")
	else:
		dead("You wasted your life.\n")
			
			
#Water room
def right_room():
	print "You've entered the Water room."
	print "The door behind you slams shut and the only option is to move ahead"
	print "A vast ocean like vista sits in front of you."
	print "Will you swim across or look around you?"
	choice = raw_input(">")
	
	if "look around" in choice:
		print "You found a some wood and rope. Maybe you could make a raft?"
		backpack.append("wood and rope")
		print "You use the %s to make the raft"% backpack[0]
		backpack.pop(0)
		print "You raft floats perfectly and after a long time you finnaly reach the end."
		next_section_right_room()
	elif "swim across" in choice:
		print "You plunge in the vastness of the ocean only to find out that it was\na meter deep."
		print "You laughted of this trickery and began crossing it."
		next_section_right_room()
	elif "swim" in choice:
		print "You plunge in the vastness of the ocean only to find out that it was\na meter deep."
		print "You laughted of this trickery and began crossing it."
		next_section_right_room()
	else:
		dead("You should have listen to your destiny.\n")
		

#the continuation of the left_room	
def next_section_left_room():
	text_wrap = "It was all an illusion!The fire was an illusion, when you stepped on the platform in front of you\n nothing happend. Amazed by your courage you see a chest in front of you. Inside of it you behold a card with a picture. A man wielding a sword called \"The Soldier\". You take it"
	print textwrap.fill(text_wrap)
	backpack.append("The Soldier")
	print "You now have the card %s" %backpack[0]
	print "A corridor paved with beautiful mozaic and an exquisite painting can be seen in front of you ."
	print "You master the courage and continue."
	choice = raw_input(">")
	
	if "continue" in choice:
		second_room()
	elif "move ahead" in choice:
		second_room()
	else:
		dead("You should have listen to your destiny.\n")
		
		
#Fire room
def left_room():
	print "You've entered the Fire room."
	print "All the room in front of you is burning."
	print "The door behind you slams shut and the only option is to move ahead"
	
	choice = raw_input(">")
	
	if "ahead" in choice:
		next_section_left_room()
	elif "move ahead" in choice:
		next_section_left_room()
	elif "move" in choice:
		next_section_left_room()
	else:
		dead("You starve and die.\n")
		
		
#The first room	
def enter():
	print "You couldn't resist the urge to follow the light."
	print "The smell of old and ancient air fills the room."
	print "Three torches light up the room showing you three doors."
	print "Each room has three symbols.The one on the left has fire,"
	print "the one on the right has water and the one in front has air."
	print "Where will you go?"
	
	choice = raw_input(">")
	
	if "left" in choice:
		left_room()
	elif "right" in choice:
		right_room()
	elif "front" in choice:
		front_room()
	else:
		dead("Don't understand.\n")
		
def stay():
	print "You decided to stay in this world."
	print "But how long will you resist this?"
	print "At the bottom of the piramid you see light getting bigger."
	print "You feel atracted by it, will you resist?"
	
	choice = raw_input(">")
	
	if "no" in choice:
		enter()
	elif "No" in choice:
		enter()
	elif "Yes" in choice:
		dead("Bye.")
	elif "yes" in choice:
		dead("Bye.")
	else:
		dead("Don't understand.\n")

def dead(why):
	print why, "Game Over"
	exit(0)

def start():
	print "You didn't know how you got here. All you can remember\nis that you went to sleep."
	print "You are now fully woke up and in front of you you see a vast desert,\nit's night and the Moon is bright red."
	print "A piramid stands in this gloomy new world you are in. Are you dreaming?"
	print "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
	print "|||||||||||||||||||||||||||||||||/\||||||||||||||||||||||||||||||||||"
	print "|||||****|||||||||||||||||||||||/  \|||||||||||||||||||||||||||||||||"
	print "||||******|||||||||||||||||||||/    \||||||||||||||||||||||||||||||||"
	print "||||******||||||||||||||||||||/      \|||||||||||||||||||||||||||||||"
	print "|||||****||||||||||||||||||||/        \||||||||||||||||||||||||||||||"
	print "||||||||||||||||||||||||||||/          \|||||||||||||||||||||||||||||"
	print "|||||||||||||||||||||||||||/            \||||||||||||||||||||||||||||"
	print "||||||||||||||||||||||||||/              \|||||||||||||||||||||||||||"
	print "|||||||||||||||||||||||||/________________\||||||||||||||||||||||||||"
	print "---------------------------------------------------------------------"
	print "---------------------------------------------------------------------"
	print "Do you wanna wake up?"
	
	choice = raw_input(">")
	
	if "no" in choice:
		stay()
	elif "No" in choice:
		stay()
	elif "Yes" in choice:
		dead("You awoke.")
	elif "yes" in choice:
		dead("You awoke.")
	else:
		dead("Don't understand.\n")

start()