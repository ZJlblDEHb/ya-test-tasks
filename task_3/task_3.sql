SELECT Name, COUNT(messages.uid) FROM users LEFT OUTER JOIN messages ON users.uid = messages.uid GROUP BY users.uid;
