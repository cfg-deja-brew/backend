from db_connection import get_db_connection


#Returns cafes based on selected city - need to create function in app to connect where clause to city selection in front end
def cafes_by_city(City):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""SELECT c.CafeName, c.Address, c.PostCode, c.City, AVG(r.Rating), 1)
                              FROM CAFES c
                              JOIN REVIEWS r
                              ON c.Id = r.CafeId
                              WHERE c.City = %s 
                              GROUP BY c.id;""", (City,))
            results = cursor.fetchall()
            return results


#Returns cafes based on attributes - unfinished
def cafes_by_attribute(Id):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute

