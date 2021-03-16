# *******List / Tuple / Dictionary / Sets*******

#******** List ********
my_list = [1,20,100,5,3,20]
print(my_list)
###############################
my_list1 = ["Apple",1,1.2222]
my_list2 = [10,20,["orange",3]]
my_list3 = my_list1 + my_list2
print(my_list3)
print("Apple" in my_list3)
###############################
print(my_list3[1])
print(my_list3[5][1])
print(my_list3[2:])
print(my_list3[:-1])
###############################
for item in my_list3 :
    print(item)
###############################
my_list = ["Apple",1] * 2
print(my_list)
###############################
my_list = [100,2,30,60,20,15,1]
print(len(my_list))
print(min(my_list))
print(max(my_list))
print(sum(my_list))
print(sorted(my_list))
print(my_list)
###############################
my_list1 = ["b","c","a"]
my_list2 = ["e","d"]
my_list2.append("f")
my_list1.extend(my_list2)
print(my_list1)
print(my_list2)
my_list1.sort()
print(my_list1)
###############################
my_list1 = ["b","c","a"]
my_list1.pop()
print(my_list1)
###############################
my_list1 = ["b","c","a"]
del my_list1[1]
print(my_list1)
my_list1.remove("b")
print(my_list1)
###############################
my_list1 = [x ** 2 for x in range(5)]
print(my_list1)
###############################
my_list1 = list(map(lambda x : x ** 2, range(5)))
print(my_list1)
###############################
a = "Apple"
my_list1 = list(a)
print(my_list1)
i1,i2,i3,i4,i5 = my_list1
print(i1,i2,i3,i4,i5)
###############################
a = "This Is My First Program"
my_list1 = a.split(' ')
print(my_list1)
###############################
my_list1 = [1,2,1,3,4,1]
print(my_list1.count(1))
print(my_list1.index(1))
my_list1.reverse()
print(my_list1)
###############################
my_list1 = [1,2,1,3,4,1]
my_list1.insert(1, "Apple")
print(my_list1)

#******** Tuple ********

my_tuple = (1,20,100,5,3,20)
print(my_tuple)
###############################
my_list = ["a","b"]
t1 = ("Apple",)
t2 = t1 + (1,2,3) + tuple(my_list)
print(t2)
print(t2[0])
print(t2[1:4])
###############################
t1 = (1,["a","b","c"])
t1[1][0] = "d"
print(t1)
del t1
t1 = 1,2,3,4
print(t1)

#******** List ********

s1 = {"Apple","Apple",1,1,1,2,(1,2),(1,2)}
print(s1)
###############################
s1 = set ("abcdef")
s2 = set ("efghi")
print(s1 | s2) # OR
print(s1 & s2) # AND
print(s1 - s2) # subtract
print(s1 ^ s2) # in s1 or s2 but not in both

#******** Dictionary ********

d1 = {"Name" : "Mohammed","Age" : 28, "Edu" : "Master In Data Science"}
print(d1)
print(d1["Name"],d1["Age"],d1["Edu"])
###############################
print("Name" in d1)
print("Mohammed" in d1)
print("Mohammed" in d1.values())
###############################
print(d1.get("Age",50))
print(d1.get("Wieght",70))
###############################
my_list = list(d1)
print(my_list)
###############################
my_list2 = list(d1.items())
print(my_list2)
###############################
print(d1.keys())
###############################
d2 = {"Name" : ["Mohammed", "Ali", "hassem"],
      "Age" : [28,30,40],
      "Country" :["Sfax","Sousse","Tunis"] }
print(d2)
print(d2["Name"][1], d2["Age"][1], d2["Country"][1])
###############################
d2["Age"] = [25,30,50]
print(d2["Age"])
d2["Age"][1] = 40
print(d2["Age"])
###############################
del d2["Name"]
print (d2)
d2.clear()
print(d2)
###############################
print(type(d2))