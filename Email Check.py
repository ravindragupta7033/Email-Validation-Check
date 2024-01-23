import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w{9}$+[.]\w{2,3}$"

Your_Email=input("Enter your Email address:")
if "gmail" in Your_Email:
    if re.search(email_condition,Your_Email):
        print("Your Email  is Valid 👍🏿👍🏾")
    else:
        print("Sorry This is Invalid Email  ❌‍💻🫥👎2 ")

else:
    print("Sorry This is Invalid Email ❌‍💻🫥👎1 ")
    print("tset")

