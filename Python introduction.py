#  Single line comment 
'''this is triple single Quotes
we can write multiple lines '''
"""this is Tiple Double Quotes
we can create multiple lines string
"""
#Variables:
# A=10                                   #  A-z
# d="Python"                             #  a-z
# Python1=3.09                           # Alphanumeric 
# abc1nn3n4n4n4n0000="No limt space"     #no limit space
# _Var=True                              #starting underscore
# __bhav__=100                           #double Starting and Ending Underscore
#not allow
'''   a=10                                #starting space(Identation)
a b=10                                 #space
in=10                                  #keyword
9python=10                            #starting Number'''


#case sensitive
'''A = 23 
print(A)     # NameError: name 'a' is not defined. Did you mean: 'A'?



#Multiple variables to the multiple values
a,b,c=10,20,20
print(a,b,c)
#multiple values assign to the single variable
a=1,2,3
print(a)
#Different variable assign to the same value
a=b=c=40
print(a)
print(b)
print(c)

a=1,2.3, "1" ,True, 4+6j
print(a)
print(type(a))

devOps=10
print(devOps)        #Output: 10
py_thon=20           
print(py_thon)       #Output:20
DevOps=10
print(DevOps)        #Output:10


#In-built elemets:
print
   input
   id
   Datatype  .etc
'''

#pre defined function
'''a=10
print(a)             #pre defined "print"

a=10
print(id(a))         #Find "address" of the value

a=10
print(type(a))       #built "type" 


#User defined function

#only int value can store
a=int(input("enter the int value:"))
print(a)                                                   #input User-defined element

#any value can store
b=input("enter the any value:int or float or string or etc:")
print(type(b)) '''                                            #its gave output "str" check onec


#import keyword as bhav
#print(bhav.kwlist)


'''import time
x=19
print(x)
time.sleep(10)   # that means taking 10 seconds its take time to the """next output"""
print()
a=10
print(a)'''

#datatypes
#int (numerical value)
'''a=10000000000000    #int
print(a)
print(type(a))

c=-399               #int
print(c)
print(type(c))

d=00                 #int
print(d)
print(type(d))'''

