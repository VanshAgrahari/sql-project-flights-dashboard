import mysql.connector
class my_db:
        def __init__(self):
            try:
                self.conn=mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='Vansh@123',
                database='flights'
            )
                self.mycursor=self.conn.cursor()
                print('conn established')
            except:
                print('conn not established')

        def fetch_city(self):
             city=[]
             self.mycursor.execute("""
                 SELECT Source FROM flight_dashboard
                 UNION
                 SELECT Destination FROM flight_dashboard
           """)
             data=self.mycursor.fetchall()
             print(data)
             for i in data:
                  city.append(i[0])
             return city
        def fetch_table(self,source,destination):
             self.mycursor.execute("""
              
                SELECT Airline,Date_of_Journey,Dep_Time,Duration,Total_Stops,Price FROM flight_dashboard
                WHERE Source='{}' AND Destination='{}'
    
             """.format(source,destination))

             data=self.mycursor.fetchall()
             return data
        
        def fetch_airline_freq(self):
             airline=[]
             frequency=[]
             self.mycursor.execute("""
                    SELECT Airline,COUNT(*) 
                    FROM flight_dashboard
                    GROUP BY(Airline)
             """)
             data=self.mycursor.fetchall()
             for i in data:
                  airline.append(i[0])
                  frequency.append(i[1])

             return airline,frequency
       
        def busy_airport(self):
             city=[]
             frequency=[]
             self.mycursor.execute("""
            SELECT Source,COUNT(*) 
            FROM(SELECT Source FROM flight_dashboard
            UNION ALL 
            SELECT Destination FROM flight_dashboard  ) AS temp
            GROUP BY Source
            ORDER BY COUNT(*) DESC

            """)
             
             data=self.mycursor.fetchall()
             for i in data:
                  city.append(i[0])
                  frequency.append(i[1])
             return city,frequency


        def find_distinct_airlines(self):
             airline=[]
             self.mycursor.execute("""
                SELECT DISTINCT(Airline) FROM flight_dashboard
               """)
             data=self.mycursor.fetchall()
             for i in data:
                  airline.append(i[0])
             return airline
        
        def day_by_day(self,airline):
             Date=[]
             Frequency=[]
             self.mycursor.execute("""
                SELECT Date_of_Journey,COUNT(*) FROM flight_dashboard
                WHERE Airline='{}'
                GROUP BY Date_of_Journey;
                """.format(airline))
             data=self.mycursor.fetchall()
             for i in data:
                  Date.append(i[0])
                  Frequency.append(i[1])

             return Date,Frequency
        
        def flights_between_cities(self):
             cities=[]
             frequency=[]
             self.mycursor.execute("""
                SELECT Source,Destination ,COUNT(*) 
                FROM flight_dashboard
                GROUP BY Source,Destination 
                """)
             data=self.mycursor.fetchall()
             for i in data:
                  cities.append((i[0],i[1]))
                  frequency.append(i[2])
             return cities,frequency