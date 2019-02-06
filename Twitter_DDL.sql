use o_twitter_dev;

create table Location(
	City_ID int not null auto_increment,
    City varchar(255),
    State varchar(255),
    Country varchar(255),
    Latitude int,
    Longitude int,
    primary key(City_ID)
);
