def make_album(artist_name, album_title, songs=None):
	if songs:
		music_album = {'artist': artist_name, 'album': album_title, 'songs': songs,}
	else:
		music_album = {'artist': artist_name, 'album': album_title,}
	return music_album

first_album = make_album('Gorillaz', 'Demon Days')
second_album = make_album('Linkin Park', 'Meteora')
third_album = make_album('U2', 'This is U2')
forth_album = make_album(album_title = 'Zelda&Chill', artist_name = 'Ninwave', 
	songs = 89)
print(first_album)
print(second_album)
print(third_album)
print(forth_album)