#float (decimal value)
'''g=1.099
print(g)
print(type(g))

g=-20.99
print("g value:",g)
print(type(g))

#perfect structure[ before 9 digits after point 7 digits] with decimal  
#only before decimal 16 digits ,Incase extended output will be changed
The number before the decimal point (.) is "12345678". 
   The number after the decimal point (.) is "03344478
gb=123456789.0344478
print(gb)                  #Output:123456789.0344478
print(type(gb))

gb=1234567891.0344478
print(gb)                  #Output:1234567891.034448
#last digit cut ,+1 added to the before digit
print(type(gb))

gb=12345678912.0344478
print(gb)                  #Output:12345678912.034449
#last digit cut ,+1 added to the before digit
print(type(gb))

gb=123456789123.0344478
print(gb)                  #Output:123456789123.03445
#last digit cut ,+1 added to the before digit
print(type(gb))

gb=1234567891234.0344478
print(gb)                  #Output:1234567891234.0344
#to the output.0344 is not added +1 because in decimal startingwith 0 that's why +1 not added
print(type(gb))

gb=12345678912345.0344478
print(gb)                  #Output:12345678912345.035
#last digit cut ,+1 added to the before digit
print(type(gb))

gb=123456789123456.0344478
print(gb)                  #Output:123456789123456.03
#to the output.03 is not added +1 because in decimal startingwith 0 that's why +1 not added
print(type(gb))

gb=1234567891234567.0344478
print(gb)                  #Output:1234567891234567.0
#to the output.03 is not added +1 because in decimal startingwith 0 that's why +1 not added
print(type(gb))

gb=12345678912345678.0344478
print(gb)                  #Output:1.2345678912345678e+16
#last digit cut ,+1 added to the before digit
print(type(gb))

#Note: staring with 0, (+1) not add [0+1=0], startswith 1 is worked[1+1=2]


#Exponentional form
g=1.2e9
print(g)                    #Ouput:1200000000.0                
#max min float
import sys

print(sys.float_info)


#String
Str1='python'
print(Str1)

#Str2='python's'             #Error
#print(Str2)

Str3="Pthon's life"
print(Str3)

#Str4=We write multiple line's
 #       ,lot of "passages", subpoints
        
print(Str4)
print(type(Str1),type(Str3),type(Str4))


#String methods
#startswith
GB="PythonLife"
print(GB.startswith("P"))   #True
print(GB.startswith("p"))   #False

#endswith
GB="PythonLife"
print(GB.endswith("L"))     #False
print(GB.endswith("e"))     #True

#upper
GB="PythonLife"
print(GB.upper())            #PYTHONLIFE
#lower
GB="PythonLife"
print(GB.lower())            #pythonlife 
print()

#count(number of elements)
GB="PythonLife"
print(GB.count('n'))         #1
AB="Amma"
print(AB.count('m'))         #2

#Count[ how many same char in the string with the help what we want char]
#1
X1="counting chars in the linestring"
print()
c='c'   #define the charcter you want to count
find_c=X1.count(c)
print(find_c)                            #2 (c,c)
print(type(X1))                          #str
print()
t='t'                                    ##define the charcter you want to count
find_t=X1.count(t)                       #assign new var
print(find_t)                            #3   (t,t,t)
print()
#index
print(GB.index('o'))         #4(index number)
print()
#index
X1="to Find index number with the help of char or string"
X2=X1.index("number")# confirm method do the assign to newvariable  #14
print()
print(X2)                                #0
print(type(X2))                          #int
print(type(X1))                          #str
print()
#2
X3=X1.index("or")
print(X3)



#find
GB="PythonLife"
print(GB.find('i'))          #7(index number)

#replace
notes="this is book"
#print(varname.method('old','new'))
print(notes.replace('is','are'))#thare are book
print(notes.replace(' is','are'))#thisare book
print(notes.replace('  is','are'))#this is book
print(notes.replace(' is',' are'))#this are book

#this is book---->these are books
note="this is book"
print(note.replace('is','ese'))
var1=note.replace(' is',' are')
print(var1)
var2=var1.replace('is','ese')
print(var2)
var3=var2.replace('book','books')
print(var3)
output:
these ese book
this are book
these are book
these are books

note6="python lifE"
var4=note6.replace('p','P').replace('l','L').replace('E','e1',10)#10 is index number
print(var4)
output:Python Life1



#length[length of the string startswith index 1]
note7=" my name python  "   #total lenth 17
len_find=print(len(note7))   #notes7 lenth=17
#lstrip
var6=note7.lstrip()
print(var6)
len_find=print(len(var6))     #16"my name python  " [left]
#rstrip
var6=note7.rstrip()
print(var6)
len_find=print(len(var6))     #15" my name python"  [right]

#strip{total bothsides strip delete}
var5=note7.strip()           #my name python
print(var5)
len_find=print(len(var5))    #left side and rightside delete space
                             #output 14

#isalpha
Gb="passage"
var8=Gb.isalpha()
print(var8)                  #True

#isalnum
Gb="pythonV3.9.12"
var9=Gb.isalnum()
print(var9)                  #False
Gb="pythonV3912"
var9=Gb.isalnum()
print(var9)                  #True

#split   [Converted String to list]

Str=PhonePe is a digital payment platform 
in india
var9=Str.split()
print(var9) 
output:
['PhonePe', 'is', 'a', 'digital', 'payment', 'platform', 'in', 'india']

#join [converted list to string]
var10=" ".join(var9)
print(var10)
output:
PhonePe is a digital payment platform in india

#format
GB= "hii {} friend?{}" 
format_str= GB.format("Python","welcome")
print(format_str)
Output: hii Python friend?welcome
#Title (Word word capital)

str="""PhonePe is a digital payment platform in India 
that allows users to make payments, transfer money"""
var11=str.title()
print(var11)
output:Phonepe Is A Digital Payment Platform In India
That Allows Users To Make Payments, Transfer Money'''




