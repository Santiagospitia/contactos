from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app) 

# settings
app.secret_key = 'mysecretkey' ### BUSCAR MEJOR EXPLICACION

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM CONTACTS')
    data = cur.fetchall()
    return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def addContact():
    if request.method == 'POST':
        fullname = request.form['fullname'] 
        phone = request.form['phone'] 
        email = request.form['email']    
        print(fullname, phone, email)

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname,phone,email))
        mysql.connection.commit()
        flash('Contacto agregado satisfactoriamente')
        return redirect(url_for('index'))

@app.route('/edit')
def editarContacto():
    return 'editar contacto'

@app.route('/delete/<string:id>')
def borrarContacto(id):    
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts where id=%s', (id))
    mysql.connection.commit()
    flash('Contacto removido satisfactoriamente')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)