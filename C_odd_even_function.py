#this will ask your name and then your fav no. and tell you that it is odd or even
print("what is your name?")
#name is a variable to store the user name/input
name = input()
print("hello"+name)
print("type your fav no")
num = int(input())
def oddeven (num):
    if(num%2==0):
        print("number is even")
    else:
        print("number is odd")
      
oddeven (num)
        