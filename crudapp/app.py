from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql
app=Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    con=sql.connect("UVDB.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM Reservation")
    data=cur.fetchall()
    return render_template("index.html",datas=data)

@app.route("/add",methods=['POST','GET'])
def add():
    if request.method=='POST':
        Gender=request.form['Gender']
        Item=request.form['Item']
        Size=request.form['Size']
        Date=request.form['Date']
        con=sql.connect("UVDB.db")
        cur=con.cursor()
        cur.execute("INSERT INTO Reservation(Gender,Item,Size,Date) values (?,?,?,?)",(Gender,Item,Size,Date))
        con.commit()
        flash('Added','Success')
        return redirect(url_for("index"))
    return render_template("add.html")
    
@app.route("/delete/<string:id>",methods=['GET'])
def delete(id):
    con=sql.connect("UVDB.db")
    cur=con.cursor()
    cur.execute("DELETE FROM Reservation WHERE ID=?",(id))
    con.commit()
    flash('Deleted','warning')
    return redirect(url_for("index"))
    
if __name__=='__main__':
    app.secret_key='admin123'
    app.run(debug=True)