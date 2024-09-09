from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

class Application:
    def __init__(self, choice):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self.choice = choice
# Seed with some seed data
        self._connection.seed("seeds/music_library.sql")

    def run(self):

        if self.choice == 1:

            artist_repository = ArtistRepository(self._connection)
            artists = artist_repository.all()

# List them out
            for artist in artists:
                print(f"{artist.id}: {artist.name} ({artist.genre})")

        elif self.choice == 2:
# Retrieve all albums
            album_repository = AlbumRepository(self._connection)
            albums = album_repository.all()

#List them out

            for album in albums:
                print(f"{album.id}: {album.title} ({album.release_year}, {album.artist_id})")


# Retrieving and printing just one album
#Using find method

if __name__ == '__main__':
    app = Application(2)
    app.run()




