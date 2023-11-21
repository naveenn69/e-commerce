#!C:/Users/predator/AppData/Local/Programs/Python/Python311/python.exe
import smtplib

print("content-type:text/html  \r\n\r\n")

import pymysql, cgi, cgitb

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="finalproject")
cur = conn.cursor()
form = cgi.FieldStorage()
pid = form.getvalue("info")
q = """select * from user where ID =%s""" % (pid)
cur.execute(q)
res = cur.fetchall()
for i in res:
    print("""<!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="navv.css">
        <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
        <title>user_cart</title>
    </head>

    <body bgcolor=#c75e55>
        <nav>
            
            <ul>
                <div class="logo">
                    <img src="./media/img/logo.jfif" alt="" height="80px" width="90px" style=" margin-right: 540px;">
                </div>
                <li><a href="user_profile.py?info=%s""><i class="fa fa-user" aria-hidden="true"></i>%s</a></li>
                <li><a href="user_index.py?info=%s"><i class="fa fa-home" aria-hidden="true"></i>Home</a></li>
                <li  class="active"><a href=""><i class="fa fa-shopping-cart" aria-hidden="true"></i>Cart</a></li>
                  <li><a href="user_vieworder.py?info=%s"><i class="fa fa-shopping-cart" aria-hidden="true"></i>Order</a></li>
                 <li><a href="index.py"><i class="fa fa-sign-out" aria-hidden="true"></i>Logout</a></li>
            </ul>
        </nav>
        <div class="input">
        <b style="padding: 10px; font-size: 30px; color: rgb(81, 47, 47);"><center></center></b>
        </div>

    </body>

    </html>""" % (pid,i[1],pid,pid))
mail = i[2]
q1 = """select * from user_cart where MAIL_ID='%s' """ % mail
cur.execute(q1)
pr = cur.fetchall()
# print(pr)
if pr!=None:
    for x in pr:
        fn = "imagess/" + x[1]
        print("""
        
        <div class="card">
        <form method="post" enctype="multipart/form-data">
        <input type="text" name="prname" value="%s" style="display:none;">
        <input type="text" name="prid" value="%s" style="display:none;">
        <input type="text" name="primg" value="%s" style="display:none;">
        <input type="text" name="bmail" value="%s" style="display:none;">
         <input type="text" name="status" value="New" style="display:none;">
        <img src="%s" alt=""><br>
        
        <h1>%s</h1><br>
        <p class="price"><i class="fa fa-inr" aria-hidden="true"></i>%s</p><br>
         <p><input type="submit" name="order" value="Order"  class="submit" ></p>
         <p><input type="submit" name="remove" value="Remove from Cart" class="submit" ></p>
         </form>
         </div>
         
        """ % (x[2],x[3],x[1],x[5],fn, x[2], x[4]))
        q3="""select * from product where PR_ID='%s'"""%x[3]
        cur.execute(q3)
        fr=cur.fetchall()
        for y in fr:
            print("""
        <input type="text" name="omail" value="%s" style="display:none;">
        """%(y[1]))
prname=form.getvalue("prname")
omail=form.getvalue("omail")
prid=form.getvalue("prid")
primg=form.getvalue("primg")
status=form.getvalue("status")
Bmail=form.getvalue("bmail")
order=form.getvalue("order")
remove=form.getvalue("remove")
if order!= None:
    q2="""insert into user_orders(PR_NAME,PR_ID,PR_IMG,BUYER_ID,OWNER_ID,STATUS)values('%s','%s','%s','%s','%s','%s')"""%(prname,prid,primg,Bmail,y[1],status)
    q3="""delete from user_cart where PR_ID='%s' and MAIL_ID='%s'"""%(prid,Bmail)
    cur.execute(q2)
    cur.execute(q3)
    conn.commit()

    fromadd = 'mn5028@srmist.edu.in'
    password = 'gionliugxxlcgckt'
    toadd =y[1]

    msg = """subject:Dear \n\n Our client is eager to make this new addition to their collection. They have requested that we source this product for them.I believe that fulfilling this request could further enhance our client's experience and strengthen our customer loyalty. Therefore, I kindly request your assistance in looking into the availability of this product from our suppliers or exploring alternative options to acquire it."""
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(fromadd, password)
    server.sendmail(fromadd, toadd, msg)

    print("""
            <script>
            alert("Order Requested");
            </script>
            """)
if remove!=None:
    q4="""delete from user_cart where PR_ID='%s' and MAIL_ID='%s'"""%(prid,Bmail)
    cur.execute(q4)
    conn.commit()
    print("""
            <script>
            alert("Item will be removed");
            </script>
            """)







print("""<style>

    .card {
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        max-width: 300px;
        background-color:#eee;
        text-align: center;
        font-family: arial;
        margin-right: 42px;
        margin-bottom: 42px;
        float: left;
        padding:30px;


    }
     .card h1{
        text-transform: uppercase;
        font-size: 20px;
    }
      .card p {
        font-size: 15px;
    }
  .card img {
        width: 200px;
        height:200px
    }
    .price {
        color: grey;
        font-size: 22px;
    }

    .card .submit  {
        border: none;
        outline: 0;
        padding: 20px;
        color: white;
        background-color: black;
        text-align: center;
        cursor: pointer;
        width: 100%;
        font-size: 15px;
        padding-top:20px;
    }

    .card .submit:hover {
        opacity: 0.7;
    }
</style>""")

print("""
<script type="text/javascript">
window.history.forward();
function noBack(){
window.history.forward();
}
</script>""")


