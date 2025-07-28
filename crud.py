import mysql.connector
try:
    conn=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Vansh@123',
        database='indigo'

        )
    mycursor=conn.cursor()
    print('connection established')
except:
    print('connection not established')

# mycursor.execute('CREATE DATABASE indigo')
# conn.commit

mycursor.execute("""

  CREATE TABLE IF NOT EXISTS airport (
            airport_id INTEGER PRIMARY KEY,
            code VARCHAR(255) NOT NULL,
            city VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL     
                 )

""")
   
conn.commit()

# insert data
# mycursor.execute('''
#         INSERT INTO airport VALUES
#         (1,'DEL','DELHI','IGA'),
#         (2,'KOL','KOLKATA','NSCA'),
#         (3,'BOM','MUMBAI','CSMA')
#                  ''')
# conn.commit()

# read data
# mycursor.execute('SELECT * FROM airport WHERE airport_id>1')
# data=mycursor.fetchall()
# print(data)

# for i in data:
#     print(i[3])

# update 
# mycursor.execute('''
#    UPDATE airport
#    SET city='BOMBAY'
#    WHERE airport_id='3'
# ''')

# conn.commit()

# mycursor.execute('SELECT * FROM airport')
# data=mycursor.fetchall()
# print(data)

# delete
# mycursor.execute('''DELETE FROM airport WHERE airport_id='3' 
#                  ''')
# conn.commit()
# mycursor.execute('SELECT * FROM airport')
# data=mycursor.fetchall()
# print(data)

