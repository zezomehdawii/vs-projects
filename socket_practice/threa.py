import threading
def add(num1,num2):
    print(num1+num2)

t=threading.Thread(target=add,args=(5,10)) #pass the function that will utilize 
"""target= define the name of the function, args, the passed arguments"""
t.start() #to start the threading function
