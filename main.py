from flask import Flask, render_template
import util

# create an application instance
# all requests it receives from clients to this object for handling
# we are instantiating a Flask object by passing __name__ argument to the Flask constructor. 
# The Flask constructor has one required argument which is the name of the application package. 
# Most of the time __name__ is the correct value. The name of the application package is used 
# by Flask to find static assets, templates and so on.
app = Flask(__name__)

# evil global variables
# can be placed in a config file
# here is a possible tutorial how you can do this
username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'

# route is used to map a URL with a Python function
# complete address: ip:port/
# 127.0.0.1:5000/
@app.route('/api/update_basket_a/')
def index():  
    log = "success"
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    
    

    
    insertion = "INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry')"
    cursor.execute(insertion)
    cursor.execute("select * from basket_a")
    print(cursor.fetchall())
    connection.commit()


    
    

    #if record1 != -1:
     #   # you can replace this part with a 404 page
      #  log = "Success!"
    #elif record1 == -1:
     #   print("SQL ERROR")
        

    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    # using render_template function, Flask will search
    # the file named index.html under templates folder
    return render_template('index.html', log_html = log)
    
    
    
    
@app.route('/api/unique/')
def unique():
    cursor, connection = util.connect_to_db('raywu1999',password,host,port,database)
    query = "select fruit_a, fruit_b from basket_a full join basket_b on fruit_a = fruit_b where a is NULL or b is NULL"
    print(cursor.description)
    col_names = ["Fruit"]
    log = util.run_and_fetch_sql(cursor, query)
    util.disconnect_from_db(connection,cursor)
    return render_template('unique.html', sql_table = log, table_title=col_names)
    
    


if __name__ == '__main__':

    # set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)

