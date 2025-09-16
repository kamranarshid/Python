mySet = {1,2,3,4,5,6,7,8,9}
print(mySet);
#add
mySet.add(10)
print(mySet);

mySet.remove(10)
print(mySet);

#union intersection difference

set1 = {1,2,3,4,5,}
set2 = {5,6,7,8,9}
union = set1|set2;
print(union);

intersection = set1 & set2;
print(intersection);

difference = set1 - set2;
print(difference);
