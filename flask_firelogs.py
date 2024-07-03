from flask import Flask 
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
db_conn = mysql.connector.connect(host='localhost', user='root', password='cutie123', database='fire_db')
cursor = db_conn.cursor()

@app.route('/')
def index():
    # Fetch fire logs from the database
    cursor.execute("SELECT * FROM fire_logs")
    fire_logs = cursor.fetchall()
    
    # Prepare HTML to display fire logs
    html = "<h1>Fire Logs</h1>"
    html += "<ul>"
    for log in fire_logs:
        html += f"<li>{log[1]}</li>"  # Assuming 'fire_detected' is the second column
    html += "</ul>"
    
    return html

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

# Close cursor and database connection
cursor.close()
db_conn.close()
