
list1=[]
n=int(input("enter the size of element list"))
for i in range(0,n):
        e=input("enter the element")
        list1.append(e)
        list1=sorted(list1)
print("the sorted elements are:",list1)
pos=int(input("enter the pos"))
ele=input("enter the element to sorted list")
list1.insert(pos,ele)
print(list1)