#we can print total string with different methods 
#1
x1='Slicing part'
#print(x1)
print()
print(type(x1))                             
print()
res=x1[0:]                                  #Slicing part
print(res)
#2
X1="slicing part1"
print()
print(X1[::])                               #Slicing part1
print(type(X1))

print()

#3
X1="slicing part2"
print()
print(X1[:])                                #Slicing part
print(type(X1))

#4
X1="slicing part3"
print()
print(X1[0:13])                             #Slicing part
print(type(X1))

#i want slicing p
X1="slicing part3"
print()
print(X1[:9])
print(type(X1))                                   #slicing p

#i want sliciing p
X1="slicing part4"
print()
print(X1[0:9])                                     #slicing p                                                           

#i want icing
X1="slicing part5"
print(X1[2:7])                                     #icing

#forward usng step
X1="slicing part7"
X6=x1[3:9:2]
print(X6)                                            #cn


#back ward i want 6trap gn 
X1="slicing part6"
X2=X1[-1:-9:-1]                                    # 6trap gn
print(X2)

#i want 7agcs
X1="slicing part7"
X2=X1[-1:-14:-3]                                    # 7agcs
print(X2)
print()
#i want 6rpg
X1="slicing part6"
X4=X1[-1:-9:-2]                                     # 6rpg
print(X4)

X1="slicing part6"
X4=X1[-1:-2:-9]      #not posible step  backward   # 6
print(X4)

#forward usng step
X1="slicing part7"
X6=x1[3:9:2]
print(X6)                                            #cn


#to reverse a string without using reverse method
'''x1="python"
res=x1[::-1]
print(res)                         #nohtyp

a=input("enter the any value:")
print(type(a))
a1=input("enter the any value:")
print(type(a1))
a2=input("enter the any value:")
print(type(a2))

a3=input("enter the any value:")
print(type(a3))
 
a4=input("enter the any value:")
print(type(a4))

a5=input("enter the any value:")
print(type(a5))'''


#list
list=[]
print(type(list))                    #list

#Insertion Reserved
list=[11,12,13,55,42]
print(list)                            #[11,12,13,55,42]
print(type(list))
print()

#find element with help of index number without using "index method "
newlist=list[1]
print(newlist)                         # 12 element 
print()


#index
new2=list.index(12)
print(new2)                            #1 index
print()

#append
#append print element
list=[11,12,13,55,42,99,78]
list.append(20)                #[11,12,13,55,42,99,78,20]
print(list)

list.append([12,11111114])
print(list)        #[11, 12, 13, 55, 42, 99, 78, 20, [12, 11111114]]
print()

#extend
#concatenation
list.extend([1,89,1000001])
print(list)
#[11, 12, 13, 55, 42, 99, 78, 20, [12, 11111114], 1, 89, 1000001]

#insert(if you insert element that element place move aside)
list4=[1,2,[4],5]
list4.insert(3 ,144)
print(list4) #output:[1, 2, [4], 144, 5]
print()

#insert 2nd method replace the place and remove before element
list4[2]=3
print(list4)
#output :[1, 2, 3, 144, 5]

list=[11, 12, 13, 55, 42, 99, 78, 20, [12, 11111114], 1, 89, 1000001]
list.insert(3 ,99)
print(list)
#[11, 12, 13, 99, 55, 42, 99, 78, 20, [12, 11111114], 1, 89, 1000001]



#pop
#it will remove the last element from the list
#and if you can give index that element will be deleted
l=[119,125,13,556,42,99,78]
l.pop() #noindexnumber
print(l)                        
#[119, 125, 13, 556, 42, 99]#78 last element deleted
print()
l.pop(3) #indexnumber
print(l)   
#[119, 125, 13, 42, 99] #556 withindex element


#remove
#it will remove the what you want (element)
l=[119,125,13,556,42,99,78,67,3]
l.remove(125)                  
print(l)
#[119, 13, 556, 42, 99, 78, 67, 3]#125 deleted
l.remove(13)
print(l)
#[119, 556, 42, 99, 78, 67, 3]

