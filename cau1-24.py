# #cau 1
# j=[]
# for i in range(2000,3201) :
#     if (i%7==0) and (i%5!=0) :
#         j.append(str(i))
# print(','.join(j))

#cau 2
# x= int(input("Nhập x :"))
# def fact(x) :
#     if x==0 :
#         return 1
#     else :
#         return(x*fact(x-1))
# print(fact(x))

# Câu 3
# n=int(input("Nhập n :"))
# d= dict()
# for i in range(1,n+1) :
#     d[i]= i*i
# print(d)

#cau 4
# values=input("Nhập giá trị : ")
# l=values.split(',')
# t=tuple(l)
# print(l)
# # print(t)

# Câu 5
# class input_outtring(Object) :
#     def __init__(self) :
#         self.s= ""
#     def getstring(self) :
#         self.s=input("Nhập chuỗi : ")
#     def print_string(self) :
#         print(self.s.upper())
# strObj= input_outtring()
# strObj.getstring()
# strObj.print_string()

#Câu 6 :
# x=int(input("Nhập số : "))
# def square(num) :
#     return num **2 
# print(square(2))
# print(square(3))
# print(square(x))
  
# câu 7
# print (abs.__doc__)
# print (int.__doc__)
# print (input.__doc__)
# def square(num) :
#     ''' Trả giá trị bình phương của số nhập vào.
#     số nhập vào phải là số nguyên.
#     '''
#     return num**2
# print(square.__doc__)

# câu 8
# class Person :
#     name ="Person"
#     def __init__(self,name =None) :
#         self.name=name
# jeffrey= Person("Jeffrey")
# print("%s name %s" & (Person.name,jeffrey.name))
# nico=Person()
# nico.name="Nico"
# print("%s name %s" &(Person.name,nico.name))


# Câu 9
# import math
# c=150
# h=30
# value=[]
# items=[x for x in input("Nhập giá trị của d:").split(',')]
# for d in items :
#     value.append(str(int(round(math.sqrt(2*c*float((d)/h))))))
# print(','.join(value))

# Câu 10
# input_str = input("Nhập x,y :")
# dimensisons=[int(x) for x in input_str.split(',')]
# rownum=dimensisons[0]
# colnum=dimensisons[1]
# multilist=[[0 for col in range(colnum)]for row in range(rownum)]
# for row in range(rownum) :
#     for col in range (colnum):
#         multilist[row][col]=row*col
# print(multilist)

# câu 11
# items=[x for x in input("Nhập vào một chuỗi").split(',')]
# items.sort()
# print(','.join(items))

# Câu 12
# lines=[]
# while True :
#     s= input("Nhập dòng:")
#     if s :
#         lines.append(s.upper())
#     else :
#         break
# for sentence in lines :
#     print(sentence)


# Câu 13
s= input("Nhập chuỗi của bạn : ")
worlds=[word for word in s.split(" ")]
# print(" ".join(sorted(list(set(worlds)))))

# Câu 14
values=[]
items=[x for x in input("Nhập các số nhị phân :").split(',')]
for p in items :
    intp=int(p,2)
    if not intp%5 :
        values.append(p)
print(','.join(values))

# Câu 15 
# values=[]
# for i in range(999,3001) :
#     s= str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0) :
#     values.append(s)
# print(','.join(values))

# Câu 16
# s= input("Nhập câu của bạn : ")
# d={"DIGITS":0,"LETTER" :0}
# for c in s :
#     if c.isdigit() :
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTER"]+=1
#     else:
#         pass
# print("Số chữ cái là :",d["LETTER"])
# print("Số chữ là: ",d["DIGITS"])

# Câu 17

s=input("Nhập câu của bạn")
d={"upper case":0,"lower case":0}
for c in s :
    if c.isupper():
        d["upper case"]+=1
    elif c.islower():
        d["lower case"]+=1
    else :
        pass
print("Chữ hoa là",d["upper case"])
print("Chữ thường là",d["lower case"])

# Câu 18

# a= input("Nhập số a: ")
# n1= int("%s" & a)
# n2= int("%s%s" & (a,a))
# n3=int("%s%s%s" & (a,a,a))
# n4=int("%s%s%s%s" & (a,a,a,a))
# print("Tổng cần tính: ",n1+n2+n3+n4)

# Câu 19
# number=[x for x in input("Nhập sã số của bạn").split(',') if int(x)%2!=0]
# print(','.join(number))

# Câu 20
# import sys 
# netAmount=0
# while True :
#     s= input("Nhập nhật ký giao dịch: ")
#     if not s :
#         break
#     values= s.split(" ")
#     operation= values[0]
#     amount= int(values[1])
#     if operation=="D" :
#         netAmount+=amount
#     elif operation=="W" :
#         netAmount_=amount
#     else :
#         pass
# print(netAmount)

# Câu 21
# import re
# value=[]
# items=[x for x in input("Nhập mật khẩu:").split(',')]
# for p in items:
#     if len(p)<6 or len(p)>12 :
#         continue
#     else:
#         pass
#     if not re.search("[a-z]",p):
#         continue
#     elif not re.search("[0-9]",p):
#         continue
#     elif not re.search("[$#@]",p):
#         continue
#     elif re.search("\s",p):
#         continue
#     else:
#         pass
#     value.append(p)
# print(','.join(value))

# Câu 22
# from operator import itemgetter,attrgetter
# l=[]
# while True:
#     s=input("Nhập đê: ")
#     if not s :
#         break
#     l.append(tuple(s.split(',')))
# print(sorted(1,key=itemgetter(0,1,2)))

# Câu 23
# def putnumber(n):
#     i=0
#     while i<n:
#         j=i
#         i+=1
#         if j%7==0:
#             yield j
# for i in putnumber (100):
#     print(i)

# Câu 24
import math
pos=[0,0]
while True:
    s= input()
    if not s :
        break
    movement=s.split(" ")
    directation= movement[0]
    steps=int(movement[1])
    if directation=="up":
        pos[0]+=steps
    elif directation=="down":
        pos[0]-=steps
    elif directation=="left":
        pos[0]-=steps
    elif directation=="righr":
        pos[0]+=steps
    else:
        pass
