import pymysql as p
def make_connection():
   con=p.connect(host="localhost",user="root",password="",database="blog")
   return con


def insert_author(myt):
    con=make_connection()
    cur=con.cursor()
    query="insert into Author_table (A_UNAME,A_PASSWORD,A_CITY) values (%s,%s,%s)"
    cur.execute(query,myt)
    con.commit()
    con.close()

def insert_user(myt):
    con=make_connection()
    cur=con.cursor()
    query="insert into User_table (U_UNAME,U_PASSWORD,U_CITY) values (%s,%s,%s)"
    cur.execute(query,myt)
    con.commit()
    con.close()

def checkauthor(t):
    con=make_connection()
    cur=con.cursor()
    q="select * from Author_table where a_uname=%s and a_password=%s"
    cur.execute(q,t)
    data=cur.fetchall()
    return data

def checkuser(t):
    con=make_connection()
    cur=con.cursor()
    q="select * from User_table where u_uname=%s and u_password=%s"
    cur.execute(q,t)
    data=cur.fetchall()
    return data


def savepostfun(t):
    con=make_connection()
    cur=con.cursor()
    q="insert into Author_Post (P_UNAME,P_Title,P_post) values(%s,%s,%s)"
    cur.execute(q,t)
    con.commit()
    con.close()

def view_spec_post(t):
    con=make_connection()
    cur=con.cursor()
    q="select * from Author_Post where P_Uname=%s"
    cur.execute(q,t)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def fetch_all_post():
    con=make_connection()
    cur=con.cursor()
    q="select * from Author_Post"
    cur.execute(q)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data
    