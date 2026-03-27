-- TYPE YOUR SQL QUERY BELOW

-- PART 1: Create a SQL query that maps out the daily average users before and after the feature change

SELECT date(login_timestamp, 'unixepoch') AS Day, COUNT(DISTINCT user_id) AS NumUsers
FROM login_history WHERE login_timestamp < strftime('%s', '2018-06-02') GROUP BY Day;

SELECT AVG(NumUsers) AS dau_beforefeature FROM (
    SELECT date(login_timestamp, 'unixepoch') AS Day, COUNT(DISTINCT user_id) AS NumUsers 
    FROM login_history 
    WHERE login_timestamp < strftime('%s', '2018-06-02') 
    GROUP BY Day
);

SELECT date(login_timestamp, 'unixepoch') AS Day, COUNT(DISTINCT user_id) AS NumUsers
FROM login_history WHERE login_timestamp >= strftime('%s', '2018-06-02') GROUP BY Day;

SELECT AVG(NumUsers) AS dau_afterfeature FROM(
    SELECT date(login_timestamp, 'unixepoch') AS Day, COUNT(DISTINCT user_id) AS NumUsers 
    FROM login_history 
    WHERE login_timestamp >= strftime('%s', '2018-06-02') 
    GROUP BY Day
);
-- PART 2: Create a SQL query that indicates the number of status changes by card

SELECT name, COUNT(card_change_history.id) 
FROM card_change_history 
JOIN card ON card_change_history.cardID = card.id 
WHERE oldStatus is NOT NULL GROUP BY cardID;



