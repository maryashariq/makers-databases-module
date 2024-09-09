from lib.album import Album

"""
Album constructs with an id, title, and artist id
"""

def test_album_constructs():
    album = Album(1, 'Test Album', 1111, 1)
    assert album.id == 1
    assert album.title == 'Test Album'
    assert album.release_year == 1111
    assert album.artist_id == 1

"""
Formats albums to strings nicely
"""

def test_albums_format_nicely():
    album = Album(1, 'Test Album', 1111, 1)
    assert str(album) == "Album(1, Test Album, 1111, Artist ID: 1)"

"""
Compare two identical albums
And have them be equal
"""

def test_albums_are_equal():
    album1 = Album(1, 'Test Album', 1111, 1)
    album2 = Album(1, 'Test Album', 1111, 1)
    assert album1 == album2