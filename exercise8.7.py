def make_album(artist, title, songs=None):
    """Return a dictionary describing a music album."""
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album


album_1 = make_album('taylor swift', 'red')
album_2 = make_album('keshi', 'the reaper')
album_3 = make_album('olivia rodrigo', 'you seem pretty sad for a girl so in love', songs=13)

print(album_1)
print(album_2)
print(album_3)