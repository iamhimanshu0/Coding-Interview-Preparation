-- Acceptance Rate By Date
-- What is the overall friend acceptance rate by date? Your output should have the rate of acceptances by the date the request was sent. Order by the earliest date to latest.

-- Assume that each friend request starts by a user sending (i.e., user_id_sender) a friend request to another user (i.e., user_id_receiver) that's logged in the table with action = 'sent'. If the request is accepted, the table logs action = 'accepted'. If the request is not accepted, no record of action = 'accepted' is logged.o record of action = 'accepted' is logged.

-- fb_friend_requests (data structure)
-- user_id_sender          varchar
-- user_id_receiver        varchar
-- date                    datetime
-- action                  varchar

-- https://www.stratascratch.com/blog/facebook-data-science-interview-question-and-solution-in-sql-friend-acceptance-rate/

-- acceptance rate = # accepted / # sent
select 
    a.date,
    count(b.user_id_receiver)/count(a.user_id_sender) as accept
from
(
    SELECT 
        user_id_sender,
        user_id_receiver,
        date, 
        action
    FROM
        fb_friend_requests
    WHERE 
        action = "sent") a
    left join (
    SELECT 
        user_id_sender,
        user_id_receiver,
        date, 
        action
    FROM
        fb_friend_requests
    WHERE 
        action = "accepted") b 
    on b.user_id_sender = a.user_id_sender
       and b.user_id_receiver = a.user_id_receiver
GROUP BY a.date
ORDER BY a.date DESC