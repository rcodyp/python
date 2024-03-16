def greet(name,age):
    print('welcome '+name+'.you are '+str(age)+' years old.')



name = input('enter your name : ')
age = input('enter your age : ')
greet(name,age)

#return
def calc(num1 , num2):
    return num1+num2

num1 = int(input('enter the first num:'))
num2 = int(input('enter the second num:'))
print(calc(num1,num2))

