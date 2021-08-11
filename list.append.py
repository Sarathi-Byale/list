a=[]
print("Enter the length of list")
n=int(input()) #How much Elements you need in list
for i in range (n):
  print("Enter the elements you need in list:")
  c=int(input()) # Number You have to append in list
  a.append(c)
print("Your list is:")
print(a)
n=[]
for z in range(len(a)):
  if a[z]>0:
    n.append(a[z])
print("Your list after removing the negative numbers")
print(n)
