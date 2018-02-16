#print hello world
print ("Hello World\n")

#print your name saved into a variable as an inputstring
name=input("Enter you name :")
print (name+"\n") 

#Find Length of a String
a="mohan"
l=0
for c in a:
    l+=1
print ("length=%s"%l)

#Print Input String into Tuple
inputString=input("\nEnter string  for tuple: ")
t = tuple(inputString)
print (t)

#Print List Items
newlist=['mohan','sha']
print ("\n")
print(newlist)

#Print Sum of Numbers Received as Input
total = 0
while True:
    number = input('\n Enter a number to find sum or 0 to finish: ')
    if int(number) == 0:
        break
    total += int(number)
print ('Total =', total)

#Next Day
from datetime import datetime
date="01-02-2018"
temp=datetime.strptime(date,'%d-%m-%Y')
incrementDay=temp.day+1
print ("\nNext day: "+str(incrementDay)+"-"+str(temp.month)+"-"+str(temp.year))

#Print String From A Function
def printstr():
    print("\nThis is function\n")
printstr()

#Print Sum of List Values And Swap First Two Values
number=[1,2,3,4]
i=0
total=0
while len(number):
    total=total + number[i]
    i+=1
    if i == len(number):
        break 
print("Total: "+str(total))
print("Input List : "+str(number))
tmp=number[0]
number[0]=number[1]
number[1]=tmp
print("Swapped List: "+str(number)+"\n")

#Tuples
inp=input("Enter data for tuple comma seperated: ")
out=tuple(inp.split(','))
print(out)

#List
inpl=input("Enter data for list comma seperated: ")
outl=list(inpl.split(','))
print(outl)

#Dictionary
outd={}
while True:
    inpdk=input("Enter keys data for dictonary comma seperated: ")
    if inpdk == '0':
        print(outd)
        exit()
    inpdv=input("Enter keys data for dictonary comma seperated: ")
    outd[inpdk]=inpdv

#File Operations
# write a file
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
fo.write( "Python is a great language.\nYeah its great!!\n")
fo.close()

# read a file
fo = open("foo.txt", "r+")
str = fo.read(10)
print ("Read String is : ", str)
fo.close()


#Print Odd or Even Numbers from List
number=[1,2,3,4]
i=0
while len(number): 
    if number[i] % 2 == 0:
        print(str(number[i])+" Even")
        i+=1
        if i == len(number):
            break
    else:
        print(str(number[i])+" Odd")
        i+=1
        if i == len(number):
            break

  



