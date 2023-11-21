#!C:/Users/predator/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html  \r\n\r\n")

print("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="nav.css">
    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
    <title>admin_viewproducts</title>
</head>

<body bgcolor=#c75e55>
<nav>
        <!-- <label for="" class="logo"><img src="mnm logo f.jpg" alt="" height="80px" width="100px"></label> -->
        <ul>
            <div class="logo">
                <img src="./media/img/logo.jfif" alt="" height="80px" width="90px" style=" margin-right: 500px;">
            </div>
            <li><a href="admin_index.py"><i class="fa fa-home" aria-hidden="true"></i>Home</a></li>
            <li><a href=""><i class="fa fa-user" aria-hidden="true"></i>SHOP OWNER</a>

                <div class="submenu">
                    <ul>
                        <li><a href="adminview_newshopowner.py"><i class="fa fa-user" aria-hidden="true"></i>NEW ACCOUNT</a></li>
                        <li><a href="adminview_existingshopowner.py"><i class="fa fa-user" aria-hidden="true"></i>EXISTING ACCOUNT</a></li>
                    </ul>
                </div>
            <li><a href="admin_viewuser.py"><i class="fa fa-user" aria-hidden="true"></i>USER</a></li>
             <li  class="active" ><a href="admin_viewproducts.py"><i class="fa fa-shopping-cart" aria-hidden="true"></i>Products</a></li>
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
            <th>MAIL_ID</th>
            <th>PRODUCT_NAME</th>
            <th>PRICE</th>
            <th>PRODUCT_ID</th>
            <th>DELETE</th>
        </tr>
     </thead>""")

import pymysql, cgi, cgitb, smtplib

cgitb.enable()
con = pymysql.connect(host='localhost', user='root', password="", database='finalproject')
cur = con.cursor()

q = "select * from product"
cur.execute(q)
res = cur.fetchall()
for i in res:
    print(""" 
       <tbody>
        <tr class="active-row">
            <form method="post" enctype="multipart/form-data">
            <td><input type="text" value="%s" name="id" style="border: none; width:40px;"></td>
            <td><input type="text" value="%s" name="mail" style="border: none; width:250px;text-transform: uppercase;"></td>
            <td><input type="text" value="%s" name="name" style="border: none; width:100px;"></td>
            <td><b>%s</b></td>
            <td><b>%s</b></td>""" % (i[0], i[1], i[2], i[4],i[6]))
    print("""
          <td><input type="submit" value="DELETE" name="delete"></td>
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

f = cgi.FieldStorage()
delete = f.getvalue("delete")
if delete != None:
    print("""
        <script>
        alert("Account deleted")
        </script>""")
    ID = f.getvalue("id")
    Name = f.getvalue("name")
    Mail = f.getvalue("mail")
    q2 = """delete from product where ID='%s'""" % (ID)
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

    cur.execute(q2)
    con.commit()
    print("""
    <script>
    alert("Account deleted")
    </script>""")


    print("""
    <script type="text/javascript">
    window.history.forward();
    function noBack(){
    window.history.forward();
    }
    </script>""")
