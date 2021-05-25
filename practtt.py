#write a pro if a person is eligible for vote or not
'''
name= input("enter the name:" )
Age = int(input("enter the age: "))

if Age>= 18:
    print(f'{name} is eligible for vote')
else:
    print( f"{name} is not eligible for vote" )
    '''


# total average print if student is pass or fail

'''
def Results(name):
    Telugu = int(input("enter the marks: "))
    maths = int(input("enter the marks: "))
    biology = int(input("enter the marks: "))
    social = int(input("enter the marks: "))
    hindi = int(input("enter the marks: "))

    total= print("The total marks for the"+" "+name+"is"+" "+str(Telugu+hindi+biology+social+maths))
    Total1=(Telugu+hindi+biology+social+maths)
    ave=(Total1/5)
    average =print("Averagr marks for the"+"  "+name+" "+str(ave))

    if Total1 >= 180:
        print(f"{name} is pass")
    else:
        print(f"{name} is fail")    


Results(input("Enter the name of the Student:"))
'''
#hotel bill 

'''


print("MENU")
print("1.IDLY")
print("2.WADA")
print("3.PURI")
print("4.UTHAPPA")
print("5.SET DOSA")

Order= {"idly":"25","wada":"25","puri":"25","uthappa":"35","setdosa":"50"}
idly= 25
wada=  25
puri=  25
uthappa = 35
setdosa =  50
item=input("enter the item:")

if f"{item}"=="idly":
    print("the price of " + item + " "+str(idly) )
else:
    print("nthdbj")

for i in item:
    print(i)



'''

'''
i = 1 
while i<5:
   
    
 
    if i == 2:
     i = i+1
     continue
    print(i)



    #break
    #continue 
'''
'''
i = 1
while i < 7:
    print(i)
    i = i +1 
else:
 print("i is not lessthan  7")

'''

'''
n= 5
for i in range(n):
    for j in range(i):
        print('*', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('*', end="")
    print('')   

'''

'''
n = 5
for i in range(n):
    for j in range(i):                      #  n = 5
       print('*', end="")   
    print('')                 # 5 to 0
   


for i in range(n,0,-1):
    for j in range(i):
        print('*',end="")
    print('')
'''



'''


f = open("C:\\Users\\personal\\Documents\\example.txt", "a")
f.write("now this text will be seen in the file this is append method ")
f.close()

f=open("C:\\Users\\personal\\Documents\\example.txt","w")
f.write("this cant be seen in  the file due to the file is in read mode")
f.close()

f = open("C:\\Users\\personal\\Documents\\example.txt","r")
print(f.read())

'''
'''
import os
os.remove("C:\\Users\\personal\\Documents\\example.txt") 
'''



'''print("welcome  to ATM")
print("insert the card")
pin=1234
pin1=int(input("please enter the pin: "))
if pin1==pin:
    print("1.check your balace: ")
    print("2.withdraw money")
    print("3.deposite money")
    print("4.mini statement")
    print("5.change password")
    a=int(input(" choose from the following"))
    if a== 1:
        print("the amount in your account is ****")
    if a == 2:
       amunt=  int(input("enter the amount to withdraw:  "))
       print("collect the case")
        
else:
    print("password incorrect")
    '''
i=3
a = 5
while i >=0:
    b =int(input("enter the number: "))
    if b == a:
        print("password correct")
        break
    elif b != a:
        print("chance 1")
    elif b != a:
        print("chance 2")


        i = i - 1
        if i == 0:
            print("you have exhausted the limit")
            break
