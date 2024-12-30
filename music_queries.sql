use music_database;

## Query 1: Simple query 
## Retrieve the song_id, song_name that does not belong to any album:

SELECT song_id , song_name 
FROM Songs 
WHERE album_id IS NULL;

## Query 2:Aggregate
## Retrieve the number of albums created by an artist

select  artist_id ,count(album_name)  from Album
group by artist_id;

## Qyery 3: Join
## Retrieve the artist_name of all artists who have payment amount > 391142
# joins two tables payments and artists 

select a.artist_name , p.artist_id ,p.amount from Artist a
    JOIN Payments p ON a.artist_id = p.artist_id
    where p.amount > 391142;
    
## Query 4: Nested query 
## Retrieve artist name, artist_id having maximum song_count 

SELECT 
    a.artist_id, 
    a.artist_name, 
    COUNT(s.song_id) AS song_count
FROM 
    Artist A
JOIN 
    Songs S
ON 
    a.artist_id = s.artist_id
GROUP BY 
    a.artist_id, a.artist_name
HAVING 
    COUNT(s.song_id) = (
        SELECT 
            MAX(song_count)
        FROM (
            SELECT 
                s.artist_id, 
                COUNT(s.song_id) AS song_count
            FROM 
                Songs S
            GROUP BY 
                s.artist_id
        ) AS ArtistCounts
    );   

## Query 5:Correlated query 
## Retrieve the playlist_id , playlist_name which has more than 6 songs 
## playlist_id from outer query is referenced in the nested query 

SELECT 
    P.playlist_id,
    P.playlist_name
    FROM 
    Playlist P
    WHERE 6 <
    (SELECT COUNT(*) 
     FROM Playlist_Songs PS 
     WHERE PS.playlist_id = P.playlist_id);
     
## Query 6: Exists 
## Retrieve the playlist_name containing songs created by artist_id=27 
## EXISTS returns true if there is atleast one tuple in the result of  nested query 
     
     SELECT DISTINCT p.playlist_name 
        FROM Playlist p WHERE EXISTS (
        SELECT 1
        FROM Playlist_Songs ps
        JOIN Songs s ON ps.song_id = s.song_id
        WHERE ps.playlist_id = p.playlist_id
        AND s.artist_id = 27
);

## Query 7:Set operations (Union) 
## Retrieve the songs_id, song_name for genre :Rock and Pop
## same number of columns are used  while performning union operation

SELECT DISTINCT
    S.song_id AS SongID, 
    S.song_name AS Name, 
    G.genre_name AS Genre
    FROM Songs S
    JOIN 
    Genre G 
    ON 
    S.genre_id = G.genre_id
    WHERE 
    G.genre_name = 'Pop'

    UNION

    SELECT DISTINCT
    S.song_id AS SongID, 
    S.song_name AS Name, 
    G.genre_name AS Genre
    FROM 
    Songs S
    JOIN 
    Genre G 
    ON 
    S.genre_id = G.genre_id
    WHERE 
    G.genre_name = 'Rock';
    
## Query 8: Subqueries in Select and From 
## Retrieve data from two tables (Artist and Songs) to show each artist’s total number of songs and their most recently released song.
## here we have a subquery in select component.

SELECT 
    A.artist_id,
    A.artist_name,
    (SELECT COUNT(*) 
     FROM Songs S 
     WHERE S.artist_id = A.artist_id) AS song_count,
    (SELECT S.song_name 
     FROM Songs S 
     WHERE S.artist_id = A.artist_id
     ORDER BY S.release_date DESC
     LIMIT 1) AS latest_song
    FROM 
    Artist A;    