print()
#sort
l=[119,125,13,556,42,99,78,67,3]
l.sort()
print(l)
#[3, 13, 42, 67, 78, 99, 119, 125, 556]

print()
'''form  1'''
l.sort(reverse=True)
print(l)
#[556, 125, 119, 99, 78, 67, 42, 13, 3]

#reverse
'''form  2'''
print()
l.reverse()
print(l)#to Above output reverse order
#[3, 13, 42, 67, 78, 99, 119, 125, 556]
#reverse order
'''form 3'''
print(l[::-1])


#count
#count how many same items
same_one=[1,3,4,1,2,1,4,1]
count_ele=same_one.count(1)
print(count_ele)   #4   times

print()
#copy
orig_list=['python','bhavani',1]
orig_list.copy()
print(orig_list)
#['python','bhavani',1]copied list
add_list=orig_list.append(['bhavani1'])
print(add_list)                 # output : #None


print()
#copy
orig_list=['python','bhavani',1]
copy_list=orig_list.copy()
print("copied list:",copy_list) 
#copied list: ['python', 'bhavani', 1]

copy_list.append(['bhavani1'])
print("i add to the copied list,not to the orig_list:",copy_list) 
#outputi:i add to the copied list,not to the orig_list: ['python', 'bhavani', 1, ['bhavani1']]

#clear
l1=[23,4,5,6,6,62,"3r"]
l1.clear()
print(l1)                        #[]

#length
l2=[21,5,3,4,4,2,4,43,3,]
print(len(l2))                   #9elements
#slicing
x12=[1,2,3,54,4,45,56,7,2]
print()
print(x12[::])    #[1, 2, 3, 54, 4, 45, 56, 7, 2]
print(x12[:])     #[1, 2, 3, 54, 4, 45, 56, 7, 2]
            #reverse
print(x12[::-1])   #[2, 7, 56, 45, 4, 54, 3, 2, 1]

print()
print(x12)
print()

print(len(x12))    #9
print()
print(x12)
print(x12[0:7])     #[1, 2, 3, 54, 4, 45, 56]
print(x12[0:8])     #[1, 2, 3, 54, 4, 45, 56, 7]
print(x12[0:9])     #[1, 2, 3, 54, 4, 45, 56, 7, 2]
print(x12[0:10])    #[1, 2, 3, 54, 4, 45, 56, 7, 2]


print(x12[4:8])     #[4, 45, 56, 7]
print(x12[2:9])     #[3, 54, 4, 45, 56, 7, 2]

#range[start:stop:step]

print(x12[0:9:2]) 
         #[index 0: stop index 9..(9-1)=8indexlast:step 2]
         #[1, 3, 4, 56, 2]
print(x12[2:6:1])
         #[3, 54, 4, 45]
print(x12[2:8:3])
         #[3, 45]
print(x12[2:9:3])#out of index 9 
         #[3, 45, 2]

#backward direction lo
print(x12)
#[1, 2, 3, 54, 4, 45, 56, 7, 2]
print(x12[:-1])
#[1, 2, 3, 54, 4, 45, 56, 7]
print(x12[-1:-8:-1]) 
#[2, 7, 56, 45, 4, 54, 3]
print(x12[-1:-8:-2])#
#[2, 56, 4, 3]
print(x12[-5:-9:-4])
#[4]
print(x12[-5:-10:-4])
#[4, 1]


py=["bhav","python","python2"]
#  [ -3       -2       -1    ]
print(py[-1:])
#['python2']
print(py[:-1])
#['bhav', 'python'
py[2]="python3" 
print(py)
#['bhav', 'python', 'python3']
py.insert(2, "English")
print(py)
#['bhav', 'python', 'English', 'python3']

#Tuple
x=(10)
print(type(x)) #int

X11=()
print(type(X11))  #tuple

x1=10,20
print(type(x1)) #tuple

X2=( 10, )
print(type(X2))  #tuple

print(X2[0])      #10

x=(10,3,"3AA",4,45,5,5,5,)
print(x[2])#3AA
print(x[0:5])#(10, 3, '3AA', 4, 45)

