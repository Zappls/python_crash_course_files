def make_album(artist_name, album_title, songs=None):
	if songs:
		music_album = {'artist': artist_name, 'album': album_title, 'songs': songs,}
	else:
		music_album = {'artist': artist_name, 'album': album_title,}
	return music_album


while True:
	print("Type 'quit' at any point to quit.")
	artist = input("Enter an artist's name: ")
	if artist == 'quit':
		break
	title = input("Enter one of their albums: ")
	if title == 'quit':
		break
	number = input("Enter the number of songs the album has or type in 'no' if "
		"you don't want to specify: ")
	if number == 'quit':
		break
	elif number == 'no':
		user_album = make_album(artist, title)
	else:
		songs = int(number)
		user_album = make_album(artist, title, songs)
	print(user_album)
