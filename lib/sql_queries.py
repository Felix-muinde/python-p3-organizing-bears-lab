import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('bears.db')  # Replace 'bears.db' with your database file name

# Create a cursor
cursor = conn.cursor()

# Define SQL queries
select_all_female_bears_return_name_and_age = """
    SELECT name, age
    FROM bears
    WHERE sex = 'F';
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT name
    FROM bears
    ORDER BY name;
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT name, age
    FROM bears
    WHERE alive = 1
    ORDER BY age;
"""

select_oldest_bear_and_returns_name_and_age = """
    SELECT name, age
    FROM bears
    ORDER BY age DESC
    LIMIT 1;
"""

select_youngest_bear_and_returns_name_and_age = """
    SELECT name, age
    FROM bears
    ORDER BY age
    LIMIT 1;
"""

# Execute the SQL queries
cursor.execute(select_all_female_bears_return_name_and_age)
female_bears = cursor.fetchall()

cursor.execute(select_all_bears_names_and_orders_in_alphabetical_order)
all_bears_alphabetical = cursor.fetchall()

cursor.execute(select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest)
alive_bears_youngest_to_oldest = cursor.fetchall()

cursor.execute(select_oldest_bear_and_returns_name_and_age)
oldest_bear = cursor.fetchone()

cursor.execute(select_youngest_bear_and_returns_name_and_age)
youngest_bear = cursor.fetchone()

# Close the database connection
conn.close()

# Print the results
print("All Female Bears (Name and Age):")
for bear in female_bears:
    print(bear[0], bear[1])

print("\nAll Bears (Alphabetical Order):")
for bear in all_bears_alphabetical:
    print(bear[0])

print("\nAlive Bears (Name and Age, Youngest to Oldest):")
for bear in alive_bears_youngest_to_oldest:
    print(bear[0], bear[1])

print("\nOldest Bear (Name and Age):")
print(oldest_bear[0], oldest_bear[1])

print("\nYoungest Bear (Name and Age):")
print(youngest_bear[0], youngest_bear[1])
