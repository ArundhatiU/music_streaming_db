
#example of python connecting to MySQL server and databases
#
  
import mysql.connector

from mysql.connector import Error


try:
    connection = mysql.connector.connect(host='127.0.0.1',
                                         database='music_database',
                                         user='root',
                                         password='Admin$18',
                                         auth_plugin = 'Admin$18')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)
#
        
#

#Exist (List the playlist_name containing songs created by artist_id=27 )
        sql_select_Query = """SELECT DISTINCT p.playlist_name 
        FROM Playlist p WHERE EXISTS (
        SELECT 1
        FROM Playlist_Songs ps
        JOIN Songs s ON ps.song_id = s.song_id
        WHERE ps.playlist_id = p.playlist_id
        AND s.artist_id = 27
);"""
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("Query 1: EXIST Query \n")
        print("List the playlist_name containing songs created by artist_id=27 :\n")
        for row in records:
            print('playlist_name =',row[0])
        print("***********************")

#


#SimpleQuery (List the song_id ,song_name that does not belong to any album)
        sql_select_Query = """select song_id , song_name from Songs 
        where album_id IS NULL ;"""
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("Query 2: SIMPLE Query \n")
        print("List the song_id ,song_name that does not belong to any album:\n")
        for row in records:
            print('song_id =',row[0],'song_name=',row[1] )
        print("***********************")

#


# Join Query (List the artist_name of all artists who have payment amount > 391142)
    sql_select_Query = """select a.artist_name , p.artist_id ,p.amount from Artist a
    JOIN Payments p ON a.artist_id = p.artist_id
    where p.amount > 391142;"""
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Query 3: JOIN Query \n")
    print("List the artist_name of all artists who have payment amount > 391142:\n")
    for row in records:
        print('artist_name =',row[0], '\tartist_id=',row[1], '\tamount=',row[2] )
    print("***********************")

# 

# Aggregate query(List the number of albums created by an artist )

    sql_select_Query = """select  artist_id ,count(album_name)  from Album
                    group by artist_id;"""
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Query 4: AGGREGATE Query \n")
    print("List the artist_name of all artists who have payment amount > 391142:\n")
    for row in records:
        print('artist_id =',row[0], '\tcount(album_name)=',row[1] )
    print("***********************")
#

# Nested query(artist name, artistid having maximum song_count) 
    sql_select_Query = """SELECT 
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
    );"""
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Query 5: NESTED Query \n")
    print("List the artist_id ,artist_name of artist having maximum song_count :\n")
    for row in records:
        print('artist_id =',row[0], '\tartist_name=',row[1],'\tsong_count=', row[2] )
    print("***********************")

#
# Co-orrelated query (List the playlist_id , playlist_name which has more than 6 songs )
    sql_select_Query = """SELECT 
    P.playlist_id,
    P.playlist_name
    FROM 
    Playlist P
    WHERE 6 <
    (SELECT COUNT(*) 
     FROM Playlist_Songs PS 
     WHERE PS.playlist_id = P.playlist_id);"""
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Query 6: COORRELATED Query \n")
    print("List the playlist_id , playlist_name which has more than 6 songs:\n")
    for row in records:
        print('playist_id =',row[0], '\tplaylist_name=',row[1])
    print("***********************")


#

# set operation union(Get the songs_id, song_name for genre :Rock and Pop)

    sql_select_Query = """SELECT DISTINCT
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
    G.genre_name = 'Rock';"""
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Query 7: UNION Query \n")
    print("List songs_id, song_name for genre :Rock and Pop:\n")
    for row in records:
        print('songs_id =',row[0], '\tsong_name=',row[1])
    print("***********************")

#

# Subqueries in Select and From ()

    sql_select_Query = """SELECT 
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
    Artist A;"""
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Query 8: SUBQUERIES IN SELECT AND FROM\n")
    print("List the artist_id , name ,song count of the artist and their newest song released: \n")
    for row in records:
        print('artist_id =',row[0], '\tartist_name=',row[1],'\tsong_count=',row[2],
        '\tlatest_song=',row[3])
    print("************************************")



except Error as e:
        print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


#you should see the following output
#'''Connected to MySQL Server version  8.0.17
#Your connected to database:  ('classicmodels',)
#True
#MySQL connection is closed'''