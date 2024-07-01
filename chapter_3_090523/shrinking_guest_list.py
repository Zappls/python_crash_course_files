guests = ['Ceasar', 'Alexander the Great', 'Chester Bennington']
invitation = f"\tDear {guests[0].title().strip()},\n\tI would be most honored if you would come to my dinner party next Sunday at 6pm.\n\tYours, Wolfger Alexander"
print(invitation)
invitation = f"\tDear {guests[1].title().strip()},\n\tI would be most honored if you would come to my dinner party next Sunday at 6pm.\n\tYours, Wolfger Alexander"
print(invitation)
invitation = f"\tDear {guests[2].title().strip()},\n\tI would be most honored if you would come to my dinner party next Sunday at 6pm.\n\tYours, Wolfger Alexander"
print(invitation)
print(guests[2],"is at a concert and can't come.")
absent = guests.pop()
guests.append('God')
invitation = f"\tDear {guests[0].title().strip()},\n\tI would be most honored if you would come to my dinner party next Sunday at 6pm.\n\tYours, Wolfger Alexander"
print(invitation)
invitation = f"\tDear {guests[1].title().strip()},\n\tI would be most honored if you would come to my dinner party next Sunday at 6pm.\n\tYours, Wolfger Alexander"
print(invitation)
invitation = f"\tDear {guests[2].title().strip()},\n\tI would be most honored if you would come to my dinner party next Sunday at 6pm.\n\tYours, Wolfger Alexander"
print(invitation)
print("\nI just found a bigger dinner table, so now more space is available.")
guests.insert(0, 'Heinz Aspernig')
guests.insert(2, 'Maria Wolfger')
guests.append('Saitama')
invitation = f"\tDear {guests[0].title().strip()},\n\tI would be most honored if you would come to my dinner party next Sunday at 6pm.\n\tYours, Wolfger Alexander"
print(invitation)
invitation = f"\tDear {guests[1].title().strip()},\n\tI would be most honored if you would come to my dinner party next Sunday at 6pm.\n\tYours, Wolfger Alexander"
print(invitation)
invitation = f"\tDear {guests[2].title().strip()},\n\tI would be most honored if you would come to my dinner party next Sunday at 6pm.\n\tYours, Wolfger Alexander"
print(invitation)
invitation = f"\tDear {guests[3].title().strip()},\n\tI would be most honored if you would come to my dinner party next Sunday at 6pm.\n\tYours, Wolfger Alexander"
print(invitation)
invitation = f"\tDear {guests[4].title().strip()},\n\tI would be most honored if you would come to my dinner party next Sunday at 6pm.\n\tYours, Wolfger Alexander"
print(invitation)
invitation = f"\tDear {guests[5].title().strip()},\n\tI would be most honored if you would come to my dinner party next Sunday at 6pm.\n\tYours, Wolfger Alexander"
print(invitation)
print("I'm a terrible host, and can only invite 2 people after all.")
print(guests)
popped = guests.pop()
uninvite = f"\tDear {popped.title().strip()}, the dinner table didn't arrive in time so you can't come.\n\tI'm very sorry.\n"
print(uninvite)
print(guests)
popped = guests.pop()
uninvite = f"\tDear {popped.title().strip()}, the dinner table didn't arrive in time so you can't come.\n\tI'm very sorry.\n"
print(uninvite)
print(guests)
popped = guests.pop()
uninvite = f"\tDear {popped.title().strip()}, the dinner table didn't arrive in time so you can't come.\n\tI'm very sorry.\n"
print(uninvite)
print(guests)
popped = guests.pop()
uninvite = f"\tDear {popped.title().strip()}, the dinner table didn't arrive in time so you can't come.\n\tI'm very sorry.\n"
print(uninvite)
confirmation = f"\tDear {guests[0].title().strip()},\n\tyou are still invited."
print(confirmation)
confirmation = f"\tDear {guests[1].title().strip()},\n\tyou are still invited."
print(confirmation)
del guests[0]
del guests[0]
print(guests)


