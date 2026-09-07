#Question 6
import psycopg2

#data gotten after running main.py
color_counts = {
    'GREEN': 10, 'YELLOW': 5, 'BROWN': 6, 'BLUE': 31, 
    'PINK': 5, 'ORANGE': 9, 'CREAM': 2, 'RED': 9, 
    'WHITE': 16, 'ASH': 1, 'BLACK': 1
}

#connecting to the postgresql database I set up
conn = psycopg2.connect(
    host="localhost", 
    database="bincom_test", 
    user="postgres", 
    password="Gbolahan_08", 
    port="5432"
)

cursor = conn.cursor()

# Creating a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS color_frequencies (
        color VARCHAR(50) PRIMARY KEY,
        frequency INT
    )
""")

# I'm inserting all the data at once
cursor.executemany("""
    INSERT INTO color_frequencies (color, frequency) 
    VALUES (%s, %s)
    ON CONFLICT (color) DO UPDATE SET frequency = EXCLUDED.frequency
""", list(color_counts.items()))


conn.commit()
cursor.close()
conn.close()