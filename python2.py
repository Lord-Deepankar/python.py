list1 = []
for i in range (5):
    list1.append(i)
print(list1)
n = len(list1)
target = int(input('enter digit btwn 1-10 to find in the list...'))
for i in range (n):
    if target == list1[i]:
        print("index value of target", i)    
    else:
        pass


