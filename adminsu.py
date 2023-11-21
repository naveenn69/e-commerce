#!C:/Users/predator/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html  \r\n\r\n")

import smtplib
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="signup.css">
    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
    <title>adminsu</title>
</head>
<body background="./media/img/b3.jpg">
    <nav>
        <!-- <label for="" class="logo"><img src="mnm logo f.jpg" alt="" height="80px" width="100px"></label> -->
        <ul>
            <div class="logo">
                <img src="./media/img/logo.jfif" alt="" height="80px" width="90px" style=" margin-right: 545px;">
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
            <form action="">
                <h1>Admin's Login</h1>

                <input type="text" name="name" id="user" placeholder="NAME">
                <input type="text" name="mail" id="user" placeholder="MAIL ID">
                <input type="text" name="phn" id="user" placeholder="PHONE NUMBER">
                <input type="password" name="pass" id="user" placeholder="PASSWORD">
                <input type="password" name="rpass" id="user" placeholder="RE-TYPE PASSWORD">



                <a href="adminlogin.py">Already have an account?</a>
                <div class="submit">
                    <input type="submit" name="submit" value="CREATE ACCOUNT">
                </div>
            </form>
    </div>


</body>


</html>
""")
import pymysql,cgi,cgitb

cgitb.enable()
con=pymysql.connect(host='localhost',user='root',password="",database='finalproject')
cur=con.cursor()

f=cgi.FieldStorage()
if len(f)!=0:
    Name=f.getvalue("name")
    Mail=f.getvalue("mail")
    phone=f.getvalue("phn")
    password=f.getvalue("pass")
    repassword=f.getvalue("rpass")
    submit=f.getvalue("submit")
    if Name!=None:
        if Mail!=None:
            if phone!=None:
                if password!=None:
                    if(password==repassword):
                        if submit!=None:
                                q="""insert into admin(NAME,MAIL_ID,PHONE,PASSWORD) values('%s','%s','%s','%s')"""%(Name,Mail,phone,password)
                                cur.execute(q)
                                con.commit()
                                fromadd = 'mn5028@srmist.edu.in'
                                password = 'gionliugxxlcgckt'
                                toadd = Mail
                                subject = Name

                                msg = """subject:Dear {0}\n\n I hope this message finds you well. We wanted to take a moment to express our sincere appreciation for signing up on our page at www.MNMe-commerce.com. Your decision to join our community means a great deal to us, and we are thrilled to welcome you aboard.\n\n If you ever have any questions, suggestions, or feedback, please don't hesitate to reach out to our support team at mn5028@srmist.edu.in. We are always here to assist you and make your experience with us as enjoyable as possible.""".format(subject)
                                server = smtplib.SMTP('smtp.gmail.com:587')
                                server.ehlo()
                                server.starttls()
                                server.login(fromadd, password)
                                server.sendmail(fromadd, toadd, msg)
                                print("""
                                           <script>
                                           alert("login success");
                                           
                                           </script>
                                           """ )

                                server.quit()
                                print("""
                                <script>
                                alert("Login successfull")</script>
                                """)
                    else:
                        print("""<script>
                        alert("Password doesn't match")</script>""")
                else:
                    print("""  <script>
                    alert("fill in the password")
                    </script>""")
            else:
                print("""  <script>
                alert("fill in the phoneNum")
                </script>""")
        else:
            print("""  <script>
            alert("fill MailID")
            </script>""")
    else:
        print("""  <script>
        alert("fill Name")
        </script>""")

