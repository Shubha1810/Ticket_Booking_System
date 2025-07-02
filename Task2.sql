use ticketbookingsystem;

-- TASK 2 
-- QUERY 2
select * from event;
select event_name from event;
select event_name from event;

-- QUERY 3
select available_seats from event;

-- QUERY 4
select * from event
where event_name like '%cup%';

-- QUERY 5
select * from event
where ticket_price between 1000 and 2500;

-- QUERY 6
select * from event
where event_date between '2025-06-01' and '2025-07-31';

-- QUERY 7
select * from event
where available_seats > 0 and event_type like '%concert%' and event_name like '%concert%';

-- QUERY 8
select * from customer
limit 5 offset 5;

 -- QUERY 9
select * from booking
where num_tickets > 4;

-- QUERY 10
select * from customer
where phone_number like '%000';

-- QUERY 11
select * from event
where total_seats > 15000
order by total_seats desc;

-- QUERY 12
select * from event
where event_name not like 'x%' and
      event_name not like 'y%' and
      event_name not like 'z%';



