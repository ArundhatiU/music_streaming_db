# music_streaming_db
### Music Streaming Service

Music streaming services have become a cornerstone of digital entertainment, offering users convenient access to millions of songs.
In this project, focus is on building a relational database for a music streaming platform to address critical backend needs. 
The goal was to design a system capable of managing core functionalities such as user subscriptions, playlists, and artist data while keeping the database scalable for future enhancements. 
This approach ensures that the platform has a robust foundation, capable of adapting to advanced features like personalized recommendations or real-time search tools as the platform grows.

This database design includes comprehensive metadata for songs and artists. This metadata—such as genres, release dates, and lyrics—enables the platform to support future developments like real-time search and personalized recommendations. 
One of the key components is the subscription plan table, which categorizes users into free and premium tiers. 
This table ensures scalability, supporting features specific to each tier. 
Additionally, the database supports subscriber-generated playlists through a playlist table. 
Relationships between playlists and songs are managed via the playlist_songs table, which allows users to create and customize playlists seamlessly. 
Together, these features provide an efficient and organized way to handle core user interactions on the platform.

In addition to managing user and playlist data,  database tracks artist payments through a dedicated payments table. 
This table allows for multiple payment entries per artist, ensuring accurate tracking of revenues over time. 
While the database excludes stream counts and detailed user activity tracking—such as listening history or favorites—it focuses on simplicity and functionality. 
By prioritizing essential features like playlist and song organization, we created a system that is scalable and ready for future integration of advanced functionalities. 
These might include search optimization, personalized content recommendations, or real-time data analysis. 
Ultimately, this project lays a strong foundation for both efficient operations and meaningful expansion opportunities in the future.

EER model link:  https://github.com/ArundhatiU/music_streaming_db/blob/main/EER_diagram_music_streaming_service_db.drawio.png

## Relations used in database:

1. Account(account_id, account_type) 
2. Subscriber(subscriber_id, subscriber_name, subscriber_email,plan_id)
3. Artist(artist_id, artist_name, artist_email, bank_acc_no)
4. Subscription_Plan(plan_id, plan_name)
5. Playlist(playlist_id, subscriber_id, playlist_name)
6. Album(album_id, album_name, artist_id)
7. Songs(song_id, song_name, song_lyrics, genre_id, release_date, artist_id,album_id)
8. Playlist_Songs(playlist_id, song_id)
9. Payments(payment_id, artist_id, amount, date)
10. Genre(genre_id, genre_name, genre_description )
