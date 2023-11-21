#!C:/Users/predator/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html  \r\n\r\n")

print("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="navv.css">
    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
    <title>admin_index</title>
</head>

<body background="./media/img/b3.jpg">
    <nav>
        <!-- <label for="" class="logo"><img src="mnm logo f.jpg" alt="" height="80px" width="100px"></label> -->
        <ul>
            <div class="logo">
                <img src="./media/img/logo.jfif" alt="" height="80px" width="90px" style=" margin-right: 530px;">
            </div>
            <li class="active"><a href="admin_index.py"><i class="fa fa-home" aria-hidden="true"></i>Home</a></li>
            <li><a href=""><i class="fa fa-user" aria-hidden="true"></i>SHOP OWNER</a>

                <div class="submenu">
                    <ul>
                        <li><a href="adminview_newshopowner.py"><i class="fa fa-user" aria-hidden="true"></i>NEW ACCOUNT</a></li>
                        <li><a href="adminview_existingshopowner.py"><i class="fa fa-user" aria-hidden="true"></i>EXISTING ACCOUNT</a></li>
                    </ul>
                </div>
                  <li><a href="admin_viewuser.py"><i class="fa fa-user" aria-hidden="true"></i>User</a></li>
            <li><a href="admin_viewproducts.py"><i class="fa fa-shopping-cart" aria-hidden="true"></i>Products</a></li>
            <li><a href="index.py"><i class="fa fa-sign-out" aria-hidden="true"></i>LOG OUT</a></li>
            </li>
        </ul>
    </nav>
        <div class="heading">
            <h1>WELCOME BACK ADMIN</h1>
        </div>
    </div>
</body>

</html>""")

print("""
<script type="text/javascript">
window.history.forward();
function noBack(){
window.history.forward();
}
</script>""")
