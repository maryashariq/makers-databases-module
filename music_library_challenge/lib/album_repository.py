from lib.album import Album

class AlbumRepository():

    #Initialise database connection
    def __init__(self, connection):
        self._connection = connection
    
    #Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        
        for row in rows:
            item = Album(row["id"], row["title"],row["release_year"], row["artist_id"])
            albums.append(item)

        return albums
    
    #Find a single album by its id

    def find(self, album_id):
        rows = self._connection.execute(
            'SELECT * from albums WHERE id = %s', [album_id])
        row = rows[0] # row[0] because it only returns 1 row but we need to extract it
        return Album(row["id"],row["title"], row["release_year"], row["artist_id"])
    
    #Create a new album
    
    def create(self, album):
        self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [
            album.title, album.release_year, album.artist_id])
        return None
    
    # Delete album by its id
    def delete(self, album_id):
        self._connection.execute(
            'DELETE FROM albums WHERE id = %s', [album_id])
        return None