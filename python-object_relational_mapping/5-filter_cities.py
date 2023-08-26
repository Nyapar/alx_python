import MySQLdb
import sys

def list_cities_by_state(username, password, database_name, state_name):
    # Connect to the MySQL server
    try:
        connection = MySQLdb.connect(user=username, passwd=password, db=database_name, host='localhost', port=3306)
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Prepare the parameterized SQL query and execute it
    query = "SELECT * FROM cities WHERE state_name = %s ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the rows and display the results
    cities = cursor.fetchall()
    for city in cities:
        print(city)

    # Close the cursor and the database connection
    cursor.close()
    connection.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database_name> <state_name>")
        sys.exit(1)

    username, password, database_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    list_cities_by_state(username, password, database_name, state_name)