t1=(1,2,4,3,4,4,44,4,4)
t2=(3,4,56)
t=t1+t2
print(t)
#(1, 2, 4, 3, 4, 4, 44, 4, 4, 3, 4, 56)

print(len(t))         #12
print(max(t))         #56
print(min(t))         #1
print(sorted(t))  
#[1, 2, 3, 3, 4, 4, 4, 4, 4, 4, 44, 56]
print(sum(t))  #133

''''
#eval():
#eval
#normal way input(int,float,str,complex,bool,list)
input_1=(input("enter the int value:"))#89
print(type(input_1))                   #str
input_2=(input("enter the int value:"))#9.00
print(type(input_2))                   #str
input_3=(input("enter the int value:"))#py1
print(type(input_3))                   #str
input_4=(input("enter the int value:"))#True
print(type(input_4))                   #str
input_5=(input("enter the int value:"))#1+8j
print(type(input_5))                   

list=[10,30,39]
x1=input("enter your value:")
list.append(x1)
print(list)
#output:
#enter your value:2
#[10, 30, 39, '2']#2 add as a str
#eval overcome this problem

x=[10,78,88]
x1=input("enter your value:")
x.append(x1)
print(x)   #output:[10,78,99,'88'] 88 is str

x=[10,78,88]
x1=eval(input("enter your value:"))
x.append(x1)
print(x)   
#output:enter your value:88
         [10,78,99,88] 88 not a str

#more than one element taken as tuple or list
x=[10,78,88]
x1=eval(input("enter your value:"))
x.append(x1)
print(x)  ''' 

'''enter your value:[78,90,98,78,88]
[10, 78, 88, [78, 90, 98, 78, 88]]'''

'''enter your value:78,90,98,78,88
[10, 78, 88, (78, 90, 98, 78, 88)]'''


#dict
dict={"name":"python","age":66,"gender":"it",}
print(dict.keys())
print(dict.values())
print(dict.items())


second_type={
            1: "name",
            2: "Emp ID",
            3: {1:"bhav"}
           }
print(type(second_type))
print(second_type)
print(second_type[3][1])
'''output
<class 'dict'>
{1: 'name', 2:'Emp ID', 3: {1: 'bhav'}}
bhav'''

#get():
#note:get is used to give key take value
dict2=dict.get("name")
print(dict2)       #python

dict3=dict.get("age")
print(dict3)      #66

#update
dict4=dict.update({"py_varsion":3.10 ,"year":1991})
print(dict4)       #output:None  


dict.update({"py_varsion":3.10 ,"year":1991})
print(dict)
'''output:
{'name': 'python', 'age': 66, 'gender': 'it', 'py_varsion': 3.1, 'year': 1991}'''
dict.update({"py_varsion":3.101})
print(dict)
'''output:
{'name': 'python', 'age': 66, 'gender': 'it', 'py_varsion': 3.101, 'year': 1991}'''

#pop
dict.pop("age")
print(dict)
'''output:
{'name': 'python', 'gender': 'it', 'py_varsion': 3.101, 'year': 1991}'''


dict["laptop"]=1
print(dict)
'''output:
{'name': 'python', 'gender': 'it', 'py_varsion': 3.101, 'year': 1991, 'laptop': 1}'''


#clear
dict.clear()
print(dict)   #{}

#Set
s1={11,22,3,45,5,9,6,9}
print(type(s1))
print(s1)
#<class 'set'>
#{3, 5, 6, 22, 9, 11, 45}

s1.add("python")
print(s1)
#output{3, 5, 6, 22, 'python', 9, 11, 45}

s1.update({"aa"})
print(s1)
#output{3, 5, 6, 9, 11, 45, 'aa', 'python', 22}

s1.pop()
print(s1)
#output{5, 6, 9, 11, 45, 'aa', 'python', 22}

s1.remove(11)
print(s1)
#output{5, 6, 9, 45, 'aa', 'python', 22}

s1.discard(6)
print(s1)
#output{5, 9, 45, 'aa', 'python', 22}

s1.difference_update({22})
print(s1)
#output:{5, 9, 45, 'aa', 'python', 22}

