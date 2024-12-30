### Music Streaming Service

Music streaming services have become a cornerstone of digital entertainment, offering users convenient access to millions of songs. This project explores building a comprehensive database system for a music streaming platform, leveraging both relational (SQL) and non-relational (NoSQL) approaches to address critical backend needs. The objective was to design a scalable, efficient, and versatile system capable of managing core functionalities such as user subscriptions, playlists, artist data, and metadata while being adaptable for future enhancements.

EER model link:  https://github.com/ArundhatiU/music_streaming_db/blob/main/EER_diagram_music_streaming_service_db.drawio.png

## Relational Database (SQL) Implementation
The SQL implementation focuses on creating a structured, relational database to ensure robust organization and enforce relationships between entities. Key highlights of this implementation include:

Comprehensive Metadata for Songs and Artists: The database stores rich metadata, such as genres, release dates, and lyrics, to support advanced features like real-time search and personalized recommendations.
User Subscriptions: A dedicated subscription plan table categorizes users into free and premium tiers, enabling feature differentiation and scalability for evolving subscription models.
Playlist Management: The playlist and playlist_songs tables manage user-generated playlists, allowing seamless creation and customization of playlists while maintaining relational integrity.
Artist Payments: A payments table tracks artist revenues over time, supporting accurate financial management with multiple payment entries for each artist.
This SQL-based design emphasizes simplicity, scalability, and readiness for future integrations, such as advanced search optimization, personalized content recommendations, or real-time data analysis.

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

## Non-Relational Database (NoSQL) Implementation
To complement the SQL design, a NoSQL implementation was developed using MongoDB, providing flexibility and scalability for handling unstructured and semi-structured data. Key features of this implementation include:

Document-Based Data Model: Data for songs, users, playlists, and artist information is stored in a document-oriented structure, enabling rapid development and iteration.
Nested and Dynamic Data: Complex relationships, such as playlists containing multiple songs or user preferences, are managed within nested documents, reducing the need for extensive joins.

The NoSQL approach enhances the system's ability to support features like real-time activity tracking, dynamic recommendations, and high-speed queries for large-scale datasets.
