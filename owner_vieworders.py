#!C:/Users/predator/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html  \r\n\r\n")
import pymysql, cgi, cgitb, smtplib

cgitb.enable()
con = pymysql.connect(host='localhost', user='root', password="", database='finalproject')
cur = con.cursor()
f = cgi.FieldStorage()
pid = f.getvalue("info")
q1 = """select * from staff where ID =%s""" % (pid)
cur.execute(q1)
pr = cur.fetchall()
# mail=res[2]
# print(res)
for r in pr:
    print("""<!DOCTYPE html>
    <html lang="en">
    
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="nav.css">
        <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
        <title>owner_vieworder</title>
    </head>
    
    <body bgcolor=#c75e55>
    <nav>
            <!-- <label for="" class="logo"><img src="mnm logo f.jpg" alt="" height="80px" width="100px"></label> -->
            <ul>
                <div class="logo">
                    <img src="./media/img/logo.jfif" alt="" height="80px" width="90px" style=" margin-right: 300px;">
                </div>
                 <li><a href="owner_profile.py?info=%s"><i class="fa fa-user" aria-hidden="true"></i>%s</a></li>
                <li ><a href="ownerin.py?info=%s"><i class="fa fa-home" aria-hidden="true"></i>Home</a></li>
                <li><a href="sell.py?info=%s"><i class="fa fa-user" aria-hidden="true"></i>SELL PRODUCTS</a>
                <li class="active"><a href=""><i class="fa fa-shopping-cart" aria-hidden="true"></i>View Orders</a></li>
                <li><a href="owner_viewprevorder.py?info=%s"><i class="fa fa-user" aria-hidden="true"></i>PREVIOUS ORDERS</a></li>
                <li><a href="index.py"><i class="fa fa-sign-out" aria-hidden="true"></i>LOG OUT</a></li>
                </li>
            </ul>
        </nav>
            <br><br><div class="heading">
                <h5>PRODUCTS DETAILS</h5>
            </div>
        </div>
        <center>
        <table class="styled-table">
         <thead>
            <tr>
                <th>ID</th>
                <th>PR_ID</th>
                <th>PRODUCT_NAME</th>
                <th>BUYER ID</th>
                <th>OWNER ID</th>
                <th>DELIVER</th>
                <th>CANCEL</th>
            </tr>
         </thead>"""%(pid,r[1],pid,pid,pid))


mail=r[3]
q = """select * from user_orders where OWNER_ID='%s' and STATUS='%s'""" %(mail,'New')
cur.execute(q)
res = cur.fetchall()
for i in res:
    print(""" 
       <tbody>
        <tr class="active-row">
            <form method="post" enctype="multipart/form-data">
            <td><input type="text" value="%s" name="id" style="border: none; width:40px;"></td>
            <td><input type="text" value="%s" name="mail" style="border: none; width:100px;text-transform: uppercase;"></td>
            <td><input type="text" value="%s" name="name" style="border: none; width:100px;"></td>
            <td><b>%s</b></td>
            <td><b>%s</b></td>""" % (i[0], i[2], i[1], i[4],i[5]))
    print("""
          <td><input type="submit" value="DELIVER" name="deliver"></td>
          <td><input type="submit" value="CANCEL" name="cancel"></td>
            </form>
        </tr>
        </tbody>
        """)

print("""""")
print("""
<style>
        .styled-table {
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 0.9em;
            font-family: sans-serif;
            min-width: 400px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);

        }
         .styled-table thead tr {
            background-color: #de9090;
            color: #ffffff;
            text-align: left;
        }
        .styled-table th,
        .styled-table td {
            padding: 12px 15px;
        }
        .styled-table tbody tr {
            border-bottom: 1px solid #de9090;
        }

        .styled-table tbody tr:nth-of-type(even) {
            background-color: #f3f3f3;y
        }

        .styled-table tbody tr:last-of-type {
            border-bottom: 2px solid #de9090;
        }
         .styled-table tbody tr input{
         border: none;
          color: aliceblue;
        font-weight: bolder;
         background-color:#c75e55 ;
         }
              </table>  
              </center>
                </body>
                </html>
                """)

deliver = f.getvalue("deliver")
cancel=f.getvalue("cancel")
if deliver != None:
    ID = f.getvalue("id")
    Name = f.getvalue("name")
    Mail = f.getvalue("mail")
    q2 = """update user_orders set STATUS='ordered' where ID='%s'""" % (ID)
    # fromadd = 'mn5028@srmist.edu.in'
    # password = 'gionliugxxlcgckt'
    # toadd = Mail
    # subject = 'Shop Registration'
    # body = 'Dear {}, \n\t\t Admin has deleted your account.'.format(Name)
    # msg = """Subject:{}\n\n{}""".format(subject, body)
    # server = smtplib.SMTP('smtp.gmail.com:587')
    # server.ehlo()
    # server.starttls()
    # server.login(fromadd, password)
    # server.sendmail(fromadd, toadd, msg)
    # server.quit()
    #
    cur.execute(q2)
    con.commit()
    print("""
    <script>
    alert("ordered Confirmed")
    </script>""")
if cancel!=None:
    ID = f.getvalue("id")
    Name = f.getvalue("name")
    Mail = f.getvalue("mail")
    q3 = """update user_orders set STATUS='cancelled' where ID='%s'""" % (ID)
    cur.execute(q3)
    con.commit()
    print("""
        <script>
        alert("ordered Cancelled")
        </script>""")


    print("""
    <script type="text/javascript">
    window.history.forward();
    function noBack(){
    window.history.forward();
    }
    </script>""")
