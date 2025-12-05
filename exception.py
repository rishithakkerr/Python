gay= input("Are you gay? (yes/no): ")

if not type(gay) is str:
    print("Welcome to the club!")
else:
    raise TypeError("You are not allowed here!")