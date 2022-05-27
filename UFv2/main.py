import sqlite3
import datetime

class variables:
    Size = "M"
    Gender = "Female"
    Item = "Shirt"
    Antal = 0 
    nytantal = 0
    ID = 0
    UVDB = False
    Dato = datetime.date.today()

def controlfunktion():
    data_check_batch()
    if variables.Antal > 0 and variables.nytantal == 0:
        variables.Antal = variables.Antal -1
        data_update_batch()
        
    reset()
    
def data_check_batch():
        try:                                                   
            sqliteConnection = sqlite3.connect('UVDB.db')     
            cursor = sqliteConnection.cursor()                  

            sql_select_query = """SELECT * FROM Lager;"""
            cursor.execute(sql_select_query,)                   
            records = cursor.fetchall()                                            
            for row in records:                                 
                if(variables.Gender == str(row[1]) and variables.Item == row[2] and variables.Size == row[3]):           
                    variables.UVDB = True
                    variables.Antal = row[4]
                    variables.ID = row[0]  
                    break                  
                else:                                             
                    print("row0 = ", row[1])
                    print("Vi har ikke et match")
                    variables.UVDB = False          
            cursor.close()                                      
        except sqlite3.Error as error:                         
            print("Failed to read data from sqlite table", error)
        finally:                                                
            if sqliteConnection:
                sqliteConnection.close()
                
                
def data_update_batch():
    try:                                                                                #Vi har nedenstående inde i en try så programmer ikke lukker hvis der sker en fejl
        sqliteConnection = sqlite3.connect('UVDB.db')                                  #Opretter forbindelse til batch.db
        cursor = sqliteConnection.cursor()                                              #cursor er en instance af cursor() klassen hvor man kan tilslutte sqlite metoder og køre dem

        sql_update_query = """Update Lager set Antal = ? where ID = ?""" #Vi opdatere productbatch table på antallet hvis barcode matcher
        data = (variables.Antal, variables.ID)                                   #Spørgsmålstegnene ovenover betyder at vi har variabler. Her laver vi en tuple med de variabler vi gerne vil bruge
        print(data)
        cursor.execute(sql_update_query, data) 
        cursor.execute("INSERT INTO Reservation(Gender,Item,Size,Date) VALUES (?,?,?,?);", (variables.Gender, variables.Item, variables.Size, variables.Dato)) #Nu køre vi querien med vores tuple variabler
        sqliteConnection.commit()                                                       #Og vi skal commit for at den endelige ændring sker
        print("Batch Updated successfully")
        cursor.close()                                                                  #Derefter lukker vi cursor metoden. Hvilket for os er forbindelsen til databasen
        print("Vi har et match")
    except sqlite3.Error as error:                                                      #Hvis der sker en fejl udprinter vi fejlbeskeden
        print("Failed to update batch table", error)
    finally:                                                                            #Til sidst kigger den på om den har en forbindelse til en database. Hvis den har det lukker den forbindelsen
        if sqliteConnection:
            sqliteConnection.close()
def reset():
    variables.Size = ""
    variables.Gender = ""
    variables.Item = ""
    variables.Antal = 0 
    variables.nytantal = 0
    variables.ID = ""
    variables.UVDB = False
controlfunktion()