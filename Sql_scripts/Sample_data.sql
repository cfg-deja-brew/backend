USE DEJA_BREW;

INSERT INTO CAFES (Id, CafeName, Address, PostCode, City, Created, Latitude, Longitude, CafeDescription, OpeningTimes) VALUES 
('1', 'St Martins Coffee Shop', 'Cank St', 'LE1 5DG', 'Leicester', '2022-05-04 10:00:45', '52.634875', '-1.134974', 'In the heart of the city, serving on-site roasted coffees with an extensive brunch menu', '9:30am-4pm daily'),
('2', 'Kigali Coffee', '2 Stoney St', 'NG1 1LG', 'Nottingham', '2022-05-04 10:05:45', '52.95339100', '-1.14374200', "Speciality coffee shop serving the finest coffee with some of the best cakes and pastries from Nottingham's great artisan bakers", '8am-5pm daily'),
('3', 'The Book Cafe', 'Corn Mkt', 'DE1 1QH', 'Derby', '2022-05-04 10:07:45', '52.922083', '-1.477160', 'Warm, quirky outlet offering all-day breakfast & lunch menus, plus baked goods, coffee & tea', '9am-4pm daily'),
('4', 'Bryter Moon Deli', 'Unit 1 Silver Arcade', 'LE1 5FA', 'Leicester', '2022-05-04 10:07:45', '52.634349', '-1.132549', 'small café with an in-store deli, with a wide range of cheeses and antipasti', '9:30am-5pm daily'),
('5', 'Healthy Louisa','Unit 1, 63 Belgrave Gate', 'LE1 3HR', 'Leicester', '2022-05-04 10:07:45', '52.6391', '-1.1321', 'entirely vegan café serving hearty portions of healthy meals', '10am-5pm daily'),
('6', 'Saints of Mokha', '51 Belvoir St','LE1 6SL','Leicester','2022-05-04 10:07:45','52.633', '-1.1315', 'family-run business, with a focus on speciality lattes','9am-6pm daily'),
('7', 'ORSO', '4 Market Pl', 'LE1 5GF', 'Leicester','2022-05-04 10:07:45','52.63481500', '-1.13413300', 'industrial-style coffee shop with a menu inspired by Australia & Bali','10am-3pm daily'), 
('8', 'Chloe Gourmet','10-12 Cank St', 'LE1 5GW', 'Leicester', '2022-05-04 10:07:45', '52.635246' ,'-1.134050', 'a little slice of Paris in Leicester, serving French patisserie','10am-6:30pm daily'),
('9', 'Grays Coffee Shop', '31 Rutland St', 'LE1 1RE', 'Leicester', '2022-05-04 10:07:45', '52.6345', '-1.128092', 'situated within LCB depot, a great spot to work and relax','9am-4:30pm daily'),
('10', 'BEAR - Iron Gate','7 Iron Gate','DE1 3FJ','Derby', '2022-05-04 10:07:45','52.924017','-1.4772872','Relaxed, rustic-industrial spot for coffee, cocktails & craft beers plus breakfast & lunch fare','7:30am-6pm daily'),
('11', 'BEAN Caffé at Friargate Studios', 'Friar Gate Studios, Ford St','DE1 1EE','Derby', '2022-05-04 10:07:45', '52.924585','-1.483364','Easygoing cafe with modern decor, turning out seasonal grub, fair trade coffee and homemade cakes', '8:30am-2:30pm daily'),
('12', 'Acropolis Cafe', '35-37 Market Pl','DE1 3AE','Derby', '2022-05-04 10:07:45', '52.922892','-1.4765789', 'Family-run cafe offering home cooked breakfasts', '7am-4pm daily'),
('13', 'Café Rosa', 'Theatre Walk, 42D','DE1 2AZ','Derby', '2022-05-04 10:07:45', '52.920812','-1.471745', 'Small local cafe offering hot drinks and sandwiches made to order', '10am-5pm daily'),
('14', 'Miss Coffee', 'Derbion, Crown Walk, 43','DE1 2NP','Derby', '2022-05-04 10:07:45', '52.920753','-1.474824', 'Cafe offering unique blend of freshly prepared oriental bubble tea, fruit tea, cheesecake, milkshakes as well as traditional coffee', '9am-6pm daily'),
('15', 'Cartwheel Cafe and Roastery','16 Low Pavement','NG1 7DL','Nottingham', '2022-05-04 10:07:45','52.9514','-1.1482', 'Relaxed, quaint cafe & roastery offering coffee drinks, baked goods & toast with toppings', '9am-4pm daily'),
('16', 'Fox Cafe', '9 Pelham St','NG1 2EH','Nottingham', '2022-05-04 10:07:45','52.953773','-1.146161','Small, warm cafe serving breakfast & lunch plates plus vegan options alongside coffee drinks','8:30am-6pm'),
('17', 'The Specialty Coffee Shop','50 Friar Ln','NG1 6DQ','Nottingham', '2022-05-04 10:07:45','52.9524', '-1.152', 'Laid-back spot for java drinks with savory cafe eats (some vegan) & baked goods for daytime dining','9am-6pm daily');

