for i in range (1,10):
    print(i)

#for print this fruits
Fruits=["Banana","cherry","apple"]
for i in Fruits:
    print(i)

#for print only banana sepratly
for i in "banana":
    print(i)

#break concept
Fruits=["Banana","Cherry","Apple"]
for i in Fruits:
    if i == "Cherry":
        break
    print(i)

#continue concept
Fruits=["Banana","Cherry","Apple"]
for i in Fruits:
    if i =="Cherry":
        continue
    print(i)

#range
for i in range(5):
    print(i)

#jump concept
for i in range(2,20,3):
    print(i)

#range
for i in range(1,6):
    print(i)


#formate concept
a=5
for i in range(1,11):
    b=a*i
    print(f"{a}*{i}={b}")
    

 