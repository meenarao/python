x=int(input("enter your baggage weight"))
if(x>15):
    print("your weight is exceeds the baggage limit of 15kg please remove something")
b=x-15
print(b)

#add up the numbers less than 90 using a for loop
def num():
    total=0
    for i in range(90):
        total+=i
        print(total)
num()
#In class exercise: Create a function that returns the sum of the first n numbers, where n is given as function parameter. 

def num(n):
    total=0
    for i in range(n):
        total+=i
        print(total)
num(10)
#list
mylist=[1,4,8,9,80]
print(sum(mylist))
print(max(mylist))
print(min(mylist))