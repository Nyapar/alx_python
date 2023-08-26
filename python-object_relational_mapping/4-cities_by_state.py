import MySQLdb
import sys

def list_cities(username, password, database_name):
    # Connect to the MySQL server
    try:
        connection = MySQLdb.connect(user=username, passwd=password, db=database_name, host='localhost', port=3306)
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute the SQL query to retrieve all cities and sort by cities.id
    query = "SELECT * FROM cities ORDER BY cities.id ASC"
    cursor.execute(query)

    # Fetch all the rows and display the results
    cities = cursor.fetchall()
    for city in cities:
        print(city)

    # Close the cursor and the database connection
    cursor.close()
    connection.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_cities(username, password, database_name)

