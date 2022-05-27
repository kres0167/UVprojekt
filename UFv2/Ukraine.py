class variables:
    Størrelse = ""
    Køn = ""
    Vare = ""
    Antal = ""
    nytantal = 0

    def data_check_batch():
        try:                                                   
            sqliteConnection = sqlite3.connect('UVDB.db')     
            cursor = sqliteConnection.cursor()                  

            sql_select_query = """select * from Lager where Køn = Kvinde Vare = Trøje, Størrelse = M;"""
            cursor.execute(sql_select_query, (UVDB.Lager))                   
            records = cursor.fetchall()                                            
            for row in records:                                 
                if(UVDB.Lager == str(row[1])):           
                    print("Vi har et match")
                    UVDB.Lager = True                     
                else:                                             
                    print("row0 = ", row[1])
                    print("Vi har ikke et match")
                    UVDB.Lager = False          
            cursor.close()                                      
        except sqlite3.Error as error:                         
            print("Failed to read data from sqlite table", error)
        finally:                                                
            if sqliteConnection:
                sqliteConnection.close()
        def data_update_batch():
            try:                                                                               
                sqliteConnection = sqlite3.connect('UVDB.db')                                 
                cursor = sqliteConnection.cursor()                                              

                sql_update_query = """Update Stockdb set Quantity = ? where Barcode = ?""" 
                data = (UVDB.db, UVDB.Lager)                                   
                print(data)
                cursor.execute(sql_update_query, data)                                          
                sqliteConnection.commit()                                                       
                print("Lager opdateret")
                cursor.close()                                                                 

            except sqlite3.Error as error:                                                      
                print("Failed to update Lager table", error)
            finally:                                                                            
                if sqliteConnection:
                    sqliteConnection.close()


    def indsæt():
        try:                                                  
            sqliteConnection = sqlite3.connect('UVDB.db')     
            cursor = sqliteConnection.cursor()                
        

            sqlite_insert_query = """INSERT INTO Lager                    
                                (Køn, Vare, Størrelse) 
                                VALUES (?,?,?);"""                                                                                                                        #Her indsætter vi i databasen. Og vi definere kolone navnene vi gerne vil sætte ind på og derefter de værdier vi gerne vil sætte ind. Det gør vi ved ? for at vise det variabler som vi definere senere
            #tuple1 = (str(BatchData.Barcode), BatchData.Product, BatchData.EAN13, BatchData.EAN6, BatchData.Date, BatchData.Batch, BatchData.Category, BatchData.Price, BatchData.Quantity,) #Spørgsmålstegnene ovenover betyder at vi har variabler. Her laver vi en tuple med de værdier vi gerne vil bruge
            print("row værdi: ", tuple1)
            cursor.execute(sqlite_insert_query, tuple1)                                                                                                                     #Nu køre vi querien med vores tuple variabler
            sqliteConnection.commit()                                                                                                                                       #Og vi skal commit for at den endelige ændring sker
            print("Record inserted successfully into Batch, Productbatch table ", cursor.rowcount)
            cursor.close()                                                                                                                                                  #Derefter lukker vi cursor metoden. Hvilket for os er forbindelsen til databasen

        except sqlite3.Error as error:                  
            print("Failed to insert data into productbatch table", error)
        finally:                                       
            if sqliteConnection:
                sqliteConnection.close()


