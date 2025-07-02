create database ticketbookingsystem;
use ticketbookingsystem;

create table venue (
    venue_id int primary key auto_increment,
    venue_name varchar(50),
    address varchar(100)
);
desc venue;

create table booking (
    booking_id int primary key auto_increment,
    customer_id int,
    event_id int,
    num_tickets int,
    total_cost decimal(10,2),
    booking_date date
);
desc booking;

create table event (
    event_id int primary key auto_increment,
    event_name varchar(100),
    event_date date,
    event_time time,
    venue_id int,
    total_seats int,
    available_seats int,
    ticket_price decimal(10,2),
    event_type enum('movie', 'sports', 'concert'),
    booking_id int,
    foreign key (venue_id) references venue(venue_id),
    foreign key (booking_id) references booking(booking_id)
);

create table customer (
    customer_id int primary key auto_increment,
    customer_name varchar(100),
    email varchar(100),
    phone_number varchar(15),
    booking_id int,
    foreign key (booking_id) references booking(booking_id)
);


create table movie (
    movie_id int primary key auto_increment,
    event_id int,
    genre varchar(50),
    actor_name varchar(100),
    actress_name varchar(100),
    foreign key (event_id) references event(event_id)
);

create table sports (
    sports_id int primary key auto_increment,
    event_id int,
    sport_name varchar(50),
    teams_name varchar(100),
    foreign key (event_id) references event(event_id)
);

create table concert (
    concert_id int primary key auto_increment,
    event_id int,
    artist_name varchar(100),
    concert_type enum('Theatrical', 'Classical', 'Rock', 'Recital'),
    foreign key (event_id) references event(event_id)
);
select * from booking;

select * from event;