#!C:/Users/predator/AppData/Local/Programs/Python/Python311/python.exe
import os

print("content-type:text/html  \r\n\r\n")
import pymysql,cgi,cgitb
import smtplib
cgitb.enable()
con=pymysql.connect(host='localhost',user='root',password="",database='finalproject')
cur=con.cursor()

q1="""select max(ID) from user"""
cur.execute(q1)
r=cur.fetchone()
if r[0]!=None:
    n=r[0]
else:
    n=0
z=""
if n<=9:
    z="000"
elif n>=10 and n<=99:
    z="00"
elif n>=100 and n<=999:
    z="0"
UserID="23USER"+z+str(n+1)
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="signup.css">
    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
    <title>user_signup</title>
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
            <form action="" method="post" enctype="multipart/form-data">
                <h1>User's Login</h1>

                <input type="text" name="name" id="user" placeholder="NAME">
                <input type="text" name="mail" id="user" placeholder="MAIL ID">
                <input type="text" name="phn" id="user" placeholder="PHONE NUMBER">
                <input type="password" name="pass" id="user" placeholder="PASSWORD">
                <input type="password" name="rpass" id="user" placeholder="RE-TYPE PASSWORD">
                <input type="text" name="userid" id="user" value='%s' style="display:none;">
                <label for="user" >Upload Your Image</label>
                <input type="file" name="image" id="user">
                <a href="userlogin.py">Already have an account?</a>
                <div class="submit">
                    <input type="submit" name="submit" value="CREATE ACCOUNT">
                </div>
            </form>
    </div>


</body>


</html>
"""%UserID)

f=cgi.FieldStorage()
if len(f)!=0:
    Name=f.getvalue("name")
    Mail=f.getvalue("mail")
    phone=f.getvalue("phn")
    password=f.getvalue("pass")
    repassword=f.getvalue("rpass")
    pic = f['image']
    userid=f.getvalue("userid")
    submit=f.getvalue("submit")
    if pic.filename:
        fn = os.path.basename(pic.filename)
        open("imagess/" + fn, "wb").write(pic.file.read())
        if Name!=None:
            if Mail!=None:
                if phone!=None:
                    if password!=None:
                        if(password==repassword):
                            if submit!=None:
                                    q="""insert into user(NAME,MAIL_ID,PHONE,PASSWORD,USER_ID,IMAGE,STATUS) values('%s','%s','%s','%s','%s','%s','%s')"""%(Name,Mail,phone,password,userid,fn,'Logged')
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
                                    alert("Registered successfull")
                                    location.href="userlogin.py";
                                    </script>
                                    """)
                            else:
                                print("""<script>
                                        alert("Upload Image")</script>""")
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
    
            print("""
            <script type="text/javascript">
            window.history.forward();
            function noBack(){
            window.history.forward();
            }
            </script>""")
