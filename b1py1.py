list1=[]
n=int(input("enter the size of element list"))
for i in range(0,n):
        element = int(input("enter the list of the elements"))
        list1.append(element)
search=int(input("enter the search element"))
for i in list1:
    if i==search:
     print("Element found")
     break
else:  
     print("Element not found")

