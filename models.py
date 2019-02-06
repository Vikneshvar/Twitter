from mysql.connector import connection
import peewee as pw

db_conn  = pw.MySQLDatabase(host="localhost",user="root",password="vik123",database="o_twitter_dev")
print(db_conn)

# cur = conn.cursor()
# query = "SELECT * from location"
# cur.execute(query)
# for (City_ID,City,State,Country,Latitude,Longitude) in cur:
#     print("City={}, State={}, Country={},Latitude={},Longitude={}".format(City,State,Country,Latitude,Longitude))

class Location(pw.Model):
    City_ID = pw.AutoField(primary_key=True)
    City = pw.CharField()
    State = pw.CharField()
    Country = pw.CharField()
    Latitude = pw.CharField()
    Longitude = pw.CharField()
    CCity = pw.CharField()
    CCity_WOEID = pw.CharField()


    class Meta:
        database = db_conn

if __name__ == "__main__":
    try:
        Location.create_table()
    except pw.OperationalError:
        print("Location table already exists!")
 