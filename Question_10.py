#Given a list l = [10, 20, 30, 40, 50], write a program that removes the middle element (or elements if the length is even).
l=[10, 20, 30, 40, 50]
if len(l)&1==1:
    l.pop(len(l)//2)
else:
    l.pop(len(l)//2)
    l.pop(len(l)//2-1)
print(l)


