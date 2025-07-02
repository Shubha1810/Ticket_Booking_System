use ticketbookingsystem;

insert into venue (venue_name, address) values
('grand theater', 'mumbai'),
('sky arena', 'delhi'),
('open grounds', 'bangalore'),
('city hall', 'kolkata'),
('silver stage', 'chennai'),
('lakeview plaza', 'pune'),
('central dome', 'ahmedabad'),
('stadium a1', 'hyderabad'),
('music square', 'goa'),
('culture house', 'jaipur');
select * from venue;

insert into booking (customer_id, event_id, num_tickets, total_cost, booking_date) values
(1, 1, 2, 2000.00, '2025-06-01'),
(2, 2, 1, 1500.00, '2025-06-02'),
(3, 3, 4, 4000.00, '2025-06-03'),
(4, 4, 3, 2700.00, '2025-06-04'),
(5, 5, 1, 1200.00, '2025-06-05'),
(6, 6, 5, 5000.00, '2025-06-06'),
(7, 7, 1, 1800.00, '2025-06-07'),
(8, 8, 2, 2200.00, '2025-06-08'),
(9, 9, 3, 2700.00, '2025-06-09'),
(10, 10, 2, 3000.00, '2025-06-10');
select * from booking;

insert into customer (customer_name, email, phone_number) values
('ravi sharma', 'ravi@gmail.com', '9876540000'),
('neha verma', 'neha@gmail.com', '9876541000'),
('aman jain', 'aman@gmail.com', '9876542000'),
('pooja naik', 'pooja@gmail.com', '9876543000'),
('anil khanna', 'anil@gmail.com', '9876544000'),
('divya patil', 'divya@gmail.com', '9876545000'),
('suresh mehta', 'suresh@gmail.com', '9876546000'),
('shruti desai', 'shruti@gmail.com', '9876547000'),
('rahul gupta', 'rahul@gmail.com', '9876548000'),
('meena joshi', 'meena@gmail.com', '9876549000');
select * from customer;

insert into event (event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type) values
('world cup match', '2025-07-01', '18:00:00', 1, 20000, 10000, 2500.00, 'sports'),
('movie night', '2025-06-15', '20:00:00', 2, 500, 200, 500.00, 'movie'),
('rock concert', '2025-08-05', '19:30:00', 3, 3000, 2500, 1500.00, 'concert'),
('theater play', '2025-06-20', '17:00:00', 4, 400, 300, 800.00, 'movie'),
('classical concert', '2025-09-10', '18:30:00', 5, 1500, 1200, 2000.00, 'concert'),
('stand-up comedy', '2025-06-25', '21:00:00', 6, 700, 400, 700.00, 'movie'),
('sufi night', '2025-07-15', '20:30:00', 7, 800, 600, 1200.00, 'concert'),
('cricket cup', '2025-07-10', '16:00:00', 8, 25000, 20000, 1800.00, 'sports'),
('fusion concert', '2025-07-30', '19:00:00', 9, 1000, 850, 1600.00, 'concert'),
('indie film fest', '2025-08-20', '15:00:00', 10, 300, 200, 1000.00, 'movie');
select * from event;


insert into movie (event_id, genre, actor_name, actress_name) values
(1, 'Action', 'Shahrukh Khan', 'Deepika Padukone'),
(2, 'Comedy', 'Ayushmann Khurrana', 'Yami Gautam'),
(3, 'Horror', 'Vicky Kaushal', 'Bhumi Pednekar'),
(4, 'Drama', 'Amitabh Bachchan', 'Jaya Bachchan'),
(5, 'Thriller', 'Rajkummar Rao', 'Radhika Apte'),
(6, 'Romance', 'Ranbir Kapoor', 'Alia Bhatt'),
(7, 'Sci-Fi', 'Hrithik Roshan', 'Priyanka Chopra'),
(8, 'Adventure', 'Akshay Kumar', 'Katrina Kaif');

insert into sports (event_id, sport_name, teams_name) values
(9, 'Cricket', 'India vs Australia'),
(10, 'Football', 'Brazil vs Argentina'),
(11, 'Kabaddi', 'Patna Pirates vs U Mumba'),
(12, 'Tennis', 'Federer vs Nadal'),
(13, 'Badminton', 'PV Sindhu vs Carolina Marin'),
(14, 'Wrestling', 'India vs USA'),
(15, 'Boxing', 'India vs Cuba'),
(16, 'Hockey', 'India vs Germany');

insert into concert (event_id, artist_name, concert_type) values
(1, 'Arijit Singh', 'Classical'),
(2, 'Sonu Nigam', 'Recital'),
(3, 'Neha Kakkar', 'Rock'),
(4, 'Shreya Ghoshal', 'Theatrical'),
(5, 'A R Rahman', 'Classical'),
(6, 'Diljit Dosanjh', 'Rock'),
(7, 'KK', 'Recital'),
(8, 'Badshah', 'Rock');

