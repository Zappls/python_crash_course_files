magicians = ['alice', 'david', 'carolina']  #defining the list.
for magician in magicians:  # defining the for loop. Tells python to take a name and gives it the variable magician.
	print(magician)  #prints the name that has just been assigned.
# or
magicians = ['alice', 'david', 'carolina']  #defining the list.
for magician in magicians:  # defining the for loop. Tells python to take a name and gives it the variable magician.
	print(f"\n{magician.title()}, that was a great trick" ) #prints the name that has just been assigned with a message.
	print(f"I can't wait to see your next trick, {magician.title()}.")
print("\nThank you, everyone. That was a great magic show!")