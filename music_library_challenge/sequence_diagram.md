```mermaid
sequenceDiagram
    participant t as terminal
    participant app as Main program (in app.py)
    participant ar as AlbumRepository class <br /> (in lib/album_repository.py)
    participant db_conn as DatabaseConnection class in (in lib/database_connection.py)
    participant db as Postgres database

    Note left of t: Flow of time <br />⬇ <br /> ⬇ <br /> ⬇ 

    t->>app: Runs `python app.py`
    app->>db_conn: Opens connection to database by calling connection method on DatabaseConnection object
    db_conn->>db_conn: Opens database connection using PG and stores the connection
    app->>ar: Calls all method on AlbumRepository
    ar->>db_conn: Sends SQL query by calling execute method on DatabaseConnection
    db_conn->>db: Sends query to database via the open database connection
    db->>db_conn: Returns an array of dictionaries, one for each row of the albums table

    db_conn->>ar: Returns a list of dictionaries, one for each row of the albums table
    loop 
        ar->>ar: Loops through list and creates an Album object for every row
    end
    ar->>app: Returns a list of Album objects
    app->>t: Prints list of albums to terminal

```