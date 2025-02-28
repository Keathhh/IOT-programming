import serial
import mysql.connector

device = '/dev/cu.usbmodem101'
# Update the port path with the correct one for your Arduino
ser = serial.Serial(device, 9600, timeout=1)  # Set timeout to 1 second

# Connect to MySQL database
db_conn = mysql.connector.connect(host='localhost', user='root', password='cutie123', database='fire_db')

# Create cursor object
cursor = db_conn.cursor()

try:
    while True:
        # Read data from Arduino until timeout
        data = ser.readline().decode().strip()  # Read one line of data
        if data:
            print(data)

            # Insert data into the database
            insert_query = "INSERT INTO fire_logs (fire_detected) VALUES (%s)"
            cursor.execute(insert_query, (data,))
            db_conn.commit()

except KeyboardInterrupt:
    print("Stopping data acquisition.")

finally:
    # Close cursor and database connection
    cursor.close()
    db_conn.close()
    ser.close()
