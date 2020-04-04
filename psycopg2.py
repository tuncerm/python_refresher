import psycopg2

connection = psycopg2.connect('dbname=todoapp_development user=amy')

cursor = connection.cursor()

# Open a cursor to perform database operations
cursor = connection.cursor()

# drop any existing todos table
cursor.execute("DROP TABLE IF EXISTS todos;")

# (re)create the todos table
# (note: triple quotes allow multiline text in python)
cursor.execute("""
  CREATE TABLE todos (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL
  );
""")

cursor.execute('INSERT INTO todos (id, completed) VALUES (1, True);')

cursor.execute('INSERT INTO todos (id, completed) VALUES (%s, %s);', (2, True))

SQL = 'INSERT INTO todos (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
  'id': 3,
  'completed': False
}

cursor.execute(SQL, data)

cursor.execute('SELECT * FROM todos;')

result = cursor.fetchall()  # fetchall, fetchmany(num), fetchone

print(result)

result2 = cursor.fetchone();

print(result2)  # prints nothing, the fetchall above, fetch everything in the query. fetches are cumulative.

# commit, so it does the executions on the db and persists in the db
connection.commit()

cursor.close()
connection.close()
