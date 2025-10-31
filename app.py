import sqlite3

# Create a connection to a new database (or connect to an existing one)
conn = sqlite3.connect('movies.db')

# Create a cursor object
cursor = conn.cursor()

# Select all movies


cursor.execute('SELECT * FROM movies')
all_movies = cursor.fetchall()
print("All movies:")
for movie in all_movies:
    print(movie)





cursor.execute('SELECT AVG(rating) FROM movies')
avg_rating = cursor.fetchone()[0]
print(f"\nAverage rating: {avg_rating:.2f}")

# Commit the changes and close the connection
conn.commit()

# Don't forget to close the connection when you're done!
conn.close()