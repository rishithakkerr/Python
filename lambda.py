square= lambda x: x*x
print(square(5))

num=[1,2,3,4,5]
result = list(map(lambda x: x*2, num))
print(result)

gayNames = ['John', 'Paul', 'George', 'Ringo']
greet = map(lambda name: f"Hello, {name}!", gayNames)
print(list(greet))

even=list(filter(lambda x: x%2==0, num))
print(even)

students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
students.sort(key=lambda x: x[1], reverse=False)
print(students)