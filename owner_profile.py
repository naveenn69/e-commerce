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
    fn = "imagess/" + i[8]
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
                <li class="active"><a href=""><i class="fa fa-user" aria-hidden="true"></i>%s</a></li>
                <li ><a href="ownerin.py?info=%s"><i class="fa fa-home" aria-hidden="true"></i>Home</a></li>

                <li><a href="sell.py?info=%s"><i class="fa fa-shopping-cart" aria-hidden="true"></i>Sell Products</a></li>
                  <li><a href="owner_vieworders.py?info=%s"><i class="fa fa-shopping-cart" aria-hidden="true"></i>View Orders</a></li>
                <li><a href="owner_viewprevorder.py?info=%s"><i class="fa fa-shopping-cart" aria-hidden="true"></i>Previous Orders</a></li>
                 <li><a href="index.py"><i class="fa fa-sign-out" aria-hidden="true"></i>Logout</a></li>
            </ul>
        </nav>
        <div class="input">
        <b style="padding: 10px; font-size: 30px; color: rgb(81, 47, 47);"><center></center></b>
        </div>

    </body>

    </html>""" % (i[1],pid, pid,pid,pid))

    print("""      
        <div class="card">
                <img src="%s" alt=""><br><br>
                """ % (fn))
    print("""
                <h1>%s</h1><br><br>
                         """ % (i[1]))
    print("""

                <p><b>%s</b></p><br>
                """ % (i[2]))
    print("""
                <p><b>%s</b></p><br>
                <p><b>+91%s</b></p><br>
                <p><b>%s</b></p><br>
            </div>""" % (i[3], i[4],i[7]))

    print("""<style>
                .card {
          box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
          max-width: 300px;
          margin: auto;
          text-align: center;
        }
        .card img{
        width: 100%;
         border: #000 solid 2px;
        }
        .title {
          color: grey;
          font-size: 18px;
        }
        .card h1{
        text-transform: uppercase;
        color:#eee;
        }
        .card p{
        text-transform: uppercase;
        color:#eee;
        }
        button {
          border: none;
          outline: 0;
          display: inline-block;
          padding: 8px;
          color: white;
          background-color: #000;
          text-align: center;
          cursor: pointer;
          width: 100%;
          font-size: 18px;
        }

        a {
          text-decoration: none;
          font-size: 22px;
          color: black;
          text-transform: uppercase;
        }

        button:hover, a:hover {
          opacity: 0.7;
        }
            </style>
        </body>


        </html>""")

    print("""
    <script type="text/javascript">
    window.history.forward();
    function noBack(){
    window.history.forward();
    }
    </script>""")

