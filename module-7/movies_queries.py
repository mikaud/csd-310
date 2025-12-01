""" import statements """
import mysql.connector # to connect
from mysql.connector import errorcode

import dotenv # to use .env file
from dotenv import dotenv_values


#using our .env file
secrets = dotenv_values(".env")

""" database config object """
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True #not in .env file
}

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the movies database 
    cursor = db.cursor()
    
    # output the connection status 
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")
    query1 = "SELECT studio_id, studio_name FROM studio" 

    
    query2 = "SELECT genre_id, genre_name FROM genre"

  
    query3 = "SELECT film_name, film_runtime FROM film where film_id > 1"

    
    query4 = "SELECT film_name, film_director FROM film ORDER BY film_releaseDate DESC"

   
    cursor.execute (query1)
    result1 = cursor.fetchall()
    print("-- DISPLAYING Studio RECORDS -- ")

    for x in result1:
        print(x)
        print("\n")


    cursor.execute (query2)
    result2 = cursor.fetchall()
    print("-- DISPLAYING Genre RECORDS -- ")

    for x in result2:
        print(x) 
        print("\n")

    
    cursor.execute (query3)
    result3 = cursor.fetchall()
    print("-- DISPLAYING Short film RECORDS -- ")

    for x in result3:
        print(x)
        print("\n")

    cursor.execute (query4)
    result4 = cursor.fetchall()

    print("-- DISPLAYING Director RECORDS in Order -- ")
    for x in result4:
        print(x)
        print("\n")

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()