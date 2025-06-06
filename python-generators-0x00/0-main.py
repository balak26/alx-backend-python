#!/usr/bin/python3

seed = __import__("seed")

# Step 1: Connect to MySQL server
connection = seed.connect_db()
if connection:
    seed.create_database(connection)
    connection.close()
    print("Connection to MySQL server successful.")

    # Step 2: Connect to ALX_prodev database
    connection = seed.connect_to_prodev()

    if connection:
        # Step 3: Create the user_data table
        seed.create_table(connection)

        # Step 4: Insert data directly from S3
        seed.insert_data_from_s3(connection)

        # Step 5: Check database and table
        cursor = connection.cursor()
        cursor.execute(
            "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'ALX_prodev';"
        )
        result = cursor.fetchone()
        if result:
            print("Database ALX_prodev is present.")

        cursor.execute("SELECT * FROM user_data LIMIT 5;")
        rows = cursor.fetchall()
        print(rows)

        cursor.close()
        connection.close()
    else:
        print("Failed to connect to ALX_prodev database.")
else:
    print("Failed to connect to MySQL server.")