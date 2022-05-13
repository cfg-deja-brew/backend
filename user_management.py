from utils import get_db_connection

#add new user details into DB
def add_user(FirstName, LastName, Email, Mobile):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO USERS
                            (FirstName, LastName, Email, Mobile)
                            VALUES
                            (%s, %s, %s, %s);""", (FirstName, LastName, Email, Mobile))
            connection.commit()

#check if mobile is available
def mobile_available(Mobile):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT *
                                   FROM USERS u
                                   WHERE u.mobile = %s;""", (Mobile,))
            results = cursor.fetchall()
            if len(results) > 0:
                return False
            else:
                return True

print(mobile_available)