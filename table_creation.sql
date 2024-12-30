use music_database;


CREATE TABLE Account (
    account_id INT PRIMARY KEY NOT NULL,
    account_type VARCHAR(50)
);
CREATE TABLE Subscription_Plan (
    plan_id INT PRIMARY KEY NOT NULL,
    plan_name VARCHAR(100) NOT NULL
);

CREATE TABLE Subscriber (
    subscriber_id INT PRIMARY KEY NOT NULL,
    subscriber_name VARCHAR(100) NOT NULL,
    subscriber_email VARCHAR(100) NOT NULL UNIQUE,
    plan_id INT NOT NULL,
    FOREIGN KEY (subscriber_id) REFERENCES Account(account_id),
    FOREIGN KEY (plan_id) REFERENCES Subscription_Plan(plan_id)
);

CREATE TABLE Artist (
    artist_id INT PRIMARY KEY NOT NULL,
    artist_name VARCHAR(100) NOT NULL,
    artist_email VARCHAR(100) NOT NULL UNIQUE,
    bank_acc_no VARCHAR(50),
    FOREIGN KEY (artist_id) REFERENCES Account(account_id)
);

CREATE TABLE Playlist (
    playlist_id INT PRIMARY KEY NOT NULL,
    subscriber_id INT NOT NULL,
    playlist_name VARCHAR(100) NOT NULL,
    song_list TEXT,
    FOREIGN KEY (subscriber_id) REFERENCES Subscriber(subscriber_id)
);

CREATE TABLE Album (
    album_id INT PRIMARY KEY NOT NULL,
    album_name VARCHAR(100) NOT NULL,
    artist_id INT NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id)
);

CREATE TABLE Genre (
    genre_id INT PRIMARY KEY NOT NULL,
    genre_name VARCHAR(100) NOT NULL,
    genre_description TEXT NOT NULL
);

CREATE TABLE Songs (
    song_id INT PRIMARY KEY NOT NULL,
    song_name VARCHAR(100) NOT NULL,
    song_lyrics TEXT,
    genre_id INT NOT NULL,
    release_date DATE NOT NULL,
    artist_id INT NOT NULL,
    album_id INT NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id),
    FOREIGN KEY (album_id) REFERENCES Album(album_id),
    FOREIGN KEY (genre_id) REFERENCES Genre(genre_id)
);

CREATE TABLE Playlist_Songs (
    playlist_id INT NOT NULL,
    song_id INT NOT NULL,
    PRIMARY KEY (playlist_id, song_id),
    FOREIGN KEY (playlist_id) REFERENCES Playlist(playlist_id),
    FOREIGN KEY (song_id) REFERENCES Songs(song_id)
);
CREATE TABLE Payments (
    payment_id INT PRIMARY KEY NOT NULL,
    amount INT,
    date DATE,
    artist_id INT NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id)
);



