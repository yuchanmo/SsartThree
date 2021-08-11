CREATE TABLE sites(  
    site_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    auction_site nvarchar(255) ,
    auction_url nvarchar(300),
    create_time DATETIME not null default CURRENT_TIMESTAMP  
);


CREATE TABLE artists(  
    artist_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    artist_name_kor nvarchar(255) ,
    artist_name_eng nvarchar(300),
    artist_comment nvarchar(500),
    create_time DATETIME not null default CURRENT_TIMESTAMP  
);

create table auctions(
    auction_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    site_id INT,
    auction_url_num int,
    auction_place nvarchar(500),
    auction_date date not null,
    create_time DATETIME not null default CURRENT_TIMESTAMP ,
    foreign key(site_id)
    REFERENCES sites(site_id) on update CASCADE
);

create table arts(
    art_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    auction_id INT,
    artist_id INT,
    lot_no INT,
    make_year int,
    title_kor nvarchar(500),
    currency nvarchar(30),
    money float,
    unit_cd nvarchar(30),
    size_length float,
    size_width float,
    mix_cd float,
    mix_size float,
    canvas float,
    medium_eng nvarchar(50),
    medium_kor nvarchar(50),
    description nvarchar(500),
    estimate_high float,
    estimate_low float,
    edition nvarchar(50),
    image_name nvarchar(500),
    create_time DATETIME not null default CURRENT_TIMESTAMP ,
    foreign key(auction_id)
    REFERENCES auctions(auction_id) on update CASCADE,
    foreign key(artist_id)
    REFERENCES artists(artist_id) on update CASCADE
);
