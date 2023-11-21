#!C:/Users/predator/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html  \r\n\r\n")

import pymysql, cgi, cgitb

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="finalproject")
cur = conn.cursor()
form = cgi.FieldStorage()
pid = form.getvalue("info")
q = """select * from staff where ID =%s""" % (pid)
cur.execute(q)
res = cur.fetchall()
# mail=res[2]
# print(res)
for i in res:
    print("""<!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="navv.css">
        <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
        <title>ownerin</title>
    </head>

    <body bgcolor=#c75e55>
        <nav>
            <!-- <label for="" class="logo"><img src="mnm logo f.jpg" alt="" height="80px" width="100px"></label> -->
            <ul>
                <div class="logo">
                    <img src="./media/img/logo.jfif" alt="" height="80px" width="90px" style=" margin-right: 250px;">
                </div>
                <li><a href="owner_profile.py?info=%s"><i class="fa fa-user" aria-hidden="true"></i>%s</a></li>
                <li class="active"><a href=""><i class="fa fa-home" aria-hidden="true"></i>Home</a></li>
              
                <li><a href="sell.py?info=%s"><i class="fa fa-shopping-cart" aria-hidden="true"></i>Sell Products</a></li>
                  <li><a href="owner_vieworders.py?info=%s"><i class="fa fa-shopping-cart" aria-hidden="true"></i>View Orders</a></li>
                <li><a href="owner_viewprevorder.py?info=%s"><i class="fa fa-shopping-cart" aria-hidden="true"></i>Previous Orders</a></li>
                 <li><a href="index.py"><i class="fa fa-sign-out" aria-hidden="true"></i>Logout</a></li>
            </ul>
        </nav>
        <div class="input">
        <b style="padding: 10px; font-size: 30px; color: rgb(81, 47, 47);"><center>YOUR PRODUCTS</center></b>
        </div>

    </body>

    </html>""" % (pid,i[1],pid,pid,pid))
mail = i[3]
q1 = """select * from product where MAIL_ID='%s' """ % mail
cur.execute(q1)
pr = cur.fetchall()
for x in pr:
    fn = "imagess/" + x[5]
    print("""
    <div class"gap">
    <div class="card">
    <img src="%s" alt=""><br>
    <h1>%s</h1><br>
    <p class="price"><i class="fa fa-inr" aria-hidden="true"></i>%s</p><br>
     </div>
     </div>
    """ % (fn, x[2],x[4]))
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

    .card button {
        border: none;
        outline: 0;
        padding: 20px;
        color: white;
        background-color: black;
        text-align: center;
        cursor: pointer;
        width: 100%;
        font-size: 18px;
    }

    .card button:hover {
        opacity: 0.7;
    }
</style>""" )


print("""
<script type="text/javascript">
window.history.forward();
function noBack(){
window.history.forward();
}
</script>""")


