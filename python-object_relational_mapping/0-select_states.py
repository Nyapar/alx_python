import MySQLdb
import sys

def list_states(username, password, database_name):
    # Connect to the MySQL server
    try:
        connection = MySQLdb.connect(user=username, passwd=password, db=database_name, host='localhost', port=3306)
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute the SQL query to retrieve all states and sort by states.id
    query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(query)

    # Fetch all the rows and display the results
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    connection.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database_name)

