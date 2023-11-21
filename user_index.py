#!C:/Users/predator/AppData/Local/Programs/Python/Python311/python.exe
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
        <title>userindex</title>
    </head>

    <body bgcolor=#c75e55>
        <nav>
            <!-- <label for="" class="logo"><img src="mnm logo f.jpg" alt="" height="80px" width="100px"></label> -->
            <ul>
                <div class="logo">
                    <img src="./media/img/logo.jfif" alt="" height="80px" width="90px" style=" margin-right: 520px;">
                </div>
                <li><a href="user_profile.py?info=%s"><i class="fa fa-user" aria-hidden="true"></i>%s</a></li>
                <li class="active"><a href=""><i class="fa fa-home" aria-hidden="true"></i>Home</a></li>

                <li><a href="user_cart.py?info=%s"><i class="fa fa-shopping-cart" aria-hidden="true"></i>Cart</a></li>
                <li><a href="user_vieworder.py?info=%s"><i class="fa fa-shopping-cart" aria-hidden="true"></i>Order</a></li>
                 <li><a href="index.py"><i class="fa fa-sign-out" aria-hidden="true"></i>Logout</a></li>
                
            </ul>
        </nav>
         <div class="input">
        <b style="padding: 10px; font-size: 30px; color: rgb(81, 47, 47);"><center></center></b>
        </div>
    </body>
    </html>""" % (pid,i[1],pid,pid))
q1 = """select * from product"""
cur.execute(q1)
pr = cur.fetchall()
# print(pr)
for x in pr:
    fn = "imagess/" + x[5]
    print("""
    <div class="card">
    <form method="post" enctype="multipart/form-data">
    <img src="%s" alt="" name=""><br>
    <input type="text" name="img" value=%s style="display:none;" >
    <input type="text" name="name" value="%s" style="display:none;">
    <h1>%s</h1><br>
    <input type="text" name="price" value=%s style="display:none;">
    <p class="price"><i class="fa fa-inr" aria-hidden="true"></i>%s</p><br>
    <input type="text" name="pr_id" value=%s style="display:none;">
     <p><input type="submit" name="submit" value="Add to cart"></p>
     </form>
     
     </div>
    """ % (fn,x[5],x[2], x[2],x[4],x[4],x[6]))
submit=form.getvalue("submit")
img = form.getvalue("img")
name = form.getvalue("name")
mailid = form.getvalue("mail")
price = form.getvalue("price")
pr_id = form.getvalue("pr_id")
if submit != None:
        q2="""insert into user_cart(IMAGE,NAME,PR_ID,PRICE,MAIL_ID)values('%s','%s','%s','%s','%s')"""%(img,name,pr_id,price,i[2])

        cur.execute(q2)
        conn.commit()
        print("""<script>
        alert("Item added to cart")
        location.href="user_index.py?info=%s"
        </script>"""%pid)
        conn.close()








































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

    .card input {
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

    .card input:hover {
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

