dict={}
size=int(input("enter the size:"))


for i in range(size):
    key=input("enter your key:")
    value=input("enter your value:")
    dict[key]=value
print(dict)
print(type(dict))

list=[]
size=int(input("enter the list size:"))

for i in range(size):
    list.append(size)
print(list)
print(type(list))
y=[1,2,3,4]
x=y.copy()
#print(x)
print(y is x)