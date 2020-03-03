import psycopg2

def connectToDb():


    connection = psycopg2.connect(user="postgres",
                                        password="postgres",
                                        host="localhost",
                                        database="postgres")
    cursor = connection.cursor()

    return cursor