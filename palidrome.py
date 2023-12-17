a=int(input("enter any no."))
b=a
rev=0
while a!=0:
    rem=a%10
    rev=rev*10+rem
    a//=10
print(rev)
if rev==b:
    print("number is palindrom")
else:
    print("nor")