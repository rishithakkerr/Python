f1=frozenset({1,2,3})
f2=frozenset({3,4,5}) 

print("f1=",f1)
print("f2=",f2)

#copy
f3=f1.copy()
print("f3=",f3)

#difference
f4=f1.difference(f2)
print("f4=",f4)

#intersection
f5=f1.intersection(f2)
print("f5=",f5)

#isdisjoint
f6=f1.isdisjoint(f2)
print("f6=",f6)

#issubset
f7=f1.issubset(f2)
print("f7=",f7)

#issuperset
f8=f1.issuperset(f2)
print("f8=",f8)

#symmetric difference
f9=f1.symmetric_difference(f2)
print("f9=",f9)

#union
f10=f1.union(f2)
print("f10=",f10)


