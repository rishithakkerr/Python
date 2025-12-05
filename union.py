thisset={"apple","banana","cherry"}
thatset={"banana","kiwi","mango"}
otherset={"cherry","orange","papaya"}

set3=thatset|thisset|otherset
print(set3)
set3.copy()
print(thisset.difference(thatset))