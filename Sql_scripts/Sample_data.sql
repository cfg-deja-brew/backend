USE DEJA_BREW;

INSERT INTO CAFE_OWNERS (Id, CafeId, FirstName, LastName, Email, Mobile) VALUES
('113', '1', 'Agne', 'Markeviciute', 'amarkev@gmail.com', '+447542402087'),
('114', '2', 'Dominika', 'Gorgosz', 'dom.gorgosz@gmail.com', '+447543402087'),
('115', '3', 'Emma', 'Harrison', 'emma.harrison@gmail.com', '+447544402087');

INSERT INTO CAFES (Id, CafeName, Address, PostCode, City, Created, Latitude, Longitude, OwnerId) VALUES
('1', 'St Martins Coffee Shop', 'Cank St', 'LE1 5DG', 'Leicester', '2022-05-04 10:00:45', '52.634875', '-1.134974', '113'),
('2', 'Kigali Coffee', '2 Stoney St', 'NG1 1LG', 'Nottingham', '2022-05-04 10:05:45', '52.95339100', '-1.14374200', '114'),
('3', 'The Book Cafe', 'Corn Mkt', 'DE1 1QH', 'Derby', '2022-05-04 10:07:45', '52.922083', '-1.477160', '115');

INSERT INTO USERS (Id, FirstName, LastName, Email, Mobile, MobileConfirmed, AccountCreated) VALUES
('101', 'Jane', 'Smith', 'jane.smith@gmail.com', '+447545402087', TRUE, '2022-05-04 10:07:45'),
('102', 'Tom', 'Jackson', 'tom.jackh@gmail.com', '+447545402088', TRUE, '2022-05-04 10:09:35'),
('103', 'Sonny', 'Smith', 'sonnys@gmail.com', '+447545402089', TRUE, '2022-05-04 10:11:45'),
('104', 'Nick', 'Roberts', 'nroberts@gmail.com', '+447545402090', TRUE, '2022-05-04 11:09:00');

INSERT INTO REVIEWS (Id, UserId, CafeId, Rating, ReviewText, Created) VALUES
('1234', '101', '1', 3.5, 'Great spot, conveniently located but do not have many vegan options', '2022-05-04 11:09:00'),
('1235', '102', '2', 5.0, 'Love it! I go here every day', '2022-05-05 11:35:00'),
('1236', '103', '3', 4.7, 'Amazing vibes and coffee', '2022-05-11 11:35:00'),
('1237', '104', '3', 4.4, 'They do my favourite latte and are located in a great spot', '2022-05-11 11:55:05');


INSERT INTO CAFE_ATTRIBUTES VALUES
('1', FALSE, TRUE, TRUE, FALSE, TRUE, FALSE, FALSE),
('2', TRUE, FALSE, TRUE, TRUE, TRUE, TRUE, FALSE),
('3', FALSE, FALSE, TRUE, FALSE, TRUE, TRUE, TRUE);
