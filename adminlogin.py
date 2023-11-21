#!C:/Users/predator/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html  \r\n\r\n")

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link rel="stylesheet" href="logine.css">
    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
    <title>admin login</title>
</head>

<body background="./media/img/b3.jpg">
    <nav>
        <ul>
            <div class="logo">
                <img src="./media/img/logo.jfif" alt="" height="80px" width="90px" style=" margin-right: 350px;">
            </div>
            <li class="active"><a href="index.py"><i class="fa fa-home" aria-hidden="true"></i>Home</a></li>
            <li><a href=""><i class="fa fa-envelope" aria-hidden="true"></i></i>About</a></li>
            <li><a href=""><i class="fa fa-instagram" aria-hidden="true"></i>Instagram</a></li>
            <li><a href=""><i class="fa fa-facebook-square" aria-hidden="true"></i>Facebook</a></li>
            <li><a href="index.py"><i class="fa fa-sign-out" aria-hidden="true"></i>Logout</a></li>
        </ul>
    </nav>
    <div class="body">
        <form action="">
            <h1>Admin's Login</h1>
            <input type="text" name="name" id="user" placeholder="USERNAME">
            <input type="password" name="pass" id="user" placeholder="PASSWORD">
            <div class="submit">
                <input type="submit" name="submit" value="LOGIN">
            </div>


        </form>
    </div>
</body>

</html>""")


import pymysql,cgi,cgitb

cgitb.enable()
con=pymysql.connect(host='localhost',user='root',password="",database='finalproject')
cur=con.cursor()

f=cgi.FieldStorage()
if len(f)!=0:
    Name=f.getvalue("name")
    Password=f.getvalue("pass")
    submit=f.getvalue("submit")

    if Name!=None:
        if Password!=None:
            if submit!=None:
                q="""select id from admin where MAIL_ID='%s' and Password='%s'"""%(Name,Password)
                cur.execute(q)
                res=cur.fetchone()
                if res!=None:
                    print("""
                    <script>
                    alert("Login successfull")
                    location.href="admin_index.py?info=%s";
                    </script>"""%res[0])

                else:
                   print("""
                   <script>
                   alert("INVALID CREDENTIALS")
                   </script>""")
        else:
            print("""
           <script>
            alert("ENTER PASSWORD")
            </script>""")
    else:
            print("""
             <script>
             alert("ENTER MAIL ID")
             </script>""")
    con.close()

