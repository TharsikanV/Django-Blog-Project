import MySQLdb

# Replace with your actual database credentials
db = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='2000',
    db='blog'
)

cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print(f'Database version: {data}')

db.close()