INSERT INTO USERS (Id, FirstName, LastName, Email, Mobile, MobileConfirmed, AccountCreated) VALUES
('101', 'Emma', 'Harrison', 'emma.harrison@gmail.com', '+447432087350', TRUE, '2022-05-04 10:07:45'),
('102', 'Dom', 'Gorgosz', 'dom.gorgosz@gmail.com', '+447487222663', TRUE, '2022-05-04 10:09:35'),
('103', 'Leslie', 'Suh', 'happyleslielikesdoughballs@gmail.com', '+447717579188', TRUE, '2022-05-04 10:11:45'),
('104', 'Mariyum', 'Khan', 'mariyummy@gmail.com', '+447746211025', TRUE, '2022-05-04 11:09:00');

INSERT INTO REVIEWS (Id, UserId, CafeId, Rating, ReviewText, Created) VALUES
('1234', '101', '1', 3.5, 'Great spot, conveniently located but do not have many vegan options', '2022-05-04 11:09:00'),
('1235', '102', '2', 5.0, 'Love it! I go here every day', '2022-05-05 11:35:00'),
('1236', '103', '3', 4.7, 'Amazing vibes and coffee', '2022-05-11 11:35:00'),
('1237', '104', '3', 4.4, 'They do my favourite latte and are located in a great spot', '2022-05-11 11:55:05');


INSERT INTO CAFE_ATTRIBUTES VALUES
('1', FALSE, TRUE, TRUE, FALSE, TRUE, FALSE, FALSE),
('2', TRUE, FALSE, TRUE, TRUE, TRUE, TRUE, FALSE),
('3', FALSE, FALSE, TRUE, FALSE, TRUE, TRUE, TRUE),
('4', FALSE, TRUE, FALSE, FALSE, TRUE, FALSE, TRUE),
('5', TRUE, FALSE, TRUE, TRUE, FALSE, TRUE, FALSE),
('6', FALSE, TRUE, TRUE, FALSE, TRUE, FALSE, FALSE),
('7', TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, FALSE),
('8', FALSE, TRUE, TRUE, FALSE, TRUE, TRUE, TRUE),
('9', TRUE, FALSE, TRUE, TRUE, FALSE, TRUE, FALSE),
('10', FALSE, TRUE, FALSE, FALSE, TRUE, FALSE, FALSE),
('11', FALSE, FALSE, TRUE, TRUE, TRUE, TRUE, FALSE),
('12', FALSE, TRUE, TRUE, FALSE, TRUE, FALSE, FALSE),
('13', TRUE, FALSE, TRUE, TRUE, TRUE, TRUE, FALSE),
('14', TRUE, TRUE, TRUE, TRUE, TRUE, FALSE, FALSE),
('15', TRUE, FALSE, TRUE, TRUE, TRUE, TRUE, TRUE),
('16', FALSE, TRUE, TRUE, FALSE, TRUE, FALSE, FALSE),
('17', FALSE, FALSE, TRUE, FALSE, TRUE, TRUE, TRUE);
