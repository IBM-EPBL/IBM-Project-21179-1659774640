from flask import Flask, render_template, request
import ibm_db

app = Flask(__name__)

conn = ibm_db.connect(
    "DATABASE=bludb;HOSTNAME=1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=32286;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=dtk93338;PWD=honkzW80jUXH3UJN;",
    "", "")
num=[]
num1=[]

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/login.html')
def login1():
    return render_template('login.html')

@app.route('/register.html')
def register():
    return render_template('register.html')


@app.route('/login',methods=["GET","POST"])
def login():
     i = int(0)
     if request.method=="POST":
        fn= request.form.get('fn')
        pn = request.form.get('password')
        sql = "select * from userdetails"
        stmt = ibm_db.exec_immediate(conn, sql)
        while ibm_db.fetch_row(stmt) != False:
           em=ibm_db.result(stmt,0)
           num1.append(em)
           i=i+1
        for y in range(i):
           ele2=str(fn)
           if ele2==num1[y]:
              return render_template("alertwrong.html")
           else:
               return render_template("wrong.html")




@app.route('/register', methods=["GET", "POST"])
def insert():
    i=int(0)
    if request.method == "POST":
        fn = request.form.get('firstname')
        mn = request.form.get('middlename')
        ln = request.form.get('lastname')
        course = request.form.get('course')
        gender = request.form.get('gender')
        #skill = request.form.get('skillset')
        email = request.form.get('email')
        pw = request.form.get('password')
        sql = "select * from userdetails"
        stmt = ibm_db.exec_immediate(conn, sql)
        while ibm_db.fetch_row(stmt) != False:
           em=ibm_db.result(stmt,0)
           num.append(em)
           i=i+1
        for y in range(i):
           ele2=str(fn)
           if ele2==num[y]:
              print("already registered mail")
              return render_template("alertwrong.html")


        insert_sql = "Insert INTO userdetails Values(?,?,?,?,?,?,?)"
        prep_stmt = ibm_db.prepare(conn, insert_sql)
        ibm_db.bind_param(prep_stmt, 1, fn)
        ibm_db.bind_param(prep_stmt, 2, mn)
        ibm_db.bind_param(prep_stmt, 3, ln)
        ibm_db.bind_param(prep_stmt, 4, course)
        ibm_db.bind_param(prep_stmt, 5,  gender)
        ibm_db.bind_param(prep_stmt, 6, email)
        ibm_db.bind_param(prep_stmt, 7, pw)
        ibm_db.execute(prep_stmt)
        print("inserted")
        return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
