lets_play = raw_input("Are you ready to play the game of Alice's life? ")

if lets_play == "yes":
	print "Wahoo! Get ready for a wild ride!"
	
	tech_or_npo = raw_input("One of Alice's first big decisions was whether to seek out a job in the non-profit sector or in tech. Which did she choose? ")
	
	if tech_or_npo == "tech":
		print "Yep! I choose tech because I believed I could make a more sustainable impact by working at a social innovation company rather than being reliant on the charity of others to improve the world."
		
		sales_or_product = raw_input("After working as an account manager for a couple of years, I began doing project management work on the side. When one of the sales managers left, I was given the opportunity to move into her role. Project management was closer to the technical side of the business while the other opportunity was a promotion within the sales org. Which did I choose? ")

		if sales_or_product == "sales":
			print "No way jose. I quickly got bored of the sales aspect of my job. While I loved working with customers, I didn't feel I was intellectually stimulated. Learning about product, design and engineering, on the other hand, was always exciting to me. In my project management role I took over the QA and feedback process. I investigated bugs, listened to customers, and organized bugs and feedback in a way that encouraged action. Instead of providing lip service, I finally felt like I could make a difference for the customer. "
		else:
			print "You're right! In my product management role, I took over the QA and feedback process. I investigated bugs, listened to customers, and organized bugs and feedback in a way that encouraged action. Instead of providing lip service, I finally felt like I could make a difference for the customer."

	else:
		print "No. I decided against pursuing a career in the nonprofit industry because many nonprofit positions are focused on raising money. I hate money, and I especially hate asking for it!"
else:
	print "Bummer. Maybe next time!"

	
