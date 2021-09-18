d1 = [10, 30, 20, 10]
print(d1)
# index starts from position 0,1,2 and so on
# add elements
d1.append(30)
print(d1)

#d1.append(10, 40)
#print(d1)
#append can only add one element

d1.extend([10, 40])
# extend can add more than one elements
print(d1)

d1.insert(2, 50)
print(d1)

# remove elements
d1.remove(30)
print(d1)

#d1.remove(18)
#since 18 is not in list error

d1.pop()
print(d1)

d1.pop(3)
print(d1)
# it will pop 3 element from list

d1.clear()
print(d1)
# clear functn will clear list