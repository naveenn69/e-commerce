#!C:/Users/predator/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html  \r\n\r\n")

import pymysql,cgi,cgitb,os
# cgitb.enable()
conn=pymysql.connect(host="localhost",user="root",password="",database="finalproject")
cur=conn.cursor()
f=cgi.FieldStorage()
q2="""select max(ID) from product"""
cur.execute(q2)
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
prodID="23PR"+z+str(n+1)

pid = f.getvalue("info")
q1="""select * from staff where ID=%s"""%(pid)
cur.execute(q1)
conn.commit()
res=cur.fetchall()
for i in res:
    mail=i[3]
    name=i[1]

print("""<!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- <link rel="stylesheet" href=".css">
        <link rel="stylesheet" href="index.css"> -->
        <link rel="stylesheet" href="sell.css">
        <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
        <title>sell</title>
    </head>
    
    <body bgcolor=#c75e55>
        <nav>
            <!-- <label for="" class="logo"><img src="mnm logo f.jpg" alt="" height="80px" width="100px"></label> -->
            <ul>
                <div class="logo">
                    <img src="./media/img/logo.jfif" alt="" height="80px" width="90px" style=" margin-right: 350px;">
                </div>
                 <li><a href="owner_profile.py?info=%s"><i class="fa fa-user" aria-hidden="true"></i>%s</a></li>
                <li ><a href="ownerin.py?info=%s"><i class="fa fa-home" aria-hidden="true"></i>Home</a></li>
                <li class="active"><a><i class="fa fa-shopping-cart" aria-hidden="true"></i>Sell Products</a></li>
                  <li><a href="owner_vieworders.py?info=%s"><i class="fa fa-shopping-cart" aria-hidden="true"></i>View Orders</a></li>
                <li><a href="owner_viewprevorder.py?info=%s"><i class="fa fa-shopping-cart" aria-hidden="true"></i>Previous Orders</a></li>
                <li><a href="index.py"><i class="fa fa-sign-out" aria-hidden="true"></i>Logout</a></li>
            </ul>
        </nav>
        <div class="body">
             <form action="" method="post" enctype="multipart/form-data">
    
                <h1>Product Detail's</h1>
                <input type="text" name="mail" id="user" value="%s">                        
                <input type="text" name="name" id="user" placeholder="PRODUCT NAME">
                <input type="text" name="price" id="user" placeholder="PRICE">
                <input type="text" name="size" id="user" placeholder="SIZE">
                <input type="text" name="pro_id" id="user" value='%s' style="display:none;">
                <input type="file" name="image" id="file" class="inputfile">
                <label for="file"><strong><i class="fa fa-upload" aria-hidden="true"></i>
                        Click To Upload Product Image</strong></label>
    
                <div class="submit">
                    <input type="submit" name="submit" value="POST PRODUCT">
                </div>
    
    
            </form>
        </div>
    </body>
    </html>"""%(pid,i[1],pid,pid,pid,mail,prodID))
if len(f)!=0:
        mail=f.getvalue("mail")
        pname=f.getvalue("name")
        price=f.getvalue("price")
        size=f.getvalue("size")
        pic=f['image']
        prodID=f.getvalue("pro_id")
        submit = f.getvalue("submit")
        if pic.filename:
            fn=os.path.basename(pic.filename)
            open("imagess/" +fn,"wb").write(pic.file.read())
            if submit != None:
                q = """insert into product(MAIL_ID,PR_NAME,PRICE,SIZE,IMAGE,PR_ID)values('%s','%s','%s','%s','%s','%s')""" % (mail,pname,price,size,fn,prodID)
                cur.execute(q)
                conn.commit()
                print("""
                    <script>
                    alert("Inserted successfully");
                    location.href="ownerin.py?info=%s"
                    </script>
                    """%pid)
conn.close()


print("""
<script type="text/javascript">
window.history.forward();
function noBack(){
window.history.forward();
}
</script>""")