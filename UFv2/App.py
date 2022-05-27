import sqlite3
from flask import Flask , render_template, g
import datetime
app = Flask(__name__)                                           #Her bliver der lavet en instance af Flask klassen
date1 = datetime.datetime.now() + datetime.timedelta(days=10)   #Bruger datetime modulet til at få dags dato og ligge 10 dage oven i
date = datetime.datetime.now()      
date2 = datetime.datetime(day=1, month=1, year=2000)
timedelta10 = date1 - date2
timedelta = date - date2
print(timedelta)


@app.route("/main")        # @ er en python decorator som flask bruger tildele url.            
def forside():   #Funktionen rendere forsiden og sender variabler med database med samt numerisk værdi af dags dato
    data = get_dbforside()
    batch = get_db_batch()
    print(data)
    return render_template("Forside.html", sort_data = data, var = timedelta.days, batch = batch)        #rendere forside.html samt definere sort_data variablen til at være det samme som data. Dette gør at sort_data variablen kan bruges i html koden. samme med daysdelta
def get_dbforside(): #Samler information fra databasen
    db = getattr(g, '_database', None)          #klargøre til at lave database intruksen
    if db is None:                              #Kigger på om der er en database forbindelse
        db = g._database = sqlite3.connect('Storedb.db') #laver instruksen færdig til oprettelse af forbindelse 
        cursor = db.cursor()                            #laver en instance af cursor til oprettelse af forbindelse
        cursor.execute("select * from Stockdb")           #opretter forbindelse og Køre queryen
        sort_data = cursor.fetchall()                                   #Trækker resultatet ud af databasen
        db.close()                                                      #Lukker forbindelsen
    return sort_data                                                    #Returnere dataen


@app.route("/db")
def database():#Funktionen rendere database siden og sender variabler med database med samt numerisk værdi af dags dato
    data = get_db_stock()
    batch = get_db_batch()
    print(data)
    return render_template("Database.html", all_data = data, var = timedelta.days, batchdata = batch )
def get_db_stock():#Samler information fra databasen
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('Storedb.db')
        cursor = db.cursor()
        cursor.execute("select * from Stockdb")
        all_data = cursor.fetchall()
        db.close()
    return all_data
def get_db_batch():
    try:                                                   
        sqliteConnection = sqlite3.connect('Infodb.db')
        cursor = sqliteConnection.cursor()       
        cursor.execute("select * from Returnbatchdb")
        batchdata = cursor.fetchall()
        cursor.close()                                                                                                                                                  #Derefter lukker vi cursor metoden. Hvilket for os er forbindelsen til databasen
        print("batchdata = ", batchdata)
    except sqlite3.Error as error:
        print("Failed to select data from Infodb.db Returnbatchdb table", error)
    finally: 
        if sqliteConnection:
            sqliteConnection.close()
    return batchdata 


    


@app.route("/")
def index(): #Funktionen rendere login siden
    return render_template("Login.html")


@app.teardown_appcontext #lukker database forbindelsen
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run() #Starter flask op med login siden.
    