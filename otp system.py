import random as rn
'''email=input("enter email: ")
username=email[:email.index("@")]
domain=email[email.index("@")+1:]

output="your email is {}, your username is {} and your domain is {}.".format(email,username,domain)
print(output)'''
num=int(input("enter your mobile number : "))
a="xxxxxxx"
strnum=str(num)
strnum=strnum[7:]
print(strnum)
output="your OTP has been sent on {}{}".format(a,strnum)
print(output)

otp=rn.randint(1000,9999)
print(otp)
validate=int(input("enter OTP : "))
if otp==validate:
    print("login successful")
else :
    print("invalid OTP")