#set operations
#Union:no duplicate values
set1={1,2,3,4,5,6,7}
set2={1,2,3,4,5,6,7,4,88,7}
set3=set1.union(set2)
print(set3)
#output:{1, 2, 3, 4, 5, 6, 7, 88}

set1={1,2,3,4,5,6,7}
set2={1,2,3,4,5,6,7,4,88,7}
set3=set2.union(set1)
print(set3)
#output:{1, 2, 3, 4, 5, 6, 7, 88}

#intersection
set1={1,2,3,4,5,6,7}
set2={1,2,3,4,5,6,7,4,88,7}
set3=set1.intersection(set2)
print(set3)
#output:{1, 2, 3, 4, 5, 6, 7}

set1={1,2,3,4,5,6,7}
set2={1,2,3,4,5,6,7,4,88,7}
set3=set2.intersection(set1)
print(set3)
#output:{1, 2, 3, 4, 5, 6, 7}

#difference
set1={1,2,3,4,5,6,7}
set2={1,2,3,4,5,6,7,4,88,7}
set3=set1.difference(set2)
print(set3)
#output:set()

set1={1,2,3,4,5,6,7}
set2={1,2,3,4,5,6,7,4,88,7}
set3=set2.difference(set1)
print(set3)
#output:{88}

#disjoint
set1={1,2,3,4,5,6,7}
set2={1,2,3,4,5,6,7,4,88,7}
set3=set1.isdisjoint(set2)
print(set3)     
#output:False

set1={1,2,3,4,5,6,7}
set2={1,2,3,4,5,6,7,4,88,7}
set3=set2.isdisjoint(set1)
print(set3)
#output:False

#issuperset
set1={1,2,3,4,5,6,7}
set2={1,2,3,4,5,6,7,4,88,7}
set3=set1.issuperset(set2)
print(set3)
#False
set1={1,2,3,4,5,6,7}
set2={1,2,3,4,5,6,7,4,88,7}
set3=set2.issuperset(set1)
print(set3)
#True
#issubset
set1={1,2,3,4,5,6,7}
set2={1,2,3,4,5,6,7,4,88,7}
set3=set2.issubset(set1)
print(set3)
#False
set1={1,2,3,4,5,6,7}
set2={1,2,3,4,5,6,7,4,88,7}
set3=set1.issubset(set2)
print(set3)
#True
print()
#forzenset
set={1,2,34,5,5}
new_far=frozenset(set)
print(new_far)
print(type(new_far))  
'''output:frozenset({1, 2, 34, 5})
<class 'frozenset'> '''

#bytes
set1_byte={1,2,3}
new_byte=bytes(set1_byte) 
print(*new_byte)   # 1 2 3

print(new_byte)   #output:b'\x01\x02\x03'

#bytearry
#note:It working same as bytes.
#it is mutable
l=[10,38,28,28]
b=bytes(l)
print(*b)
ba=bytearray(l)
ba [0]=99
ba[2]=50
print(*ba)
'''output
10 38 28 28
99 38 50 28'''
#range
number=range(10)
print(number)
for num in number:
    print(num)

'''output:    
range(0, 10)
0
1
2
3
4
5
6
7
8
9'''

#None
#None means nothing or empty.
list=None
print(list)
print(type(list))
'''output:
None
<class 'NoneType'>'''



a=[1,2,3,4,5,6]
for i in a:
   a.remove(i)
   print(a)

#the output  i'''
# Ask the user for the number of key-value pairs they want in the dictionary
num_pairs = int(input("Enter the number of key-value pairs for the dictionary: "))

# Create an empty dictionary to store the key-value pairs
my_dict = {}

# Iterate through the range of the specified number of key-value pairs
for i in range(num_pairs):
    # Prompt the user to input each key and value pair
    key = input("Enter key {}: ".format(i+1))
    value = input("Enter value for {}: ".format(key))
    
    # Add the key-value pair to the dictionary
my_dict[key] = value

# Print the final dictionary
print("The dictionary you entered is:", my_dict)
